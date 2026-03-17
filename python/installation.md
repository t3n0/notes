# Miniconda
Just anaconda without 1 million useless packages.

## Installation

1. From the official website [download miniconda](https://docs.conda.io/projects/miniconda/en/latest/index.html) or run (for Linux)
   ```bash
   wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
   ```
   
2. Run the installer
   ```bash
   bash Miniconda3-latest-Linux-x86_64.sh
   ```
   Type `yes` agree license  
   Choose default folder: `home/user/miniconda3`  
   Type `yes` conda init

3. Check for updates
   ```bash
   conda update conda
   ```

## To uninstall

1. Run
   ```bash
   conda install anaconda-clean
   anaconda-clean --yes
   ```

2. Nuke the folder
   ```bash
   rm -rf /path/to/miniconda3
   ```

## Setting up environments and useful packages

Miniconda (as well as Anaconda) sets up a default environment called `base`.
It is advisable to always leave this env pristine and install all necessary packages in newly created envs depending on the project we are working on.

My personal take is to create a `sci` environment where I install all the most common scientific python packages and then make this environment the default.

1. Create a new env `sci`
   ```bash
   conda create -n sci
   ```

2. Make `sci` default, i.e. append `conda activate sci` to .bashrc
   ```bash
   echo "conda activate sci" >> .bashrc
   ```

3. Restart the terminal and install all the cool packages (in the current env)
   ```bash
   conda install python
   conda install numpy
   conda install matplotlib
   conda install scipy
   conda install -c conda-forge notebook
   ```

4. To check the history of the packages installed in the current env, run
   ```bash
   conda list --revisions
   ```
   This will show all the *revisions* numbered from `rev 0`, `rev 1`, `rev 2`, ... and list all packages that have been installed in those revisions.
   To restore a specific revision type
   ```bash
   conda install --rev 8
   ```
## Managing conda and other useful commands

To have a summary of the current conda installation, just run
```
conda info
```
<ol><details><summary>You should get something like this (click to expand):</summary>

```
(mpi) tentacolo@wenjiabao:~$ conda info

     active environment : mpi
    active env location : /home/tentacolo/miniconda3/envs/mpi
            shell level : 3
       user config file : /home/tentacolo/.condarc
 populated config files : /home/tentacolo/.condarc
          conda version : 24.3.0
    conda-build version : not installed
         python version : 3.12.1.final.0
                 solver : libmamba (default)
       virtual packages : __archspec=1=skylake
                          __conda=24.3.0=0
                          __cuda=12.2=0
                          __glibc=2.35=0
                          __linux=6.5.0=0
                          __unix=0=0
       base environment : /home/tentacolo/miniconda3  (writable)
      conda av data dir : /home/tentacolo/miniconda3/etc/conda
  conda av metadata url : None
           channel URLs : https://conda.anaconda.org/conda-forge/linux-64
                          https://conda.anaconda.org/conda-forge/noarch
                          https://repo.anaconda.com/pkgs/main/linux-64
                          https://repo.anaconda.com/pkgs/main/noarch
                          https://repo.anaconda.com/pkgs/r/linux-64
                          https://repo.anaconda.com/pkgs/r/noarch
          package cache : /home/tentacolo/miniconda3/pkgs
                          /home/tentacolo/.conda/pkgs
       envs directories : /home/tentacolo/miniconda3/envs
                          /home/tentacolo/.conda/envs
               platform : linux-64
             user-agent : conda/24.3.0 requests/2.31.0 CPython/3.12.1 Linux/6.5.0-26-generic ubuntu/22.04.4 glibc/2.35 solver/libmamba conda-libmamba-solver/23.12.0 libmambapy/1.5.3
                UID:GID : 1000:1000
             netrc file : None
           offline mode : False
```
</details></ol>

To add the [`conda-forge`](https://conda-forge.org/) channel and making it the highest priority, run
```
conda config --add channels conda-forge
```
In this way, the next `conda install` will try to fecth a package from `conda-forge` first, if that's available.

To query any specification about conda, a usefull command is
```
conda config --show [key]
```
For example, i want to list my channels
```
$ conda config --show channels
channels:
  - conda-forge
  - defaults
```
