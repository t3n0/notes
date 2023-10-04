# Ubuntu clean installation

A collection of useful app and programs necessary on every Ubuntu machine.

## GUI root access

1. Set a root password (may be the same as user password) with sudo passwd root. You'll be asked to type the password twice in case of a typo.
2. Unlock the root account with sudo passwd -u root.
3. Edit sudo nano /etc/gdm3/custom.conf, and add the following line under [security]:

AllowRoot=true

4. Edit sudo nano /etc/pam.d/gdm-password, and comment out the following line by adding a # in front of it, like this:

#auth   required    pam_succeed_if.so user != root quiet_success

5. Reboot.
6. Select "Not Listed" at the login screen, then type "root" in the username field, and your root password in the password field.
7. Now you should be logged in as root in your GUI desktop.


## `gedit`
- gnuplot language support, download from [GtkSourceView](https://wiki.gnome.org/Projects/GtkSourceView/LanguageDefinitions).
Install with `sudo cp /path/to/gnuplot.lang /usr/share/gtksourceview-4/language-specs/`

## `synaptic`
 - exfat-utils (to operate on exfat filesystems)
 - eigen C++ library for linear algebra (needed to compile tortoise)

## `MateriApp`
[MateriApp](https://ma.issp.u-tokyo.ac.jp/en) is a portal for material science simulation. Install the repository from the MateriApp githbug [page](https://github.com/cmsi/MateriAppsLive/wiki/UsingMateriAppsInDebian-en) and run `sudo apt-get install <software>`. Available softwares are:
 - `vesta`
 - `quantum-espresso`
 - `XCrysDen`
 - many more

## `gnome shell extension`

## `system monitor`

## `nvidia drivers`

## `conda`
useful packages:
 - `pip install evdev`: [package](https://python-evdev.readthedocs.io/en/latest/index.html) to handle user inputs (keybord, joypads, mouse).

## `cupy`

## `gfortran`
 - coarrays
 - blas and lapack

## `quantum-espresso`
Needed libraries:
 - blas: `libblas-dev`
 - lapack: `liblapack-dev`
 - fftw: `libfftw3-dev`
 - MPI: either `mpich` (contains mpich implementation) or `openmpi` (contains LAM/MPI implementaion)

To install:
```
./configure
make all
```
To add the binaries system-wide, add `export "</path/to/qe-x.y/bin>:$PATH"` to .bashrc

To force a serial version installation:
```
./configure --disable-parallel
make all
```

Clean all files and configs:
```
make veryclean
```

## `git`

## `gnuplot`

## `zotero`
 - better bibtex for a better bibliography

## `VS Code`
Download `.deb` file from <https://code.visualstudio.com/Download>.
Install by typing `sudo apt install ./<file-name>.deb`

Extensions:
- All purpose extensions: `Git lense`, `Code runner`, `Kite`, `GitHub pull request and issues`
- `python` extensions: `Python`, `Jupyter`, `Pylance`, `Jupyter keymap`, `Jupyter Notebook Renderers`, `Magic python`
- `C++` extensions: `C/C++ extension pack` (includes `C++ intellisense`, `Better C++ syntax`, `CMake` pakgs, `remote`, etc)
- `gnuplot` extensions: `gnuplot`, `gnuplot preview`
- `markdown` extensions: `markdownlint`