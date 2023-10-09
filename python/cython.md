# Extension modules with `Cython`

Python offers the capability to write C/C++ **extension modules**.
This modules will have a `.c` extension and can be built using **setuptools**, provided that the system has a **`C` compiler** installed.

We already covered the instructions on how to build, distribute and install pure python packages on [this notes](python-packaging.md).
To bulding the extension modules, we only need a few modification in our folder structure.
Here is an example (download zip):

```
base_folder/
├── README.md
├── LICENSE
├── pyproject.toml
├── setup.py                <--- we need a very basic setup.py file
├── carwash/
│   ├── __init__.py
│   ├── washing.py
│   ├── veryfastCmodule.c   <--- and of course we need a .c module
│   └── drying.py
└── tools/
    └── spray.py
```
