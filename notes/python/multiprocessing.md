# Multiprocessing with Python

Very often a program can be split into subroutines that can be exectuded independently to each other.
In a machine with a parallel architecture, the code can take advantage of this situation by distributing each of these independent tasks to different CPUs of the system.
Nowadays, all modern computers, from laptops to High Perfomance Computers (HPCs), have a parallel architecture that can be exploited to speed up calculations.
Python offers a multitude of libraries that can be used to achieve this.
In this notes we will explore two of them:
 - the [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing) library (from the Pyhton standard library)
 - the [`mpi4py`](https://mpi4py.readthedocs.io/en/stable/) library (available with pip)

## `multiprocessing` library

The `multiprocessing` library is a useful parallelization library for machines with a [**shared memory**](https://en.wikipedia.org/wiki/Shared_memory) architecture.  
A **laptop** or a **single node** in a HPC machine are examples of shared memory machines.
This means that the `multiprocessing` is [not suitable](https://stackoverflow.com/questions/5181949/using-the-multiprocessing-module-for-cluster-computing) to distribute a parallel calculation over a cluster, where each machine/node don't share the same memory (in the case of distributed memory systems we must look into `mpi`, see the next section).

<img align="right" width="300"  src="pihits.png">

`multiprocessing` is part of the standard python library. On this tutorial we will show how to use the [`Pool`](https://docs.python.org/3/library/multiprocessing.html#using-a-pool-of-workers) class:
this class allows to create a pool of workers (i.e. processes) and provides several methods to distribute tasks to the workers.

Let's write an example: we want to calculate $\pi$ by counting how many random numbers fall inside the unit circle (see figure). 

The value of $\pi$ is then

```math
\pi \approx 4 \times \frac{h}{N}
```

where $h$ is the number of hits inside the unit circle (red dots in the figure) and $N$ is the total number of trials.

A minimal working code goes as follows (save it into a file `calculatePi.py`)

```python
import multiprocessing as mp
import numpy.random as rng


def hitCount(trials):
    """
    Counts how many times the random variable hits the inner circle.
    """
    hits = 0
    for _ in range(trials):
        x = rng.random() 
        y = rng.random()
        if ( x**2 + y**2 < 1.0 ):
            hits += 1 
    return hits


def serialPi(trials):
    """
    Calculates PI in serial.
    Just a single call to the `hitCount` function.
    """
    hits = hitCount(trials)
    pi = 4.0 * hits / trials  
    return pi


def parallelPi(trials, nprocs = 1):
    """
    Calculates PI in parallel.
    The `hitCount` function is called using `nprocs` processes at once.
    """    
    trials_per_proc = trials // nprocs
    pool_trials = [ trials_per_proc for i in range(nprocs-1) ]
    pool_trials.append(trials - trials_per_proc * (nprocs-1))
	
    with mp.Pool(nprocs) as pool:
        hits = pool.map(hitCount, pool_trials)
    
    pi = 4.0 * sum(hits) / trials  
    return pi
```

We see that the function `hitCount(trials)` is at the core of our implementation. This function only depends on the number of trials and returns the number of hits inside the unit circle.
This is the task that we want to parallelise over the workers (processes). To do so we use the `Pool.map` method. This is the easiest way to distribute a task over a pool of processes.

`Pool.map` wants a function (`hitCount` in our case) and a list of inputs for that function. Pyhton then takes care of evaluating the function over the given input list by distributing the workload over the workers. When the job is done, `Pool.map` returns a list with the results.

Pay attention that it is up to us to determine how much work load to distribute to the workers. Specifically, we split the trials into a list of trials, e.g. with 500 trials and 8 processors, the trials for every job are `pool_trials = [62, 62, 62, 62, 62, 62, 62, 66]`. In this way, every processor receives a similar amount of work to be performed.

Let's test it!

```bash
Python 3.12.1 | packaged by conda-forge | (main, Dec 23 2023, 08:03:24) [GCC 12.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import calculatePi
>>> calculatePi.serialPi(10**6)
3.140744
>>> calculatePi.parallelPi(10**6, 4)
3.13976
>>> import timeit
>>> timeit.timeit('calculatePi.serialPi(N)', number=5, setup='import calculatePi; N=10**6')
4.027927483002713
>>> timeit.timeit('calculatePi.parallelPi(N, 4)', number=5, setup='import calculatePi; N=10**6')
1.1624885639976128
```

We see that using 4 processors we achieve almost a **4x speed up**!

## MPI for python: `mpi4py`

[MPI](https://en.wikipedia.org/wiki/Message_Passing_Interface) stands for Message Passing Interface.
It is a communication protocol that defines how nodes/machines on a cluster can communicate between each other.
The most common libraries that implement this protocol are [`OpenMPI`](https://www.open-mpi.org/) and [`MPICH`](https://www.mpich.org/).  
Regarding python, `mpi4py` builds on top of the C++ MPI bindings and supports all the standards up to MPI-3.1 ([Dalcin-Fang](https://doi.org/10.1109/MCSE.2021.3083216)).
This tool allows to write prallel code on machines with a [distribute memory](https://en.wikipedia.org/wiki/Distributed_memory) architecture,
which makes it the most common choice to write code on HPC clusters.

### Installation (Linux)

The installation on Linux is easily done in the terminal via `apt` and `pip`:

1. Install your flavour of MPI: OpenMPI or MPICH

   ```bash
   apt install openmpi
   ```

2. Install `mpi4py` via pip

   ```bash
   pip install mpi4py
   ```
   If the above command fails, that could be because of the underlying anaconda environment.
   In my case, I got a linker error regarding the `compiler_compat` folder.
   Just rename the folder to some `compiler_compat_bak` and re-run `pip install`.

3. (optional) Depending on your system, it might happen that running an MPI code produces the warning `Invalid MIT-MAGIC-COOKIE-1 key`
   (more info [here](https://unix.stackexchange.com/questions/630428/invalid-mit-magic-cookie-1-when-i-run-mpirun)).
   To solve this just add the following to your `.bashrc`
   ```bash
   export HWLOC_COMPONENTS="-gl"
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


### Hello world

We start with a very easy program: copy the following into a `hello-world.py` file

```python
from mpi4py import MPI

comm = MPI.COMM_WORLD
nprocs = comm.Get_size()
myrank = comm.Get_rank()

print(f"Hello! I am rank {myrank} in group of {nprocs} processes.")
```

then run

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
4. As long as every process terminates, each processor prints the string to the standard output.

It is important to understand that `mpirun` distributes the very same *identical* code to all processes.
From that point on every process proceeds independently, unless a call to one of the MPI communication function is done.

Note: generally, `mpirun` complains if the requested number of processes exceeds the number of physical cores in a machine.
For example, in my laptop I have 4 physical cores (hyper-threading does not count). So if I try to submit the job with `mpirun -n 5` I get

```
$ mpirun -n 5 python basic.py 
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
mpirun -n 5 --oversubscribe python basic.py 
Hello! I am rank 2 in group of 5 processes.
Hello! I am rank 1 in group of 5 processes.
Hello! I am rank 4 in group of 5 processes.
Hello! I am rank 0 in group of 5 processes.
Hello! I am rank 3 in group of 5 processes.
```


### Tutorials

The following examples are based on this [source](https://fs.hlrs.de/projects/par/par_prog_ws/practical/MPI31single.zip).




