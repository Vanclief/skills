# Status light

The status word is the light. There is no separate dot or LED: the word itself, printed exactly as the backend sent it, carries the state.

It has three channels, and each answers one question.

| Channel | Answers | Values |
|---|---|---|
| Color | What kind of thing is this? | green: the work itself. yellow: a person's turn. blue: a machine in transition. red: broken. |
| Fill | Is it alive right now? | filled: alive now. outline: not running. dim outline: not started. |
| Blink | Does it need the person looking? | blinks on arrival, then holds steady and lit. Nothing else on the screen ever blinks. |

## Tiers

The words below are examples from one project. Map each of your backend's status words to a tier once, in one place in the code, and print the backend's word unchanged.

| Tier | Example words | Look |
|---|---|---|
| Lit | running | filled green, steady |
| Lit | starting, stopping | filled blue, steady |
| Lit | review (a person's turn) | filled yellow, blinks on arrival |
| Off | done, stopped cleanly | green outline at full strength, never filled |
| Attention | crashed (died and needs a hand) | filled red with a `✕`, blinks on arrival |
| Attention | failed (ended in error, nothing to do now) | red outline with a `✕`, steady |
| Idle | open, not started yet | dim green outline |
| Unknown | a word the screen does not know | dim outline, grey text |

So one thing's life reads in one color: open → running → done is dim outline → filled → outline.

## Rules

- Finished never looks like running: done is an outline, never filled.
- A dead thing is never green.
- Red is the only red on the screen. Do not use red for decoration, branding or a concept hue.
- Red states carry a `✕` inside the word's pill, so the broken thing is findable without color. The word itself already tells the states apart when read; the mark is for the glance.
- Blink the whole word, for a few seconds when the state arrives, then hold it steady and lit. Never blink faster than three times a second. With reduced motion set, do not blink at all: the lit state alone carries it.
- Blink only when the hand needed is the hand of the person looking (SKILL.md, "Attention is personal"). A review waiting on someone else is yellow and steady.
- The filled and blinking looks belong to the status column of a list. In a plain pill away from the list, the colors live in the border and the text, and nothing blinks.
