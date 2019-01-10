# grepo

> Command line interface for managing GitHub repositories.

## Usages

### Requirements

- python 3.4 or later

### Install

No package supports yet.

```sh
git clone git@github.com:HelloDHLyn/grepo.git
pip install 
```

### Commands

Before executing commands, you have to specify the name of repository.  
For default, it will be loaded from the output of `git remote get-url origin` command.

Also, grepo requires [GitHub access token](https://github.com/settings/tokens). Pass it by `GREPO_ACCESS_TOKEN` environment variable.

Available commands:

```sh
# Issue commands.
grepo issue list          # List all issues
grepo issue list --my     # List issues which assigned to me

grepo issue get <NUMBER>  # Get a issue by the nubmer
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
