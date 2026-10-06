# fairsharer

![CI](https://github.com/sorassword/fairsharer/actions/workflows/ci.yml/badge.svg)

Small university exercise (HSD Düsseldorf) on packaging, testing and CI for Python.

`fair_sharer(values, num_iterations, share=0.1)` redistributes values on a ring: in every iteration the largest value gives a fraction `share` to each of its two neighbours (the first and last element are neighbours).

```python
from src.fair_sharer import fair_sharer

fair_sharer([0, 1000, 800, 0], 1)  # -> [100, 800, 900, 0]
fair_sharer([0, 1000, 800, 0], 2)  # -> [100, 890, 720, 90]
```

## What it practises

- `pyproject.toml`-based project layout (`src/`, `tests/`)
- unit tests with **pytest**
- a **GitHub Actions** workflow that runs the tests on every push

## Run the tests

```bash
pip install pytest
pytest
```
