# Repository Guidelines

## Project Structure & Module Organization

This repository is currently a planning space for learning [Buzz](https://github.com/block/buzz). The root `readme.MD` records the project goals and open setup questions; no application code, tests, or assets are present yet. Keep documentation at the root. If implementation is added, use `src/` for Python modules, `tests/` for automated tests, `assets/` for sample media, and `docs/` for learning notes. Do not commit generated transcripts, model downloads, virtual environments, or personal recordings.

## Build, Test, and Development Commands

There is no build or test command configured yet. After Python code is introduced, document the exact supported workflow in `readme.MD` and keep dependencies in `requirements.txt` or `pyproject.toml`. A conventional local workflow would be:

```powershell
python -m venv .venv          # create an isolated environment
.\.venv\Scripts\Activate.ps1 # activate it on Windows
python -m pytest              # run the test suite, once configured
```

Do not present placeholder commands as working project commands; update this section when tooling is actually added.

## Coding Style & Naming Conventions

Use four spaces for Python indentation and UTF-8 for all text files. Follow PEP 8: `snake_case` for modules, functions, and variables; `PascalCase` for classes; and `UPPER_SNAKE_CASE` for constants. Prefer small modules with explicit imports and type hints on public functions. Name learning notes descriptively, for example `docs/day-01-overview.md`. If a formatter or linter is adopted, commit its configuration and run it before review.

## Testing Guidelines

No test framework or coverage target exists today. New executable features should add `pytest` tests under `tests/`, mirroring the source layout. Name files `test_<module>.py` and tests `test_<behavior>()`. Mock network calls and external AI services; tests must not require API keys, microphones, or downloaded models unless explicitly marked as integration tests.

## Commit & Pull Request Guidelines

Recent history favors concise, imperative Chinese summaries such as `新增 ...`; Conventional Commit prefixes such as `feat:`, `fix:`, `docs:`, and `refactor:` also appear. Follow either established form consistently and keep each commit focused. Pull requests should explain the purpose, list verification performed, link related issues, and call out new dependencies or configuration. Include screenshots or sample output for user-visible changes.

## Security & Configuration

Never commit API keys, tokens, recordings containing private information, or `.env` files. Provide a sanitized `.env.example` whenever configuration variables are introduced.
