# Installing Siesta

Super straight forward guide to install [Siesta](https://siesta-project.org/siesta/) on Ubuntu (because windows... why?).\
The full installation manual can be found [here](https://docs.siesta-project.org/projects/siesta/en/latest/how-to/index.html#how-to-build-siesta).

1. Install `gfortran`
   
   ```bash
   sudo apt install build-essential gfortran
   ```
3. Install an MPI implementation: for example `openmpi`
   ```bash
   sudo apt install libopenmpi-dev openmpi-bin
   ```
3. Install `blas`, `lapack` and `scalapack` libraries
   ```bash
   sudo apt install libblas-dev liblapack-dev libscalapack-mpi-dev
   ```
4. Install `HDF5` and `NetCDF` input/output libraries
   ```bash
   sudo apt install libhdf5-dev libhdf5-mpi-dev libnetcdf-dev libnetcdff-dev netcdf-bin
   ```
5. Install `curl` and/or `wget`
   ```bash
   sudo apt install curl wget
   ```
6. Siesta needs `CMake` >= 3.17. To install CMake just type
   ```bash
   sudo apt install cmake
   ```
   Check you CMake version by typing `CMake --version`. If this version is not up to date, you ha two options:
   1. Install via `snap`
   2. Install manually

   **i. Snap install**

      1. Uninstall the current CMake
         ```bash
         sudo apt purge --auto-remove cmake
         ```
      2. Simply run
         ```bash
         sudo snap install cmake --classic
         ```
         the `--classic` flag is necessary because cmake uses a classic [snap confinement](https://snapcraft.io/docs/snap-confinement).

   **ii. Manual install**

      1. Uninstall the current CMake
         ```bash
         sudo apt purge --auto-remove cmake
         ```
      2. Download the latest binary release from [cmake.org](https://cmake.org/download).\
         For example, at the time of writing, this is `cmake-3.27.7-linux-x86_64.sh`.
      3. Copy the script file in some meaningfull folder
         ```bash
         cp cmake-3.27.7-linux-x86_64.sh /home/user/cmake/
         ```
         Of course, replace the name with your cmake version.
      4. Execute the script
         ```bash
         bash cmake-3.27.7-linux-x86_64.sh
         ```
         and follow the instructions: accept license yes, version folder yes.
      5. Export the `bin` to PATH.




[Download](https://gitlab.com/siesta-project/siesta/-/releases)
