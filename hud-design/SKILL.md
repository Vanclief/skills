---
name: hud-design
description: >-
  Design a screen as a HUD, the way strategy, factory and colony games do
  (Age of Empires 2, StarCraft, Factorio, Satisfactory, Timberborn, Frostpunk):
  the whole state is on screen and read at a glance through icons, slots,
  numbers, color and shape, so the user never reads a paragraph, holds anything
  in their head, or wonders what to do next. Use when designing or reviewing a
  dashboard, control panel, monitoring or operations screen, a screen that
  supervises agents or jobs, or a config or creation form, and whenever the
  user wants UI that is "visual", "like a game", "at a glance", "intuitive",
  "don't make me think", "no YAML/JSON/code in the UI", or says HUD,
  hud-design or rtsdesign. It borrows how games show information, never how
  they look: no game styling, no gamification.
---

Design for a user who holds nothing in their head and remembers nothing from their last visit. The screen is their memory, and it must be operable with every sentence removed: icons, slots, numbers, color and shape carry the meaning, and text is a one or two word label at most. If a control needs a sentence to explain it, redesign the control.

**The look.** Games are the source of the mechanisms, never of the look. The finished screen looks like an ordinary, well-made screen in this product's own design system, only denser and quicker to read: the project's palette, type, components and icon set, flat surfaces, thin borders. No glow, gradients, bevels, textures, emoji, pixel art, medieval or sci-fi styling, sound, or decorative motion. No gamification: no points, streaks, badges, leaderboards, timers that pressure the user, or confetti. If someone could tell from a screenshot that games inspired it, it is wrong.

**Only real data.** Everything on screen comes from data the system really has. Unknown progress is shown as working, without a percentage. No forecast without a measured rate. No "changed since you looked" without a stored last-seen. Where the backend lacks what a region needs, leave the region out and say so in your reply; never fake it and never quietly add state.

Work in two layers, in this order: first what the screen answers, then how each thing is drawn. A screen that follows every drawing rule but leaves a question unanswered is a tidy form, not a HUD.

## Layer 1: what the screen answers

At any moment, without a click and without reading a sentence, the screen answers these. Each answer lives in one fixed region.

| Question | What answers it | Where games do it |
|---|---|---|
| What do I have? | A bar of icon-and-number totals, capacity as used/max | AoE2 resource bar, StarCraft supply `12/15` |
| What is happening? | Every running thing shows its own progress on itself | The bar filling on a building under construction |
| What is next? | The queue in order: in progress, next, waiting, and what each waits on | AoE2 production queue |
| What is stuck? | The constraint is marked: the stage with work piling up in front of it | Factorio's belt backing up in front of the slow machine |
| What needs me? | A count, and one control that jumps to the next thing waiting on this user | AoE2 idle villager button, StarCraft jump to last alert |
| What is coming? | A forecast in time | Timberborn's days until drought, Frostpunk's temperature forecast |
| What changed? | A trail of changes since the user last looked | RimWorld's letters, which stay until read |
| Did that work? | Every action changes the screen at once | A unit selected, a building placed |

Answer every question the screen's data can answer. Where the data has no answer (a settings form has no queue), leave the region out. More mechanisms, by game, are in `patterns.md`.

