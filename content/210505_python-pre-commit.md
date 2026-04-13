title: Automate Python Workflow With Pre-Commits: Autopep8 and Pylint
slug: python-pre-commit
date: 2021-05-05

Collaborating on a Python project? Keep the code base unified between contributers using pre-commit to streamline the workflow.

## What is pre-commit?

Pre-commit is a Git hook that triggers when `git commit` is attempted.

For Python projects, I use it to spend less time formatting my code and more time working on features and higher priority tasks.

## Get started

- `pip install pre-commit`
- add config file (`.pre-commit-config.yaml`), here's an example:

```yaml
    repos:
    - repo: https://github.com/PyCQA/pylint
      rev: pylint-2.7.2  # Use the sha / tag you want to point at
      hooks:
      - id: pylint
        exclude: ^server/
    - repo: https://github.com/pre-commit/mirrors-autopep8
      rev: v1.5.4  # Use the sha / tag you want to point at
      hooks:
      - id: autopep8
        exclude: ^server/
```

- Run `pre-commit install`
- Run `pre-commit run --all-files` the first time pre-commit is added to the project so all files are checked

Moving forward, pre-commit is triggered when `git commit` is attempted.

## Usage

Commits are not saved until they pass the pre-commit.

Based on the example configuration, all files must pass `pylint` then the same files are formatted to PEP 8 standard using `autopep8`.

Errors will provide details about the files and why the process failed. Fix the issues and commit again until they pass.

Pre-commit prevents pushing to the code base until they pass. Can you see the value in this? :)
