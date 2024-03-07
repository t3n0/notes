# Multiprocessing with Python

Very often a program can be split into subroutines that can be exectuded independently to each other.
In a machine with a parallel architecture, then the code can take advantage of this situation by distributing the each of these independent tasks to all the CPUs of the system.
Nowadays, all modern computers, from laptops to High Perfomance Computers (HPCs), have a parallel architecture that can be exploited to speed up calculations.
Python offers a multitude of libraries that can be used to achieve this.
In this notes we will explore two of them:
 - the [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing) library (from the Pyhton standard library)
 - the [`mpi4py`](https://mpi4py.readthedocs.io/en/stable/) library (available with pip)

install openmpi

rename the folder `compiler_compat` to some `compiler_compat_bak`

so to avoid the linker error 

run pip install mpi4py

