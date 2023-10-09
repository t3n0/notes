# Extension modules with `Cython`

Python offers the capability to write C/C++ [**extension modules**](https://setuptools.pypa.io/en/latest/userguide/ext_modules.html).
This modules will have a `.c` extension and can be built using **setuptools**, provided that the system has a **C/C++ compiler** installed.

We already covered the instructions on how to build, distribute and install pure python packages on [this notes](python-packaging.md).\
To build the extension modules, we only need a **few modification** in our folder structure:
1. we need to write the actual `.c` modules;
2. we need a `setup.py` file along with the usual `pyproject.toml`.

## 1. Writing the `.c` modules using Cython



Here is an example (download [folder zip](cython.zip)):

```
base_folder/
├── README.md
├── LICENSE
├── pyproject.toml
├── setup.py           <--- we need a very basic setup.py file
├── carwash/
│   ├── __init__.py
│   ├── washing.py
│   ├── fastmodule.c   <--- and of course we need a .c module
│   └── drying.py
└── tools/
    └── spray.py
```

The content of the `setup.py` file is

```python
from setuptools import setup, Extension

myextensions = [
    Extension(name = "carwash.fast", sources = ["carwash/fastmodule.c"])
]

setup( ext_modules = myextensions )
```

As [usual](python-packaging.md), to **build the above** we type `python -m build`.\
This creates the source and built distributions (`.tar.gz` and `.whl`) ready to be installed or shared.
