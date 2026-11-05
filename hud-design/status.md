# Status light

The status word is the light. There is no separate dot or LED: the word itself, printed exactly as the backend sent it, carries the state. Printing the backend's word keeps the screen, the logs and the API on one vocabulary.

It has three channels, and each answers one question.

| Channel | Answers | Values |
|---|---|---|
| Color | What kind of thing is this? | green: the work itself. yellow: a person's turn. blue: a machine in transition. red: broken. |
| Fill | Is it alive right now? | filled: alive now. outline: not running. dim outline: not started. |
| Blink | Does it need the person looking? | blinks on arrival, then holds steady. Nothing else on the screen ever blinks. |

## Tiers

The words below are examples from one project. Map each of your backend's status words to a tier once, in one place in the code.

| Tier | Example words | Look |
|---|---|---|
| Live | running | filled green, steady |
| Live | starting, stopping | filled blue, steady |
| Live | review (a person's turn) | filled yellow, blinks on arrival |
| Off | done, stopped cleanly | green outline at full strength, never filled |
| Broken | crashed (died and needs a hand) | filled red with an x mark, blinks on arrival |
| Broken | failed (ended in error, nothing to do now) | red outline with an x mark, steady |
| Idle | open, not started yet | dim green outline |
| Unknown | a word the screen does not know | dim outline, grey text |

So one thing's life reads in one color: open → running → done is dim outline → filled → outline.

Live is not the same as asking. A screen full of filled green words is a healthy screen; only yellow that is the viewer's turn and red ask for anything.

## Rules

- Finished never looks like running: done is an outline, never filled.
- A dead thing (crashed or failed) is never green.
- Red means broken or destructive, nothing else: never decoration, branding or a concept hue.
- Broken states carry an x mark from the project's icon set inside the word's pill, so the broken thing is findable without color. The word already tells the states apart when read; the mark is for the glance.
- Blink the whole word, for a few seconds when the state arrives, then hold it steady. Never faster than three times a second. With reduced motion set, do not blink at all: the filled state alone carries it.
- Blink only for a person who can act on it: the reviewer whose turn it is, the owner of the thing that crashed (SKILL.md, "Attention is personal"). For everyone else the same state is steady.
- The filled and blinking looks belong to the status position of a row in a list. In a plain pill away from the list, the colors live in the border and the text, and nothing blinks.
