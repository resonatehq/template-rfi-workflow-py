# RFI workflow - Resonate Python SDK application template

The repository serves as a template for scaffolding projects with the Resonate CLI.

Install dependencies:

```
uv sync
```

Both bar and baz are designed to run as services, each uses `Event().wait()` to stay running.

Run bar:

```
uv run bar
```

Run baz:

```
uv run baz
```

Foo runs as a script.

Run foo:

```
uv run foo
```
