# Quick-bench

Quick run a command across different git tags of package.

## Usage

```bash
hrun run <repo-path> --tags <tags> -- <cmd>
hrun run <repo-path> --tags <tags> --case-dir <case-path> -- <partial-cmd>
```

### Multiple versions

```bash
hrun run . --tags 3.1.12 3.2.2 -- python app.py
hrun run . --tags 3.1.12 3.2.2 -- time python app.py
hrun run . --tags 3.1.12 3.2.2 -- python -m timeit app.py
```

### Multiple cases

To run multiple cases at once, you may create a collection of case directories,
each one containing a single entrypoint file to be executed:

```bash
$ tree
mycases/
  case_a/
    app.py
    additional.toml
  case_b/
    app.py
$ hrun run 3.1.12 3.2.2 --cases-dir cases --entrypoint app.py
Running v3.1.12 [case_a]
...
Running v3.1.12 [case_b]
...
Running v3.2.2 [case_a]
...
Running v3.2.2 [case_b]
```

## Configuration

- `DATA_FOLDER`: where internal stuff goes (e.g. the managed venvs)
- `DEFAULT_CASES_DIR`: where the program will look for test cases, by default.
