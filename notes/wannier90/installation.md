# Wannier90 installation

Installation on ubuntu.

Download wannier90 from here
https://wannier.org/download/

To download an older version check this
https://github.com/wannier-developers/wannier90/tags

Install libraries\
sudo apt-get install libblas-dev liblapack-dev\
same for atlas?\
mpich or openmpi (only for wannier90.x and postw90.x)

sudo apt install gfortran

check GNU make version
make -v
if it shows GNU Make x.y then OK

create a make.inc file as follows

```
#===================
# gfortran
#===================
F90 = gfortran

COMMS  = mpi
MPIF90 = mpgfortran #mpif90

FCOPTS = -O3
LDOPTS =

#Next two lines are good for debugging
#FCOPTS = -fstrict-aliasing  -fno-omit-frame-pointer -fno-realloc-lhs -fcheck=bounds,do,recursion,pointer -ffree-form -Wall -Waliasing -Wsurprising -Wline-truncation -Wno-tabs -Wno-uninitialized -Wno-unused-dummy-argument -Wno-unused -Wno-character-truncation -O1 -g -fbacktrace
#LDOPTS = -fstrict-aliasing  -fno-omit-frame-pointer -fno-realloc-lhs -fcheck=bounds,do,recursion,pointer -ffree-form -Wall -Waliasing -Wsurprising -Wline-truncation -Wno-tabs -Wno-uninitialized -Wno-unused-dummy-argument -Wno-unused -Wno-character-truncation -O1 -g -fbacktrace


#=======================
# ATLAS Blas and LAPACK
#=======================
#LIBS = -llapack -lf77blas -lcblas -latlas

#=======================
# System LAPACK and BLAS
#=======================
#LIBS = -llapack -lblas
```

