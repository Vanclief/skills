# Mechanisms, by game

Take the mechanism, never the look. Each row is a way of putting state on screen that a game proved at scale. Build it from the project's own palette, components and icon set, so that nothing in the result says "game". Use a mechanism only where the screen has the data for it: a minimap needs something spatial, a queue needs an order.

## What do I have?

| Mechanism | Game | Use it for |
|---|---|---|
| Resource bar: icon and number, always in the same edge | Age of Empires 2 | The few totals everything else depends on |
| Used/max that changes color at the cap | StarCraft supply `12/15` | Any quota, limit or capacity |
| Supply against demand, side by side | Timberborn unemployed against vacancies (numbers); Cities: Skylines demand bars | Showing what to add next |
| Capacity, production and consumption on one graph | Satisfactory power graph | Load against headroom over time |
| Free against total, next to the icon | Frostpunk available workers | People or units not yet assigned |
| Two opposed gauges always in view | Frostpunk hope and discontent | The one or two health measures everything else serves |

## What is happening? What is next?

| Mechanism | Game | Use it for |
|---|---|---|
| Queue shown with its producer, progress on the head item | Age of Empires 2 and StarCraft selection panel; AoE2 DE strip of all queues | Jobs and pipelines: the queue sits with the thing doing the work |
| Rate per minute, produced against consumed | Factorio production stats | Flows, where a total hides the trend |
| Efficiency percent in the machine's panel | Satisfactory | How close a worker is to its ceiling |
| Tech tree: done, available, locked, and what unlocks it | Age of Empires 2 | Dependencies and prerequisites drawn as a graph |
| Ghosts: planned things drawn as outlines until built | Factorio blueprints | Pending changes, visibly different from applied ones |

## What is stuck? What needs me?

| Mechanism | Game | Use it for |
|---|---|---|
| The belt backs up in front of the slow machine; a machine with no power or fuel flashes an icon | Factorio | The constraint visible on the stage itself |
| A problem icon floating on the thing that has the problem | Frostpunk buildings: no workers, too cold, sick | Faults shown where they are, not in a separate list only |
| Idle worker button with a count, each press jumps to the next | Age of Empires 2 | Walking through everything unassigned or waiting |
| Alert that takes you there with one key | StarCraft jump to last alert | Notifications that are a jump, not a message |
| The main button becomes the next thing blocking you | Civilization "next turn" turning into "unit needs orders" | One primary action that always points at the blocker |
| Standing problem list at a fixed edge, click to jump, gone when solved | RimWorld alerts | Problems that persist until fixed, as opposed to events |

## What is coming? What changed?

| Mechanism | Game | Use it for |
|---|---|---|
| Countdown to the next hard period | Timberborn days until drought | Time until a resource runs out or a limit hits |
| Forecast strip on the main screen | Frostpunk temperature forecast | Known future changes the user must prepare for |
| A decision states its effect on the main gauges before the user commits | Frostpunk laws listing their effect on hope and discontent | Previewing the consequence of an action on the numbers it changes |
| Ping on the overview where something happened | StarCraft minimap | Change outside the current view, in the moment |
| Messages that stack at a fixed edge until read | RimWorld letters | Changes that must not be missed while away |

## Seeing and acting

| Mechanism | Game | Use it for |
|---|---|---|
| Minimap: the whole in a fixed corner, viewport marked, attention as marked dots | Every RTS | An overview that is always there |
| Selection panel: click a thing, its stats appear in the same fixed panel | Age of Empires 2, StarCraft | Detail without navigating away |
| Command card: the selected thing's actions in a fixed grid, same slots every time | StarCraft | Actions found by position; unavailable ones greyed with the reason |
| Control groups and hotkeys, the key printed on the control | StarCraft | Fast repeat access for frequent users |
| Overlays: same map, different lens | Oxygen Not Included, Cities: Skylines, Frostpunk heat overlay | Switching what is shown without switching pages |
| One toggle that prints detail on everything | Factorio alt-mode | Expert detail on demand, off by default |
| Priority as a small level control per item, or a worker-by-job grid of numbers | Timberborn building priority; RimWorld work grid | Letting the user rank work without a form |
