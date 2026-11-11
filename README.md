# azir-scratch

Public scratch product repo for testing Azir: rulesets (P12), the dev workflow (P14) and the review
workflow (P15). No real code.

- `src/scratch/calc.py`: a few small functions; tests in `tests/` (pytest writes `junit.xml`).
- CI: `.github/workflows/ci.yml` (job `ci`) calls `.github/workflows/checks.yml` (job `checks`), so the
  required check is `ci / checks`. The steps are those of Azir's `azir-ci-reusable.yml`, inlined
  because this repo is public and Azir's is private.
- `review-policy.yaml`: what Azir may auto-merge here (a copy of Azir's default). `.github/CODEOWNERS`
  is generated from it with Azir's `scripts/sync_codeowners.py`.

```bash
uv sync
uv run pytest
```
