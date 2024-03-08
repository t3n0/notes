# Multiprocessing with Python

Very often a program can be split into subroutines that can be exectuded independently to each other.
In a machine with a parallel architecture, the code can take advantage of this situation by distributing each of these independent tasks to different CPUs of the system.
Nowadays, all modern computers, from laptops to High Perfomance Computers (HPCs), have a parallel architecture that can be exploited to speed up calculations.
Python offers a multitude of libraries that can be used to achieve this.
In this notes we will explore two of them:
 - the [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing) library (from the Pyhton standard library)
 - the [`mpi4py`](https://mpi4py.readthedocs.io/en/stable/) library (available with pip)

## `multiprocessing`

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

A minimal working code goes as follows

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

## `mpi4py`



install openmpi

rename the folder `compiler_compat` to some `compiler_compat_bak`

so to avoid the linker error 

run pip install mpi4py

