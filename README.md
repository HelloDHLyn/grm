# grepo

> Command line interface for managing GitHub repositories.

## Usages

### Install

TBD

### Commands

Before executing commands, you have to specify the name of repository. For default, it will be loaded from the output of `git remote get-url origin` command.

Available commands:

```sh
# Repo commands.
grepo issue list
```


## Development

### Prerequisites

- python 3
- pipenv

### Run

```sh
# Install dependencies and launch virtual environment.
pipenv install -d
pipenv shell

# Execute commands.
python grepo.py <commands> ...
```
