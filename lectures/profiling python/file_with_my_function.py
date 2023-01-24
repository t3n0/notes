
import numpy as np

def psi(x):
    y = np.exp(-x**2)
    A = np.trapz(y**2, x)
    y /= np.sqrt(A)
    return y
