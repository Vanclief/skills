# Shared agent skills

This repository is the source directory for Skillshare:
`~/.config/skillshare/skills`.

The global configuration at `~/.config/skillshare/config.yaml` currently uses
copy mode and syncs skills to these targets:

| Agent | Skills directory |
| --- | --- |
| Claude Code | `~/.claude/skills` |
| Codex | `~/.codex/skills` |
| OpenCode | `~/.config/opencode/skills` |
| Pi | `~/.pi/agent/skills` |

Edit shared skills here, then run `skillshare sync`. Copies in agent directories
are refreshed when sync runs; copy mode does not continuously propagate edits.

## Orca skills

`orca-cli` and `orchestration` come from
[stablyai/orca](https://github.com/stablyai/orca/tree/main/skills).
Skillshare stores their upstream URLs, revisions, and hashes in `.metadata.json`
at this repository's root, so updates can be fetched with:

```sh
skillshare update orca-cli orchestration
skillshare sync
```

Review upstream changes with `git diff` before committing them. Keep the
Skillshare metadata with the skills when committing this repository.

These official skills load their complete guides using `orca skills get` from
the installed Orca CLI, keeping command instructions matched to that version.
Use Skillshare to manage these copies and distribute updates to all targets.

To recreate the import:

```sh
skillshare install stablyai/orca --skill orca-cli,orchestration
skillshare sync
```

On another machine, configure Skillshare to use this repository and the desired
agent targets, then run `skillshare sync`. The global configuration is outside
this repository and must be set up on that machine too.