1. **Nothing lives in the user's head.** If the user would have to remember it, compare it across two screens, or recall what it was before, it goes on screen. Why: people hold only a few items at once; a screen holds all of them.
2. **Progress sits on the thing itself.** Anything that takes over a second shows it is working; over ten seconds, which step it is on, and when it ends if that is known. Results arrive on their own: the user never refreshes to find out. Why: a wait with no feedback reads as broken.
3. **Show the relationship, not only the number.** In against out, used against capacity, produced against consumed, side by side on one scale, as rates and not only totals. Mark the constraint, one per pipeline: the stage with work piling up in front of it and idle stages after it. The backed-up stages before it and the starved ones after it are symptoms and stay dim. The mark is the warning icon in the amber of a person's turn, because a constraint is a person's to fix. Why: the useful question is what throttles the rest, and a lone total cannot answer it.
4. **Forecast in time.** `empty in 12 min`, not `12% left`. Wherever a resource drains, a queue grows or a limit approaches, say when. Why: seeing the present is too late to act on it.
5. **Leave a trail.** Something that changed while the user looked elsewhere keeps a steady highlight until the user has seen it, and a fixed log lists changes newest first, each one a jump to the thing. Why: people miss a large share of the changes that happen while their attention is elsewhere.
6. **Asking stays rare.** In normal operation almost nothing asks for the user. The jump control walks what waits on them, most urgent first; rows keep their place, and what waits is never scrolled out of sight or hidden behind a switch. Repeats of one alarm collapse into one with a count. If the screen still asks constantly, the alarm is set wrong: say so, never leave the user to triage. Why: when everything alarms, nothing does.
7. **Short visits.** The user acts on a thing where it is shown, from its row or panel, without navigating away. The few most frequent actions have a key, printed on the control. Why: how many things one person can run depends on how short each visit is.
8. **Workers say what they are doing.** Anything that works on its own (an agent, a job, a machine) shows in its row what it is doing now, what it waits on and, when known, when it will next need the user. Why it chose that is one click away, never in the row. Why: the user can only leave a worker alone if they can see at a glance that it is still fine.
9. **Stale is a state.** If live data stops arriving, the screen says so (`stale since 12:04`) and live statuses dim. Why: a frozen screen that still looks live is the worst failure a HUD has.

## Layer 2: how each thing is drawn

In priority order.

