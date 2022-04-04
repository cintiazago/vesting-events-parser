# How to develop on this project

This project welcomes contributions from the community.

**You need PYTHON3!**

This instructions are for linux base systems. (Linux, MacOS, BSD, etc.)

## Setting up your own fork of this repo.

- On github interface click on `Fork` button.
- Clone your fork of this repo. `git clone git@github.com:YOUR_GIT_USERNAME/project_urlname.git`
- Enter the directory `cd project_urlname`
- Add upstream repo `git remote add upstream https://github.com/author_name/project_urlname`

## Setting up your own virtual environment

Run `make virtualenv` to create a virtual environment.
then activate it with `source .venv/bin/activate`.

## Run the tests to ensure everything is working

Run `make test` to run the tests.

## Create a new branch to work on your contribution

Run `git checkout -b my_contribution`

## Make your changes

Edit the files using your preferred editor. (we recommend VIM or VSCode)

## Run the linter

Run `make lint` to run the linter.

## Test your changes

Run `make test` to run the tests.

Ensure code coverage report shows `100%` coverage, add tests to your PR.

## Commit your changes

This project uses [conventional git commit messages](https://www.conventionalcommits.org/en/v1.0.0/).

Example: `fix(package): update setup.py arguments 🎉` (emojis are fine too)

## Push your changes to your fork

Run `git push origin my_contribution`

## Submit a pull request

On github interface, click on `Pull Request` button.

Wait CI to run and one of the developers will review your PR.

## Makefile utilities

This project comes with a `Makefile` that contains a number of useful utility.

```bash
❯ make
Usage: make <target>

Targets:
help:             ## Show the help.
show:             ## Show the current environment.
clean:            ## Clean unused files.
release:          ## Create a new tag for release.
lint:             ## Run pep8, black, linters.
test:        	   ## Run tests and generate coverage report.
virtualenv:       ## Create a virtual environment and install the dependencies.
```

## Making a new release

This project uses [semantic versioning](https://semver.org/) and tags releases with `X.Y.Z`
Every time a new tag is created and pushed to the remote repo, github actions will
automatically create a new release on github and trigger a release on PyPI.

For this to work you need to setup a secret called `PIPY_API_TOKEN` on the project settings>secrets,
this token can be generated on [pypi.org](https://pypi.org/account/).

To trigger a new release all you need to do is.

1. If you have changes to add to the repo
   - Make your changes following the steps described above.
   - Commit your changes following the [conventional git commit messages](https://www.conventionalcommits.org/en/v1.0.0/).
2. Run the tests to ensure everything is working.
3. Run `make release` to create a new tag and push it to the remote repo.

the `make release` will ask you the version number to create the tag, ex: type `0.1.1` when you are asked.

> **CAUTION**: The make release will change local changelog files and commit all the unstaged changes you have.
