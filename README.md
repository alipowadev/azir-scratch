# azir-scratch

Public scratch product repo for testing Azir: rulesets (P12), the dev workflow (P14) and the review
workflow (P15). No real code.

- `src/scratch/calc.py`: a few small functions; tests in `tests/` (pytest writes `junit.xml`).
- CI: `.github/workflows/agent-ci.yml` (job `ci`, on pull requests and pushes to `main` and `agent/**`) calls `.github/workflows/checks.yml` (job `checks`), so the
  required check is `ci / checks`. The steps are those of Azir's `azir-ci-reusable.yml`, inlined
  because this repo is public and Azir's is private.
- `review-policy.yaml`: what Azir may auto-merge here (a copy of Azir's default). `.github/CODEOWNERS`
  is generated from it with Azir's `scripts/sync_codeowners.py`.

```bash
uv sync
uv run pytest
```

## Functions

The public functions of `src/scratch/calc.py`. They return floats, because `total` starts from `0.0`.

### `total(values)`

The sum of `values`; 0 for an empty list.

```python
>>> from scratch.calc import total
>>> total([1, 2, 3])
6.0

```

### `average(values)`

The mean of `values`; raises `ValueError` for an empty list.

```python
>>> from scratch.calc import average
>>> average([2, 4])
3.0

```

### `window_sums(values, size)`

The sum of each run of `size` consecutive values, in order; raises `ValueError` if `size <= 0`.

```python
>>> from scratch.calc import window_sums
>>> window_sums([1, 2, 3, 4], 2)
[3.0, 5.0, 7.0]

```
