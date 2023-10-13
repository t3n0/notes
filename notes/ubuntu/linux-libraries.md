Libraries are a set of compiled code that can be used by various programs in the system.
They can be static `.a` or dynamic `.so`.
Three tools to find where/whether a library is installed:
1. `dkpg - L <libname>`, shows files and directories related to the library <libname>
2. `apt-file search <libfile>`, this shows which library contains the file <libfile>
3. `ldd <program>`, this shows all the library files the executable <program> depends on
4. use `synaptic`
