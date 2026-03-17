## Quantum-Espresso

To install:
```
./configure
make all
```
To add the binaries system-wide, add `export "</path/to/qe-x.y/bin>:$PATH"` to .bashrc

To force a serial version installation:
```
./configure --disable-parallel
make all
```

Clean all files and configs:
```
make veryclean
```
