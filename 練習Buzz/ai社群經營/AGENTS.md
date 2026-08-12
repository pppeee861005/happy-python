# Repository Guidelines

## Project Structure & Module Organization

This repository is currently a planning space for learning [Buzz](https://github.com/block/buzz). The root `readme.MD` records project goals and open setup questions; no application code, tests, or assets are present yet. Keep general documentation at the repository root. If implementation is added, place Python modules in `src/`, automated tests in `tests/`, sample media in `assets/`, and learning notes in `docs/`. Do not commit generated transcripts, model downloads, virtual environments, or personal recordings.

## Build, Test, and Development Commands

No build or test workflow is configured yet. When Python code is introduced, document the exact supported commands in `readme.MD` and declare dependencies in `requirements.txt` or `pyproject.toml`. A conventional Windows workflow may include:

```powershell
python -m venv .venv          # Create an isolated environment
.\.venv\Scripts\Activate.ps1 # Activate it in PowerShell
python -m pytest              # Run tests after pytest is configured
```

Do not describe placeholder commands as working project commands.

## Coding Style & Naming Conventions

Use UTF-8 for text files and four spaces for Python indentation. Follow PEP 8: use `snake_case` for modules, functions, and variables; `PascalCase` for classes; and `UPPER_SNAKE_CASE` for constants. Prefer small modules, explicit imports, and type hints on public functions. Name learning notes descriptively, such as `docs/day-01-overview.md`. If a formatter or linter is adopted, commit its configuration and run it before review.

## Testing Guidelines

No test framework or coverage target exists today. New executable features should include `pytest` tests under `tests/`, mirroring the source layout. Name files `test_<module>.py` and tests `test_<behavior>()`. Mock network calls and external AI services. Tests must not require API keys, microphones, or downloaded models unless explicitly marked as integration tests.

## Commit & Pull Request Guidelines

History favors concise, imperative Chinese summaries such as `新增 ...`; Conventional Commit prefixes including `feat:`, `fix:`, `docs:`, and `refactor:` also appear. Use either established style consistently and keep each commit focused. Pull requests should explain the purpose, list verification performed, link related issues, and identify new dependencies or configuration. Include screenshots or sample output for user-visible changes.

## Security & Configuration

Never commit API keys, tokens, private recordings, or `.env` files. When configuration variables are introduced, provide a sanitized `.env.example`.
