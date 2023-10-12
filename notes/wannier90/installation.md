# Wannier90 installation

A super straight forward guide to instal [Wannier90](https://wannier.org/) on Ubuntu.\
The complete installation guide is [here](https://github.com/wannier-developers/wannier90/blob/develop/README.install).

1. Install `blas` and `lapack` libraries
   
   ```bash
   sudo apt install libblas-dev liblapack-dev
   ```
3. Install an MPI implementation: either `mpich` or `openmpi`
   ```bash
   sudo apt install mpich
   ```
4. Install `gfortran`, aka the gcc f90 compiler
   ```bash
   sudo apt install gfortran
   ```
5. Check GNU make version, e.g. `GNU Make 4.2.1`
   ```bash
   make -v
   ```
6. [Download](https://wannier.org/download/) the latest wannier90 (older versions [here](https://github.com/wannier-developers/wannier90/tags))
7. Unzip the folder at you favorite location and create a `make.inc` file with the following content
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
8. Open the terminal in the base folder and run the following (this builds `wannier90.x` and `postw90.x` executables only)
   ```bash
   make default
   ```
9. (optional) Add `wannier90.x` and `postw90.x` to the PATH, so that they can run system-wide
   ```bash
   pollo
   ```
10. Enjoy!

NOTE:\
- atlas is a mess to install, it can go to hell
- lapack and blas are more than enough
- all other install options can be found at https://github.com/wannier-developers/wannier90/blob/develop/README.install

