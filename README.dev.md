# `sequgen` developer documentation

For user documentation, go [here](README.md).

## Development install

``` {.sourceCode .shell}
# Create a virtualenv, e.g. with
python3 -m venv venv3

# activate virtualenv
source venv3/bin/activate

# make sure to have a recent version of pip
pip install --upgrade pip

# (from the project root directory)
# install sequgen as an editable package
pip install --no-cache-dir --editable .
# install development dependencies
pip install --no-cache-dir --editable .[dev]
```

## Running the tests

Running the tests requires an activated virtualenv with the development
tools installed.

``` {.sourceCode .shell}
# unit tests with mocked representations of repository behavior
pytest
pytest tests/

```

## Running linters locally

Running the linters requires an activated virtualenv with the
development tools installed.

``` {.sourceCode .shell}
# linter
prospector

# recursively check import style for the sequgen module only
isort --recursive --check-only sequgen

# recursively check import style for the sequgen module only and show
# any proposed changes as a diff
isort --recursive --check-only --diff sequgen

# recursively fix  import style for the sequgen module only
isort --recursive sequgen
```

``` {.sourceCode .shell}
# requires activated virtualenv with development tools
prospector && isort --recursive --check-only sequgen
```

You can enable automatic linting with `prospector` and `isort` on commit
like so:

``` {.sourceCode .shell}
git config --local core.hooksPath .githooks
```

## Documentation

In the Python code use [Google formatted docstrings](https://google.github.io/styleguide/pyguide.html#381-docstrings).

### Generate API documentation locally

The API documentation is hosted at [https:/sequgen.readthedocs.io](https:/sequgen.readthedocs.io) and is automatically updated when `main` branch is updated.

To generate the API documentation locally do

```shell
# Install Sphinx dependencies
pip install -e .[dev]
cd docs
make html
```

The generated <docs/_build/html/index.html> can be opened in web browser for your viewing pleasure.

## Versioning

Bumping the version across all files is done with bump2version, e.g.

``` {.sourceCode .shell}
bump2version minor
```

## Making a release

### Preparation

1.  Update the `CHANGELOG.md`
2.  Verify that the information in `CITATION.cff` is correct, and that
    `.zenodo.json` contains equivalent data
3.  Make sure the version has been updated.
4.  Run the unit tests with `pytest tests/`

### PyPI

In a new terminal, without an activated virtual environment or a venv3
directory:

``` {.sourceCode .shell}
# prepare a new directory
cd $(mktemp -d --tmpdir sequgen.XXXXXX)

# fresh git clone ensures the release has the state of origin/main branch
git clone https://github.com/sequgen/sequgen.git .

# prepare a clean virtual environment and activate it
python3 -m venv venv3
source venv3/bin/activate

# make sure to have a recent version of pip
pip install --upgrade pip

# install runtime dependencies and publishing dependencies
pip install --no-cache-dir .
pip install --no-cache-dir .[publishing]

# clean up any previously generated artefacts
rm -rf sequgen.egg-info
rm -rf dist

# create the source distribution and the wheel
python setup.py sdist bdist_wheel

# upload to test pypi instance (requires credentials)
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

In a new terminal, without an activated virtual environment or a venv3
directory:

``` {.sourceCode .shell}
cd $(mktemp -d --tmpdir sequgen-test.XXXXXX)

# check you don't have an existing sequgen
which sequgen
python3 -m pip uninstall sequgen

# install in user space from test pypi instance:
python3 -m pip -v install --user --no-cache-dir \
--index-url https://test.pypi.org/simple/ \
--extra-index-url https://pypi.org/simple sequgen
```

Check that the package works as it should when installed from pypitest.

Then upload to pypi.org with:

``` {.sourceCode .shell}
# Back to the first terminal,
# FINAL STEP: upload to PyPI (requires credentials)
twine upload dist/*
```

### GitHub

Don't forget to also make a release on GitHub.
