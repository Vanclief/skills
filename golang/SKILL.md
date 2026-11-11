---
name: golang
description: >-
  Use when writing, modifying, refactoring, or reviewing Go (Golang) code,
  including tests. Apply the user's rules for error handling and the ez
  error library, and the checks to run before finishing.
---

The user skims Go code and does not read it line by line, so these rules cover what a skim will not catch. Formatting is not one of them: `gofmt` decides the layout, and where Go offers two forms, such as `if err := f(); err != nil {` or the assignment on its own line, use the one the file already uses. In a review, report a violation of the rules below as a correctness finding and do not report style.

## Errors

Never drop an error silently. Return it or act on it. Where ignoring it is correct, say why in a comment on that line.

Name error variables `err`. Do not invent per-call names such as `parseErr` for an error that is checked and returned on the spot.

## ez

These apply where the module already uses `github.com/vanclief/ez`. Do not add it to a module that does not.

- Create an error where it originates with `ez.New(code, message, cause)`, or `ez.Root(code, message)` when there is no cause. Pass it up with `ez.Wrap(err)`. The operation name comes from the calling function, so there is nothing to pass.
- `ez.Wrap` on an error that is not from ez gives it the code `internal`, except for timeouts and cancellations. When you know what the error means, create it instead: `ez.New(ez.ENOTFOUND, "User not found", err)` for `sql.ErrNoRows`.
- Never wrap an ez error with `fmt.Errorf("...: %w", err)`. `ez.ErrorCode`, `ez.ErrorMessage` and `ez.ErrorData` stop at the first wrapper that is not an ez error, so the code is lost and the error is reported as `internal`.
- Use the `ez.E*` constants, and pick the code by what the caller should do next: `EUNAVAILABLE` when a retry may help, `EINTERNAL` when it will not, `EINVALID` for input that failed validation, `ECONFLICT` for a valid request the current state forbids. The HTTP status and gRPC code are derived from it.
- The message is shown to end users. Write a sentence they can act on, and keep internal detail out of it: the underlying error goes in `cause` and context goes in `AddData`.
- Classify an error with `ez.ErrorCode(err)`, never by matching its message.

## Before finishing

The checks stand in for the reading the user no longer does. On the packages you touched: `gofmt -l` prints nothing, `go vet` and `go build` are clean, and the tests pass, with `-race` when the change touches goroutines or shared state. Use the repository's own lint and test commands where it has them. Report what you ran and what it printed.
