# Lesson 1.1: Project setup with uv, pyproject.toml and Python 3.14

Computer Science diploma, course 1. Channel: Mahara Bel Masry. Video link: added here after the video is published.

All data in the lesson is invented for teaching. Narrated tools: uv 0.13.8, CPython 3.14.10, pytest 9.2.0. Not run in the lesson: the uv install command, `uv python install`, Windows, macOS.

## Folders
- `project/` the finished demo project (inventory-tool).
- `starter/` files to start your own exercise: `check_setup.sh`, `tests/test_total.py`, `src/inventory_tool/__init__.py`.
- `run/` the real logs of every command shown in the video (.out files).
- `self-check-1-1.md` informal 10 question self-check with answers.

## The one command
From inside `project/`:

    uv run --locked pytest -q
