## Miniconda
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
   Type `yes`: agree license  
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
