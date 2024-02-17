# Multithreading with python and cython: `openMP`

It is known that python cannot run multiple threads in parallel due to the GIL: Global Interpreter Lock (for example, see [this](http://dabeaz.blogspot.com/2010/01/python-gil-visualized.html) and [this](https://www.scaler.com/topics/gil-in-python/)).  
A way around that is provoded by cython and the `openMP` library.

