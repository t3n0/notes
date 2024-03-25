# MPI for python: `mpi4py`

[MPI](https://en.wikipedia.org/wiki/Message_Passing_Interface) stands for Message Passing Interface.
It is a communication protocol that defines how nodes/machines on a cluster can communicate between each other.
The most common libraries that implement this protocol are [`OpenMPI`](https://www.open-mpi.org/) and [`MPICH`](https://www.mpich.org/).  
Regarding python, `mpi4py` builds on top of the C++ MPI bindings and supports all the standards up to MPI-3.1 ([Dalcin-Fang](https://doi.org/10.1109/MCSE.2021.3083216)).  
This tool allows to write prallel code on machines with a [distribute memory](https://en.wikipedia.org/wiki/Distributed_memory) architecture,
which makes it the most common choice to write code on HPC clusters.

## Installation (Linux)

The installation on Linux is easily done in the terminal. There are two pathways

1. via `apt` and `pip`
2. via `conda`

**1. Pip installation**

- Install your flavour of MPI: OpenMPI or MPICH

   ```bash
   apt install openmpi
   ```

- Install `mpi4py` via pip

   ```bash
   pip install mpi4py
   ```
   If the above command fails, that could be because of the underlying anaconda environment.
   In my case, I got a linker error regarding the `compiler_compat` folder.
   Just rename the folder to some `compiler_compat_bak` and re-run `pip install`.

- (optional) Depending on your system, it might happen that running an MPI code produces the warning `Invalid MIT-MAGIC-COOKIE-1 key`
   (more info [here](https://unix.stackexchange.com/questions/630428/invalid-mit-magic-cookie-1-when-i-run-mpirun)).
   To solve this just add the following to your `.bashrc`
   ```bash
   export HWLOC_COMPONENTS="-gl"
   ```

**2. Conda installation**

- Using conda, mpi4py is available in the `conda-forge` channel. Simply type
   ```
   conda install mpi4py -c conda-forge
   ```

You can check the successful installation by opening the python interpreter
```bash
Python 3.12.1 | packaged by conda-forge | (main, Dec 23 2023, 08:03:24) [GCC 12.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from mpi4py import MPI
>>> MPI.Get_version()
(3, 1)
```
MPI 3.1 is correctly installed.

---

## Hello world

We start with a very easy program: copy the following into a `hello-world.py` file

```python
from mpi4py import MPI

comm = MPI.COMM_WORLD
nprocs = comm.Get_size()
myrank = comm.Get_rank()

print(f"Hello! I am rank {myrank} in group of {nprocs} processes.")
```

then run (my laptop has 4 cores)

```
mpirun -n 4 python hello-world.py
```

You should see

```
Hello! I am rank 0 in group of 4 processes.
Hello! I am rank 1 in group of 4 processes.
Hello! I am rank 2 in group of 4 processes.
Hello! I am rank 3 in group of 4 processes.
```

MPI works in the following way:
1. The command `mpirun -n 4` instructs the operative system to distribute the program to 4 processors.
2. The program to execute is `python hello-world.py`.
3. Every processor receives an *identical* copy of the program and executes it.
4. As long as every process terminates, each processor prints the string to the standard output and returns.

It is important to understand that `mpirun` distributes the very same *identical* code to all processes.
From that point on every process proceeds independently, unless a call to one of the MPI communication function is done.

NOTE: generally, `mpirun` complains if the requested number of processes exceeds the number of physical cores in a machine.
For example, in my laptop I have 4 physical cores (hyper-threading does not count). So if I try to submit the job with `mpirun -n 5` I get

```
$ mpirun -n 5 python hello-world.py
--------------------------------------------------------------------------
There are not enough slots available in the system to satisfy the 5
slots that were requested by the application:

  python

Either request fewer slots for your application, or make more slots
available for use.

A "slot" is the Open MPI term for an allocatable unit where we can
launch a process.  The number of slots available are defined by the
environment in which Open MPI processes are run:

  1. Hostfile, via "slots=N" clauses (N defaults to number of
     processor cores if not provided)
  2. The --host command line parameter, via a ":N" suffix on the
     hostname (N defaults to 1 if not provided)
  3. Resource manager (e.g., SLURM, PBS/Torque, LSF, etc.)
  4. If none of a hostfile, the --host command line parameter, or an
     RM is present, Open MPI defaults to the number of processor cores

In all the above cases, if you want Open MPI to default to the number
of hardware threads instead of the number of processor cores, use the
--use-hwthread-cpus option.

Alternatively, you can use the --oversubscribe option to ignore the
number of available slots when deciding the number of processes to
launch.
--------------------------------------------------------------------------
```

To overcome this simply add the `--oversubscribe` flag

```
mpirun -n 5 --oversubscribe python hello-world.py
Hello! I am rank 2 in group of 5 processes.
Hello! I am rank 1 in group of 5 processes.
Hello! I am rank 4 in group of 5 processes.
Hello! I am rank 0 in group of 5 processes.
Hello! I am rank 3 in group of 5 processes.
```


## Tutorials

The following examples are based on this [source](https://fs.hlrs.de/projects/par/par_prog_ws/practical/MPI31single.zip).

1. Broadcast a variable from the master process to all other processes
   
   ```python
   from mpi4py import MPI
   comm = MPI.COMM_WORLD
   myrank = comm.Get_rank()
   nprocs = comm.Get_size()

   # We define n in all processes
   n = None

   # If we are process 0, we initialised the variable n
   if (myrank == 0):
   	n = int(input("Enter n: ")) # e.g. we read it from input

   # the command bcast broadcasts the vanlue of n from process 0 to all other processes
   n = comm.bcast(n, root=0)

   # now every process has n, we can do useful calculations, e.g.
   myresult = n * myrank
   
   print(f"I am process {myrank} out of {nprocs}, my result is {myresult}")
   ```



