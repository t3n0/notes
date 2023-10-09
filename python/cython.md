# Extension modules with `Cython`

Python offers the capability to import C/C++ [**extension modules**](https://setuptools.pypa.io/en/latest/userguide/ext_modules.html).
This modules will have a `.c` extension and can be built using **setuptools**, provided that the system has a **C/C++ compiler** installed.

We already covered the instructions on how to build, distribute and install pure python packages on [this notes](python-packaging.md).\
To build the extension modules, we only need a **few modification** in our project:
1. we need to write the actual `.c` modules;
2. we need a `setup.py` file along with the usual `pyproject.toml`.

## 1. Writing the `.c` modules using Cython

From the Cython official [documentation](https://cython.readthedocs.io/en/latest/src/quickstart/overview.html) we read that
"Cython is a programming language that makes **writing C extensions** for the Python language **as easy as Python itself**".

There are [two syntax variants](https://cython.readthedocs.io/en/latest/src/quickstart/cythonize.html) to write a module:
1. **cython** variant: the module is a `.pyx` file and use the `cdef` keyword, *no need* to `import cython`;
2. **pure python** variant: the module is a standard `.py` file, we must `import cython` and declare variable following PEP-484 type hints and PEP 526 variable annotations.

In the following we show the first variant (because I like it more).\
Create a `fastmodule.pyx` file containing the following

```python
def f(double x):
    return x ** 2 - x


def integrate_f(double a, double b, int N):
    cdef int i
    cdef double s
    cdef double dx
    s = 0
    dx = (b - a) / N
    for i in range(N):
        s += f(a + i * dx)
    return s * dx
```

To translate this into the extension module `fastmodule.c` simply type
```
cythonize -i -a fastmodule.pyx
```

Now, our `fastmodule.c` can be imported and used from the python interpreter with `import fastmodule`. Done.

Notes:
- `-i` means inplace, i.e. the `.c` files are created in the same folder of the `.pyx` files;
- `-a` means annotation, an html file containing info about the cython to C conversion is also created (this is very important to further optimize the code).
- the above code is not fully optimized. The `f(x)` funcntion has no declared type. Declaring the type of `f(x)` can further boost the speed up, see [here](https://cython.readthedocs.io/en/latest/src/quickstart/cythonize.html).

## 2. The `setup.py` file

Once we have all our `.c` modules in place, we just have to tell setuptools where they are in order to build the distribution.\
This is done by writing a very specific `setup.py` file in the base folder, close to the usual `pyproject.toml`.\
Supposed we have the following folder structure (download [folder zip](cython.zip)):

```
base_folder/
├── README.md
├── LICENSE
├── pyproject.toml
├── setup.py           <--- we need a very basic setup.py file
├── carwash/
│   ├── __init__.py
│   ├── washing.py
│   ├── fastmodule.c   <--- the .c module we created previously
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
