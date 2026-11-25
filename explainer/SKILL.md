---
name: explainer
description: >-
  Make a visual explainer: one self-contained HTML page that explains a pull
  request, issue, bug, plan or design with pictures and only the words the
  pictures need, so the reader sees what is wrong, what changes and what is
  theirs to do, without reading code. Use when the user asks for an explainer,
  a visual explanation, to explain or show something visually, or for a page
  that explains a PR, issue, bug, plan or design. A question answered in chat
  is the explain skill, not this one.
---

The reader knows the product, has not read the code, and gives the page a few minutes. When they close it they can say what happens today, what the change does, what it leaves alone, and what is theirs to do or decide. The pictures carry the explanation: someone who looks only at the headings and the pictures still gets the story. Words are labels, plus the few sentences a picture cannot say.

**Only what is true.** Read the issue, the pull request, the code and the data before drawing anything. Every value on the page is one you read, and numbers carry the date you read them; a number taken from someone else's text says whose. A value you invented says "made-up example". A state you worked out instead of observing says "worked out, not run". What you could not confirm says "not confirmed", and what nobody has tried says "not tested". No names, emails or phone numbers of real people, and no secrets: write the role instead ("the booker's name"). Why: the page gets forwarded, and a picture is believed more easily than a paragraph.

## The story

1. **One real case, from start to end.** Pick one real example (one row, one request, one order) and follow it through every picture with its real values in monospace, so the reader can track one value from hop to hop. Name the case near the top. Where the case does not reach a branch that matters, bring in a second one for that branch and say so.
2. **Start with what the reader can see.** The symptom as it reaches them: the row, the screen, the message, with the wrong part marked. The cause comes after.
3. **The same picture for every state.** Draw the flow once, then repeat the same layout for each state: when it works, when it fails, after the change. Nothing moves between the copies, and only what differs has color. A step that exists only after the change holds its place in the earlier pictures as a dim dashed outline. The reader compares two pictures instead of reading a paragraph.
4. **Mark the exact spot.** The step where it goes wrong gets the problem color and a few words above it ("where the user is lost"). Something that should happen and does not is drawn dim and crossed out ("never asked"), never left out.
5. **Three colors, three meanings.** Orange is the problem. Green is what this change adds or fixes. Dashed amber is open: not tested, not decided, or the reader's to do. Everything else is neutral, and the legend sits under the lead.
6. **Numbers are figures.** How often, how many, how much: a big number with one line saying what it counts.
7. **Name the parts.** A change with parts labels them (Part 1, Part 2) on the picture, at the place each one acts, then gives each at most four bullets. What stays the same is a row of neutral chips: "No new column", "No API change".
8. **The reader's part is never buried.** What happens next is a row of steps in order, each saying who does it. Each thing the reader must do or decide gets its own solid callout that opens with the action. Each thing not tested or not confirmed gets a dashed one.
9. **Say where the change ends.** What is not in this change and where it goes instead. What was considered and dropped, with the one reason.

## The words

- **Title:** the question the reader would ask, in their words, with today's answer: "Who opened the gym? Today the log does not say." The ticket's own title goes in the small line above it.
- **Lead:** two or three sentences. What happens, to whom, and why it matters.
- **A heading states the finding, not the topic:** "A reservation today: the user is lost", not "Current behavior". One line under it at most.
- **The reader's vocabulary.** Product words, not code: no file paths, no function names, no code blocks. A field or status the reader will meet on a screen or in a log keeps its real name, in monospace. A vendor's or the code's name for a thing is given once, small, when the reader will hear it elsewhere ("Hikvision calls it EmployeeNo").
- **Short sentences, plain words, present tense.** One name for each thing, the same one everywhere on the page.
- **The cut test.** Remove a sentence. If the page still tells the story, it stays out. A sentence earns its place with a reason, a condition or a consequence that a picture cannot show.

## Sections

Use the ones the subject has, in this order. Each is a numbered card; the components are in `template.html`.

| Section | Shows | Component |
|---|---|---|
| What the reader sees today | one real record, screen or message, the wrong part marked | `table.row` |
| When it works | the flow for the normal case | `svg.dia` |
| Where it goes wrong | the same flow, the faulty step marked | `svg.dia` |
| A second, smaller case | a short chain: in, question, out | `.flow` |
| How often | counts and shares, with the period and the date read | `.figs` |
| After the change | the same flow again with the parts labelled, then the parts and what stays the same | `svg.dia`, `.parts`, `.facts` |
| Before and after | one line per thing the reader can observe, for the example; unchanged lines say "(same)" | `table.ba` |
| What happens next | the steps in order and who does each; what is open | `.steps`, `.callout` |
| Not in this change | what is left out, what was dropped | `.notin` |

The subject decides the sections. A bug has most of them. A feature has no failure: show today without it, then after with it. When the symptom is a cost or a count and not a record, the figures come first. For a change already merged, "today" is with it and the old state is "before". For a plan nothing has built yet, the "after" pictures are the proposal and every open decision is a callout. For someone else's pull request, the callouts are what the reviewer should check. Leave out a section the subject has nothing for; never pad one.

## Build

1. **Start from the template.** Copy `template.html` from this skill's directory. Keep its `<style>` block and the arrowheads at the top of the body, and replace the rest: it holds one of each component, with filler that says what goes there. Add a class only when no component fits. The page is one file with no scripts, no web fonts, no external images or stylesheets, so it opens from disk and can be sent as it is. Write it in the language the user writes to you in.
2. **Choose the picture.** A chain with no branches is `.flow`: it is HTML, so its text wraps by itself, and one question with several outcomes is one `.flow` row per outcome. A flow with branches, a loop, a store, or a thing inside a thing is an inline SVG on a 1200-wide viewBox. SVG text does not wrap: break the lines yourself, using the widths per character noted in the template. Draw the thing itself only when that makes it recognizable at a glance (a face, a phone, a QR); no decorative icons. The `aria-label` tells the picture's story in one sentence.
3. **Save it** where the user says; otherwise as `.claude/explainers/<subject>.html` under the repository root, such as `issue-698-amenity-qr.html`. It is not part of the change: never stage or commit it.
4. **Look at it.** A page you have not seen is not finished. Render it and read the screenshot, with the harness's browser tool or headless Chrome:

   ```bash
   "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --hide-scrollbars \
     --window-size=1280,4000 --screenshot=/tmp/explainer.png "file://$PWD/.claude/explainers/<subject>.html"
   ```

   Raise the height if the page is cut off. A tall screenshot is shrunk when you read it, and the small text in a diagram can no longer be judged: cut each diagram out and read it at full size. With `sips`, the top must be at least 1 and the top plus the height less than the screenshot's height:

   ```bash
   sips -c <height> 1280 --cropOffset <top> 1 /tmp/explainer.png --out /tmp/explainer-part.png
   ```

   Fix text that leaves its box or sits on other text, arrows that miss their box, and copies of a diagram that do not line up. Then read the page once as the reader: check every value against what you read, and apply the cut test to every sentence.
5. **Hand it over.** Reply with the `file://` link first, then, in a few lines, what is open or theirs to do. Do not retell the page in chat.
