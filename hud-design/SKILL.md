---
name: hud-design
description: >-
  Design a screen as a HUD, the way strategy, factory and colony games do
  (Age of Empires 2, StarCraft, Factorio, Satisfactory, Timberborn): the whole
  state is on screen and read at a glance through icons, slots, numbers, color
  and shape, so the user never reads a paragraph, holds anything in their head,
  or wonders what to do next. Use when designing or reviewing a dashboard,
  control panel, monitoring or operations screen, or any interface the user
  wants "visual", "like a game", "at a glance", "intuitive", "don't make me
  think", "no YAML/JSON/code in the UI", or when they say HUD, hud-design or
  rtsdesign. Not a visual theme: no medieval or sci-fi styling, no
  gamification.
---

Design for a user who holds nothing in their head and remembers nothing from their last visit. The screen is their memory, and it must be operable with every sentence removed: icons, slots, numbers, color and shape carry the meaning, and text is a one or two word label at most. If a control needs a sentence to explain it, redesign the control.

Work in two layers, in this order: first what the screen answers, then how each thing is drawn. A screen that follows every drawing rule but leaves a question unanswered is a tidy form, not a HUD.

## Layer 1: what the screen answers

At any moment, without a click and without reading a sentence, the screen answers these. Each answer lives in one fixed region.

| Question | What answers it | Where games do it |
|---|---|---|
| What do I have? | A bar of icon-and-number totals, capacity as used/max | AoE2 resource bar, StarCraft supply `12/15` |
| What is happening? | Every running thing shows its own progress on itself | The bar filling on a building under construction |
| What is next? | The queue in order: in progress, next, waiting, and what each waits on | AoE2 production queue |
| What is stuck? | The one stage throttling the rest is lit | Factorio's backed-up belt and starved machine |
| What needs me? | A count, and one control that jumps to the next thing waiting on this user | AoE2 idle villager button, StarCraft jump to last alert |
| What is coming? | A forecast in time | Timberborn's days until drought |
| What changed? | A trail of changes since the user last looked | StarCraft minimap ping and alert |
| Did that work? | Every action changes the screen at once | A unit selected, a building placed |

Answer every question the screen's data can answer. Where the data has no answer (a settings form has no queue), leave the region out; never invent one. More mechanisms, by game, are in `patterns.md`: take the mechanism, never the look.

1. **Nothing lives in the user's head.** If the user would have to remember it, compare it across two screens, or recall what it was before, it goes on screen. Why: people hold only a few items at once; a screen holds all of them.
2. **Progress sits on the thing itself.** Anything that takes over a second shows it is working; over ten seconds, which step it is on and when it ends. Results arrive on their own: the user never refreshes to find out. Why: a wait with no feedback reads as broken.
3. **Show the relationship, not only the number.** In against out, used against capacity, produced against consumed, side by side on one scale, as rates and not only totals. Light the first stage that is starved or backed up, and only that one: the stages behind it are waiting on it and stay dim. Why: the useful question is always what throttles the rest, and a lone total cannot answer it.
4. **Forecast in time.** `empty in 12 min`, not `12% left`. Wherever a resource drains, a queue grows or a limit approaches, say when. Why: seeing the present is too late to act on it.
5. **Leave a trail.** Something that changed while the user looked elsewhere keeps a steady highlight until the user has seen it, and a fixed log lists changes newest first, each one a jump to the thing. Why: people miss a large share of the changes that happen while their attention is elsewhere.
6. **Lit stays rare.** In normal operation almost nothing is lit. What waits on the user sorts to the top, most urgent first, and the jump control walks it in that order. If many things are lit at once the threshold is wrong: fix the threshold, never leave the user to triage. Why: when everything alarms, nothing does.
7. **Short visits.** The user acts on a thing where it is shown, from its row or panel, without navigating away. Frequent actions have a key, printed on the control. Why: how many things one person can run depends on how short each visit is.
8. **Workers say what they are doing.** Anything that works on its own (an agent, a job, a machine) shows in its row what it is doing now, what it waits on and, when known, when it will next need the user. Why it chose that is one click away, never in the row. Why: the user can only leave a worker alone if they can see at a glance that it is still fine.

## Layer 2: how each thing is drawn

In priority order.

