[pip]: https://pip.pypa.io/en/stable/
[PyPI]: https://pypi.org/
[build]: https://pypi.org/project/build/
[setuptools]: https://setuptools.pypa.io/en/latest/index.html
[twine]: https://twine.readthedocs.io/en/latest/
[src-vs-flat]: https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/
[flat_layout]: https://setuptools.pypa.io/en/latest/userguide/package_discovery.html#flat-layout
[packaging]: https://packaging.python.org/en/latest/tutorials/packaging-projects/

This notes are based on the official packaging python projects [page][packaging].

# Requirements

We need [`pip`][pip], [`build`][build], [`setuptools`][setuptools] and [`twine`][twine]. To install them, type

```bash
python -m pip install --upgrade pip
```
```bash
python -m pip install --upgrade build
```
```bash
python -m pip install --upgrade setuptools
```
```bash
python -m pip install --upgrade twine
```

# Build, distribute and install python code

**Building** is the process of packaging (and sometimes compiling) some python source code into a *portable and distributable format*.\
There are typically two formats:
  * a **source distribution**, generally in a `.tar.gz` format (i.e. just a compressed folder with the source code);
  * and a **built distribution**, which consist of a `.whl` file, ready to be distributed and installed in any machine running python.

**Distributing** then consist on making our package available to other users.\
The simplest choice is simply sharing the `.tar.gz` and/or the `.whl` files of our package with the final user.\
However, the standard tool to use is `twine`, which uploads the `.tar.gz` and/or the `.whl` files of our package to the [PyPI][PyPI] repository.

**Installing** a package can be done using `pip`. This will install our python code on the system (or in the currently activated conda environment).
The `pip` command can be run on a local `.whl` or `.tar.gz` file, or can be used to *download and install* a package present in the PyPI repository.

To build, distribute and install python code we need a *frontend* and a *backend* tools.
In the python community there are a number of tools that can be used.
Typical frontends are the `pip` and `build` commands.
Typical backends are: `setuptools`, `Flit`, `PDM`, `hatchling`, etc.

**In this notes we will use `pip`, `build` and `setuptools`.**

# The building, distributing and installing workflow

Any python code consist of some `.py` files contained in some folders.\
Generally, the `.py` files are called **modules**, while the folders which contain them are called **packages**.\
Other files are also present, the most important are:
- `README.md`, contains a description of the project and some instructions on how to install/use it;
- `LICENSE`, contains any license/copyright information
- `pyproject.toml`, contains the *backend* installation instructions (`setuptools` in our case).

As an example, the following shows a typical [**flat-layout**][flat_layout] folder structure:

```
base_folder/
├── README.md
├── LICENSE
├── pyproject.toml
├── carwash/
│   ├── __init__.py
│   ├── washing.py
│   └── drying.py
└── tools/
    └── spray.py
```

The `pyproject.toml` file looks like this

```toml
[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"


[project]
name = "carwash"
version = "0.1"
description = "A package made to wash cars"
readme = "README.md"
requires-python = ">=3.8"
license = {file = "LICENSE"}
keywords = ["car", "wash", "clean", "spray"]
authors = [
  {name = "First Author", email = "pollo@example.com"},
  {name = "Second Author", email = "pippo@example.com"},
  {name = "Another person"},
  {email = "different.person@example.com"},
]
maintainers = [
  {name = "Someone else", email = "pippi@python.org"}
]
classifiers = [
  "Development Status :: 4 - Beta",
  "Programming Language :: Python"
]

dependencies = [
  "numpy",
  "matplotlib",
]
# dynamic = ["version", "description"]


# generally setuptools does not require explicit paths to the modules and the packages
# but in this case we need them because there are two subfolders in the project
# the carwash folder is where the actual package is
# the tools folder contains some modules
# paths to packages and modules are written in the following way
[tool.setuptools]
packages = ["carwash"]
py-modules = ["tools.spray"]


[project.urls]
Homepage = "https://example.com"
Documentation = "https://readthedocs.org"
Repository = "https://github.com/me/carwash.git"
Changelog = "https://github.com/me/carwash/blob/master/CHANGELOG.md"


[project.scripts]
carwash = "carwash.main:main_cli"
spray = "tools.spray:spray"


[project.gui-scripts]
carwash-gui = "carwash.main:main_gui"
```


The building, distrubuting and installing **workflow** is:
1. to **build** run `python -m build`: this will create a `dist` directory containing the `.whl` and `.tar.gz` files;
2. to **distribute** run `twine upload dist/*`: this will upload both the `.whl` and `.tar.gz` files to the PyPI repository. \
   Note1: uploading to PyPI requires the registration of an account. \
   Note2: it is common practise to first upload your packahe to the TestPyPI server first, and then to the official PyPI.
3. to **install** run `pip install carwash`.

# Distributing without `twine`

Uploading your package to PyPI using `twine` is *not always* what you want.\
Once the `.whl` and/or `.tar.gz` distribution files have been created, you can just share them as you like.
You can upload them as a github release, share them with a friend, or simply install them locally on your machine.
To install the package simply type

```bash
pip install /path/to/the/package.whl
```
or
```bash
pip install /path/to/the/package.tar.gz
```
