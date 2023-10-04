# Creating system-wide python scripts and modules

Suppose we have a folder called `myproject` with this structure:

    myproject/
        mymodule/
            __init__.py
            module.py
        myscript.py

The `myscript.py` file can be called from within the `myproject` folder
    
    tentacolo@wenjiabao:~/myproject$ python myscript.py

Or from any other location, by providing the full path to the script

    tentacolo@wenjiabao:~$ python ~/myproject/myscript.py

How do we setup a system-wide command to call `myscript` without typing all of this?

## 1) System-wide scripts: `chmod +x` and `/usr/local/bin`

These are the steps:

- first, prepend at the beginning of `myscript.py` the *shebang*: `#!/usr/bin/env python`. This tell the command line interpreter to run the default python found in the environment path (note: you can also be more specific, for example `#!/usr/bin/env python3` or `#!/usr/bin/python`, the last one is not recommended since it will bypass the environment)
- second, make the script executable by typing `chmod +x myscript.py`
- third, create a symbolic link to `myscript.py` in the `/usr/local/bin` folder by typing `ln -s ~/myproject/myscript.py /usr/local/bin/<mycommand>`, where the `<mycommand>` is the name you chose to exectute the script.

Now, you can type `<mycommand>` to execute the script from everywhere in the machine

    tentacolo@wenjiabao:~$ mycommand
    Hello from myscript.py

**Note**: This simple fix only allows to run `myscript` as a command from the terminal. It does not include our script or module in the python path (i.e. we cannot `import` it).

## 2) System-wide scripts and modules: `setuptools` and `pip`

Python provides a package called `setuptools` (which inherits from the standard `distutils` package) that is used to install and maintain python packages.
To make our module and script available to the environment we have to first create a `setup.py` file in the base folder level:

    myproject/
        mymodule/
            __init__.py
            module.py
        myscript.py
        setup.py       <--- setup file

This file will contain

    from setuptools import setup
    setup(name='mypackage',
          version='1.0',
          py_modules=['mymodule.module'],
          scripts=['myscript.py']
          )

Then, from the same folder, we run `pip install .`

If we are using a `conda` environment, the new package is going to be visible by typing `conda list`.
We can now `import mymodule.module` in any instance of the python intepreter and we can call `myscript.py` from any location in the terminal.

Finally, to get rid of our package, simply type `pip uninstall mypackage`.

More info about `setuptools` can be found in [here](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/#console-scripts) and [here](https://github.com/pypa/sampleproject).

