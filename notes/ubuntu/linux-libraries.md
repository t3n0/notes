Libraries are a set of compiled code that can be used by various programs in the system.
They can be static `.a` or dynamic `.so`.
There are several tools to find where/whether a library is installed and what are its dependencies:
1. To shows files and directories related to a library, for example `liblapack-dev`

   ```bash
   dkpg - L liblapack-dev
   ```
3. To show which library contains a file, for example `liblapack.so`
   ```bash
   apt-file search liblapack.so
   ```
4. To show the libraries needed by a program, for example `wannier90.x`
   ```bash
   ldd wannier90.x
   ```


## NOTES

The tool `apt-file` does not come with default Ubuntu. One first has to install it and then update its cache
```bash
sudo apt install apt-file
sudo apt-file update
```