1. **Show the thing, not a description of it.** A resource is its icon and a number (the memory icon and `4 GB`), never "memory: 4096 MiB". The few things attached to a record (the repos on an agent) are a row of tiles, never a comma-separated string. Raw formats (YAML, JSON, config text) are never the primary view; keep them behind a `</>` toggle.
2. **One icon per concept, everywhere.** Pick the icon for CPU, memory, repo, secret, volume or channel once and use it in every list, card, detail and form. Icons come from the project's icon set: never emoji, never a second set; if the project has none, pick one set and say so. An icon the project invented keeps its one or two word label; only icons everyone knows (search, close, settings) go bare, and those still get an accessible name. Why: unlabeled custom icons are often guessed wrong.
3. **Color codes concepts, saturation codes attention.** The few concepts the screen is about (rarely more than five) each get one hue to go with their icon, used on the icon, its chips, its card header and its selected state, and kept clearly apart from the status colors. Everything else is neutral. Saturation is for what needs the eye: the primary action, the selected chip, a live status, an error. Inert things are dim. Red means broken or destructive, nothing else. Never let hue be the only difference between two meanings: add a fill, a shape or a mark. Why: a screen that is all grey is as unreadable as one that is all color, and one man in twelve cannot tell red from green.
4. **Slots make absence visible.** An empty slot is a dashed outline with a `+` where the thing would be. No label saying "none yet".
5. **Numbers come from presets.** A quantity is a row of chips (`1 2 4 8`) or a stepper with sane steps, the current value filled. Free-text numeric input is a last resort. The unit is on the chip, in the unit humans think in (GB, not MiB). Numbers use tabular figures and align right in columns.
6. **Status is one light: the word itself.** No separate dot or LED. The status word, printed exactly as the backend sent it, is colored by kind (green the work itself, yellow a person's turn, blue a machine in transition, red broken) and filled when alive now, outlined when not running. Finished never looks like running and a dead thing is never green. The tiers are in `status.md`; read it before drawing any status.
7. **Motion is for a hand.** The only thing that moves for attention is a status word that needs the person looking: it blinks for a few seconds when the state arrives, then holds steady. With reduced motion set it never blinks. Why: motion is the strongest pull the eye has, so it is spent on one thing.
8. **Toggles are switches, options are chips.** A boolean is a switch that visibly flips. Picking from a known set is a row of toggle chips, selected filled and unselected outlined. Mutually exclusive choices are a segmented control.
9. **Group with panels, not headings.** Related controls sit in one bordered card with a single icon in its corner, in the card's concept color. Headings are one word. No section descriptions.
10. **Explanations live in tooltips; content does not.** What a help sentence would say goes into a tooltip on the icon, reachable by keyboard focus as well as hover. A disabled control says in its own label why it is disabled. Content the user came to read (an agent's question, an error, a diff, a log line) is not explanation: show it in full where it is acted on.
11. **One obvious primary action.** Each panel or dialog has one filled primary button in the same corner every time. Secondary actions are smaller and outlined. Where a panel has fixed action slots, the slots keep their place and the filled one is whichever action the thing needs now. Destructive actions are red, physically separated, and confirmed by a second click in place.
12. **Instant visible feedback, and no more.** Every click changes something on screen immediately: a chip fills, a slot gets content, a count increments, a button shows busy. One visible change per action; no flourish. Why: feedback helps until it becomes a show, then it hurts.
13. **Fixed positions.** The same information lives in the same place on every screen. Never reflow panels based on content. The top-level areas of the app are all on screen at once, as groups the user can collapse, never as modes that hide each other: a collapsed group still shows its header, icon and badge, so nothing that needs attention is ever behind a switch. Why: people find things by where they were.
14. **Lists are rows, not cards.** A collection of records is flat rows with a hairline separator; colored borders are for the selected item and for panels (rule 9). A row reads left to right: the edge mark if it waits on the viewer (rule 15), the status word (rule 6), the name in normal weight, the facts as dim text in a fixed order, the act chip. A chip in a row is for something you click or something asking (a live count, a warning), never for plain facts like a model name or a person. Ten rows of equal chips read as noise: the eye must land on the status, then the name, then nothing else unless it looks.
15. **Attention is personal.** "Needs a hand" is always someone's hand. When a thing waits on the person looking, its row carries one amber mark at the left edge and a short filled chip naming the act (`accept`, `answer`), and the section's badge counts it. When it waits on someone else, show that name in dim text beside the status (`review · @ana`). Never highlight everything that waits on anyone.
16. **Derived facts are shown as results, not rules.** Instead of "the repo is cloned to /home/agent/<name>", a path chip that updates as the user types: `/home/agent/my-repo`.

## Method

1. Inventory every piece of data the screen carries and classify each: quantity, capacity, rate, time, boolean, pick-from-set, free text, list of items, path, derived, content to read.
2. Go down the Layer 1 questions. For each, name the region that answers it, or say the data has no answer.
3. Assign each piece of data a control from the table below and the project's icon for it.
4. Lay the regions out in fixed positions, controls as cards in a grid, most used first, primary action pinned.
5. Delete every sentence of explanation. Move what it said into a tooltip or make the control carry it.
6. Test, and fix what fails:
   - **No text**: hide every label; the screen is still operable. Then restore the one or two word labels.
   - **Five seconds**: after one glance, say what is stuck and what needs you.
   - **No color**: in greyscale, the broken thing and the thing waiting on you are still findable.
   - **Back from lunch**: after an hour away, the screen shows what changed without scrolling a history.
   - **Screenshot**: it looks like the rest of the product, and nothing in it says "game".

When reviewing an existing screen, report unanswered Layer 1 questions first, then drawing rule violations.

| Data | Control |
|---|---|
| quantity with sensible values | preset chips or stepper, unit on chip |
| capacity | used/max number on a bar, marked when near full |
| rate | number per unit of time, next to the rate it feeds or drains |
| time until something | countdown chip (`empty in 12 min`) |
| progress | bar on the thing itself, with the step name when long |
| boolean | switch |
| pick one of a known set | segmented control with icons |
| pick many of a known set | toggle chips |
| things attached to a record | tile row, one tile per item, trailing empty slot with `+` |
| collection of records | rows |
| free text | input with a leading icon, placeholder shows an example value |
| path or identifier | mono chip |
| derived value | read-only chip that updates live |
| content to read (message, error, diff) | shown in full where it is acted on |
| long optional text (script) | collapsed card that expands on click, never open by default |
| raw format for experts | `</>` toggle revealing the text, off by default |
