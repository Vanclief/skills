---
name: draw
description: >-
  Draw on, read, or edit the canvas in the user's "tldraw offline" desktop app
  through its built-in local HTTP agent API (no UI automation). Use whenever the
  user asks to draw, sketch, add, move, or inspect shapes, boxes, arrows, notes,
  text, or diagrams in tldraw, their whiteboard, or "my canvas", or invokes
  /draw with a request. Also use to create a new .tldraw file or read what is
  currently on the board.
---

# Draw in tldraw offline

The tldraw offline app (`/Applications/tldraw offline.app`, Electron) runs a local
HTTP server while open. Talk to it with curl; never try to click the UI.

The arguments to `/draw` are the drawing request. Restate the request in canvas
terms (which shapes, where, sizes) before writing code.

## Connect

Every shell call is fresh, so read the token inline each time. The token changes
on every app launch.

```bash
TOKEN=$(jq -r .token "$HOME/Library/Application Support/tldraw/server.json")
BASE=http://localhost:7236
```

If `server.json` is missing or `pgrep -f "tldraw offline"` finds nothing, launch
the app with `open -a "tldraw offline"` and wait for `server.json` to appear with
a fresh `pid`.

`GET $BASE/` needs no auth and returns the full API reference in markdown. It is
the source of truth; read it (or the relevant section) when anything below is not
enough. Worked recipes live in `api.recipes` (see "When you need more").

Both `/api/search` and `/api/doc/<id>/exec` take the code as raw JavaScript
(`content-type: text/plain`), which avoids JSON escaping. The code runs inside an
async function; return plain JSON.

## Workflow

1. **Find the document** and read what is already on it:

   ```bash
   curl -s -X POST $BASE/api/search -H 'content-type: text/plain' \
     -H "authorization: Bearer $TOKEN" --data-binary @- <<'JS'
   const doc = await api.getFocusedDoc()
   const page = doc ? await api.getShapes(doc.id) : null
   return {
     doc,
     viewport: page?.viewport,
     shapes: page?.shapes.map(s => ({ id: s.id, type: s.type, x: s.x, y: s.y, props: s.props })) ?? [],
   }
   JS
   ```

   `doc.id` is the target for `/exec`. `viewport` tells you where the user is
   looking; place new shapes inside it. To start a brand-new file instead, `POST
   $BASE/api/docs/create` with `{"name":"My board"}` (saved to ~/Documents).

2. **Edit** with `POST $BASE/api/doc/<docId>/exec`. `editor` (live tldraw Editor)
   and `helpers` are in scope.

   ```bash
   curl -s -X POST "$BASE/api/doc/$DOC/exec" -H 'content-type: text/plain' \
     -H "authorization: Bearer $TOKEN" --data-binary @- <<'JS'
   const { createShapeId, toRichText } = await import('tldraw')
   const id = createShapeId('box1')
   editor.createShape({
     id, type: 'geo', x: 570, y: 300,
     props: { geo: 'rectangle', w: 300, h: 300, richText: toRichText('Label') },
   })
   editor.select(id)
   return { created: id }
   JS
   ```

   Shapes are raw tldraw SDK records (`TLShapePartial`). Common types: `geo`
   (`props.geo`: rectangle, ellipse, triangle, diamond, ...), `text`, `note`,
   `arrow`. Connect boxes with `helpers.createArrowBetweenShapes(idA, idB)` so
   arrows are actually bound. Default styles unless the user asks for color or
   fill. A typical labeled box is about 300x200 with ~200 gap between shapes.

   `helpers.mermaid(source)` draws a whole diagram in one call, but its arrows
   come corner-pinned with large `bend` values inside a `group`, often routed
   through neighbouring boxes. Use it only for a diagram you will not rearrange,
   and screenshot it once. To move its boxes anyway: ungroup, set each arrow's
   `bend` to 0, and `editor.updateBindings` to `{ isPrecise: false, normalizedAnchor: { x: .5, y: .5 } }`.

3. **Verify once**: re-run the step 1 read to check the new ids are there, and
   run `return helpers.getLints()` through `/exec`, fixing only lints your edit
   introduced. Take a screenshot (`api.getScreenshot(doc.id)` returns a file
   path) only if placement is uncertain or the user asks for visual proof.

4. **Save** only when the doc is local and has a `filePath`: end the snippet with
   `await helpers.saveDoc()`. If `filePath` is `null` the board has never been
   saved and needs a human to choose a location; tell the user to press Cmd+S
   instead of calling `saveDoc`.

## When you need more

- Unknown Editor method: `POST /api/search` with
  `return api.members.filter(m => m.name.includes('align')).map(m => ({ name: m.name, signature: m.signature }))`.
- Recipes (stacking, arrows, mermaid diagrams, clickable UI, board scripts):
  `return Object.values(api.recipes).map(r => ({ id: r.id, whenToUse: r.whenToUse }))`,
  then `return api.recipes['<id>'].body`.
- Anything installed via `/exec` (listeners, timers) dies when the doc closes.
  Behavior that must survive belongs in a board script via
  `POST /api/doc/<id>/script-workspace`; read that section of `GET $BASE/` first.

## Gotchas

- Never edit the `.tldraw` file on disk while it is open in the app.
- A snippet that throws is rolled back. One stopped with
  `DELETE /api/doc/<id>/snippets/<snippetId>` is not; undo or compensate by hand.
- Hand-built `draw` shape segments crash validation; use `compressLegacySegments` from `'tldraw'`.
