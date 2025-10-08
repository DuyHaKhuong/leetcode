# Repository Guidelines

## Project Structure & Module Organization
- Source files: top-level Python scripts, one per LeetCode problem (e.g., `split-array-by-prime-indices.py`).
- Naming: lowercase kebab-case mirroring the problem title; version or approach suffixes allowed (e.g., `best-time-to-buy-and-sell-stock-v.py`, `minimum-cost-path-heap.py`).
- Notebooks live at the root (e.g., `Untitled.ipynb`); checkpoints are in `.ipynb_checkpoints/`.

## Build, Test, and Development Commands
- Run a solution: `python <file>.py` (if it includes a `__main__` harness). Otherwise, import in a REPL or notebook.
- Quick ad-hoc timing: `python -m timeit -n 10 -r 3 -s "from <module> import solve" "solve(<args>)"`.
- Optional pytest (if you add tests): `pytest -q` from repo root.

## Coding Style & Naming Conventions
- Python, 4-space indentation, PEP 8. Keep imports stdlib-only unless noted.
- Function names: `snake_case`; classes: `CamelCase`.
- Prefer pure functions; avoid global state. Add type hints and a short docstring with complexity.
- Example header:
  """
  Two pointers; O(n) time, O(1) space.
  """

## Testing Guidelines
- Minimal inline tests under `if __name__ == "__main__":` are encouraged for new files.
- If using pytest, place tests in `tests/` as `test_<slug>.py` (e.g., `tests/test_partition_string.py`) and cover edge cases (empty input, single element, extremes).
- Target correctness first; include a few adversarial cases per function.

## Commit & Pull Request Guidelines
- Commits: imperative, concise subjects (<= 72 chars). Include problem slug and approach.
  - Example: `add: partition-string.py using greedy set (O(n))`
- Description: link the LeetCode problem, outline approach and complexity, and note trade-offs.
- PRs: one problem per PR; include a short summary, sample input/output (or references to tests), and any benchmarks if performance-driven. Link related issues if applicable.

## Environment & Dependencies
- Target Python 3.10+.
- Keep solutions dependency-free unless essential; prefer standard library data structures and algorithms.

## Architecture Notes
- Each file is self-contained. If sharing utilities, keep helper functions local to the file to preserve portability to LeetCode’s runner.
