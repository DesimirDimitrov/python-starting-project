# python-starting-project

Minimal starter Python project with a CLI, logging, and tests.

## Dependencies

This project tracks its dependencies in `pyproject.toml` and also provides a classic `requirements.txt` file for convenience.

- Runtime and dev dependencies (recommended): defined in `pyproject.toml` under `[project]` and `[project.optional-dependencies]`.
- Pinned dependency list (optional): generated in `requirements.txt` using `pip freeze`.

When you add or upgrade packages locally, update `pyproject.toml` and regenerate `requirements.txt` so other users can install the same versions.

## Setup (Windows / PowerShell)

Create and activate a virtual environment:

```pwsh
python -m venv .venv
\.venv\Scripts\Activate.ps1
```

Upgrade pip (optional but recommended):

```pwsh
python -m pip install --upgrade pip
```

Install the project in editable mode with dev dependencies:

```pwsh
pip install -e ".[dev]"
```

Alternative installation using `requirements.txt` (optional):

```pwsh
python -m venv .venv
\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Run tests with pytest:

```pwsh
pytest
```

Run the CLI via the installed script:

```pwsh
python-starting-project
python-starting-project Alice
python-starting-project Bob -v
```

Or run the CLI module directly with Python:

```pwsh
python -m python_starting_project.cli
python -m python_starting_project.cli Alice -v
```

Pylance
For strict type checking
