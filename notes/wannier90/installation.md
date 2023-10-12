# Wannier90 installation

A super straight forward guide to instal [Wannier90](https://wannier.org/) on Ubuntu.\
The complete installation guide is [here](https://github.com/wannier-developers/wannier90/blob/develop/README.install).

1. Install `blas` and `lapack` libraries
   
   ```bash
   sudo apt install libblas-dev liblapack-dev
   ```
2. Install an MPI implementation: either `mpich` or `openmpi`
   ```bash
   sudo apt install mpich
   ```
3. Install `gfortran`, aka the gcc f90 compiler
   ```bash
   sudo apt install gfortran
   ```
4. Check GNU make version, e.g. `GNU Make 4.2.1`
   ```bash
   make -v
   ```
5. [Download](https://wannier.org/download/) the latest wannier90 (older versions [here](https://github.com/wannier-developers/wannier90/tags))
6. Unzip the folder at you favorite location and create a `make.inc` file with the following content
   ```
   #===================
   # gfortran
   #===================
   F90 = gfortran

   COMMS  = mpi
   MPIF90 = mpif90

   FCOPTS = -O3
   LDOPTS =

   #Next two lines are good for debugging
   #FCOPTS = -fstrict-aliasing  -fno-omit-frame-pointer -fno-realloc-lhs -fcheck=bounds,do,recursion,pointer -ffree-form -Wall -Waliasing -Wsurprising -Wline-truncation -Wno-tabs -Wno-uninitialized -Wno-unused-dummy-argument -Wno-unused -Wno-character-truncation -O1 -g -fbacktrace
   #LDOPTS = -fstrict-aliasing  -fno-omit-frame-pointer -fno-realloc-lhs -fcheck=bounds,do,recursion,pointer -ffree-form -Wall -Waliasing -Wsurprising -Wline-truncation -Wno-tabs -Wno-uninitialized -Wno-unused-dummy-argument -Wno-unused -Wno-character-truncation -O1 -g -fbacktrace

   #=======================
   # System LAPACK and BLAS
   #=======================
   LIBS = -llapack -lblas
   ```
7. Open the terminal in the base folder and run the following (this builds `wannier90.x` and `postw90.x` executables only)
   ```bash
   make default
   ```
8. (optional) Add `wannier90.x` and `postw90.x` to the PATH, so that they can run system-wide. Do **either**
   - add to `bin`
     
     ```bash
     ln -s /path/to/wannier/folder/wannier90.x /usr/local/bin/wannier90.x
     ln -s /path/to/wannier/folder/postw90.x /usr/local/bin/postw90.x
     ```
   - add to PATH: append this line to `.bashrc`
     ```bash
     export PATH="/path/to/wannier/folder:$PATH"
     ```
9. Enjoy!

NOTES:
- To clean/remove/uninstall wannier90, simply type `make clean` or `make veryclean`.
- If you want to install a new version of wannier90, you can either remove the old one (just nuke the folder) or you can simply install it by side.
  For example, assume the following folder structure
  
  ```
  /home/username/
  └── wannier90/
      ├── wannier90-3.0.0/
      │   ├── bunch of files
      │   └── wannier90.x      <-- version 3.0.0
      └── wannier90-3.1.0/
          ├── bunch of files
          └── wannier90.x      <-- version 3.1.0
  ```
  We need to choose 2 different names for the symbolic links in `usr/local/bin`, for example (choose whatever name)
  ```bash
  ln -s /home/username/wannier90/wannier90-3.0.0/wannier90.x   /usr/local/bin/pollo.x
  ln -s /home/username/wannier90/wannier90-3.1.0/wannier90.x   /usr/local/bin/wannier90.x
  ```
- The wannier installation guide suggest to use [atlas](http://math-atlas.sourceforge.net/) as the BLAS implementatio. I found it to be quite difficult to install.\
  So it can go to **hell**! Standard lapack and blas are more than enough.
