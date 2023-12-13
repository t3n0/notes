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
   conda install numpy
   conda install matplotlib
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

When $\Gamma = 0$ then
$$p = \int dx $$
```math
p = \sum_{n=0}^N a_n
```