1. **Show the thing, not a description of it.** A resource is an icon and a number (`⛁ 4 GB`), never "memory: 4096 MiB". A list of items is a row of tiles, never a comma-separated string. Raw formats (YAML, JSON, config text) are never the primary view; keep them behind a `</>` toggle.
2. **One icon per concept, everywhere.** Pick the icon for each concept once and use it in every list, card, detail and form, from the project's existing icon set; never mix sets. An icon the project invented keeps its one or two word label; only icons everyone knows (search, close, settings) go bare. Why: unlabeled custom icons are guessed wrong most of the time.
3. **Color codes concepts, saturation codes attention.** Each concept gets one hue to go with its icon, used on the icon, its chips, its card header and its selected state. Everything else is neutral. Saturation is for what needs the eye: the primary action, the selected chip, a live status, an error. Inert things are dim. Keep the hues few, and never let hue be the only difference between two meanings: add a fill, a shape or a mark. Why: a screen that is all grey is as unreadable as one that is all color, and one man in twelve cannot tell red from green.
4. **Slots make absence visible.** An empty slot is a dashed outline with a `+`, like an empty inventory square. No label saying "none yet".
5. **Numbers come from presets.** A quantity is a row of chips (`1 2 4 8`) or a stepper with sane steps, the current value lit. Free-text numeric input is a last resort. The unit is on the chip, in the unit humans think in (GB, not MiB).
6. **Status is one light: the word itself.** No separate dot or LED. The status word, printed exactly as the backend sent it, is colored by kind (green the work itself, yellow a person's turn, blue a machine in transition, red broken) and filled when alive now, outlined when not running. Finished never looks like running, a dead thing is never green, and red is the only red on the screen. The full tiers are in `status.md`; read it before drawing any status.
7. **Motion is for a hand.** The only thing that ever moves for attention is a status word that needs the person looking: it blinks for a few seconds when the state arrives, then holds steady and lit. With reduced motion set it never blinks. Why: motion is the strongest pull the eye has, so it is spent on one thing, and blinking that never stops shuts some users out.
8. **Toggles are switches, options are chips.** A boolean is a switch that visibly flips. Picking from a known set is a row of toggle chips, selected filled and unselected outlined. Mutually exclusive choices are a segmented control.
9. **Group with panels, not headings.** Related controls sit in one bordered card with a single icon in its corner, in the card's concept color. Headings are one word. No section descriptions.
10. **Explanations live in tooltips.** Everything a help sentence would say goes into a hover tooltip on the icon. The one exception: a disabled control says in its own label why it is disabled.
11. **One obvious primary action.** Each panel or dialog has one big, lit primary button in the same corner every time. Secondary actions are smaller and outlined. Destructive actions are red, physically separated, and confirmed by a second click in place.
12. **Instant visible feedback, and no more.** Every click changes something on screen immediately: a chip fills, a slot gets content, a count increments, a button shows busy. One visible change per action; no flourish. Why: feedback helps until it becomes a show, then it hurts.
13. **Fixed positions.** The same information lives in the same place on every screen, like a minimap always in its corner. Never reflow panels based on content. The top-level areas are all on screen at once, as groups the user can collapse, never as modes that hide each other: a collapsed group still shows its header, icon and badge. Why: people find things by where they were.
14. **Lists are rows, not cards.** A list item is a flat row with a hairline separator; colored borders are for the selected item and for panels (rule 9). A row has one light at the left (rule 6), the name in normal weight, and everything else as dim text in a fixed order. A chip in a row is for something you click or something lit (a live count, a warning), never for plain facts. The eye lands on the light, then the name, then nothing else unless it looks.
15. **Attention is personal.** "Needs a hand" is always someone's hand. When a thing waits on the person looking, its row carries one lit amber mark at the left edge and a short lit chip naming the act (`accept`, `answer`), and the section's badge counts it. When it waits on someone else, show that name in dim text beside the status (`review · @ana`), never lit.
16. **Derived facts are shown as results, not rules.** Instead of "the repo is cloned to /home/agent/<name>", a path chip that updates as the user types: `📁 /home/agent/my-repo`.

## Method

1. Inventory every piece of data the screen carries and classify each: quantity, capacity, rate, time, boolean, pick-from-set, free text, list of items, path, derived.
2. Go down the Layer 1 questions. For each, name the region that answers it, or say the data has no answer.
3. Assign each piece of data a control from the table below and the project's icon for it.
4. Lay the regions out in fixed positions, controls as cards in a grid, most used first, primary action pinned.
5. Delete every sentence. Move what it said into a tooltip or make the control carry it.
6. Test, and fix what fails:
   - **No text**: hide every label; the screen is still operable. Then restore the one or two word labels.
   - **Five seconds**: after one glance, say what is stuck and what needs you.
   - **No color**: in greyscale, the broken thing and the thing waiting on you are still findable.
   - **Back from lunch**: after an hour away, the screen shows what changed without scrolling a history.

When reviewing an existing screen, report unanswered Layer 1 questions first, then drawing rule violations.

| Data | Control |
|---|---|
| quantity with sensible values | preset chips or stepper, unit on chip |
| capacity | used/max number on a bar, lit when near full |
| rate | number per unit of time, next to the rate it feeds or drains |
| time until something | countdown chip (`empty in 12 min`) |
| progress | bar on the thing itself, with the step name when long |
| boolean | switch |
| pick one of a known set | segmented control with icons |
| pick many of a known set | toggle chips |
| list of items | tile row, one tile per item, trailing empty slot with `+` |
| free text | input with a leading icon, placeholder shows an example value |
| path or identifier | mono chip |
| derived value | read-only chip that updates live |
| long optional text (script) | collapsed card that expands on click, never open by default |
| raw format for experts | `</>` toggle revealing the text, off by default |

## What this is not

Not pixel art, not medieval or sci-fi styling, not sound effects, not skeuomorphism. Not gamification either: no points, streaks, badges, leaderboards, timers that pressure the user, or confetti. Use the project's existing palette and components. The game influence is purely in how information is communicated: densely, graphically, at a glance.
