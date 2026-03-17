# Managing libraries on Ubuntu

Libraries are a set of compiled code that can be used by various programs in the system.
They can be static `.a` or dynamic `.so`.
There are several tools to find where/whether a library is installed and what are its dependencies:
1. To shows files and directories related to a library, for example `liblapack-dev`

   ```bash
   dpkg -L liblapack-dev
   ```
2. To show which library contains a file, for example `liblapack.so`
   ```bash
   apt-file search liblapack.so
   ```
3. To show the libraries needed by a program, for example `wannier90.x`
   ```bash
   ldd path/to/wannier90.x
   ```

When **multiple libraries** are used to implement the same codes, it is also usefull to look at `update-alternatives`

```bash
update-alternatives --display mpirun
```
This shows all the **different implementations** of `mpirun` available in the system (most commonly `openmpi` and `mpich`) and their priority.

## NOTES

The tool `apt-file` does not come with default Ubuntu. One first has to install it and then update its cache
```bash
sudo apt install apt-file
sudo apt-file update
```
