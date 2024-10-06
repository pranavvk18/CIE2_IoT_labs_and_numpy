# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 10:38:58 2024

@author: Mouli
"""
import numpy as np

a = np.array([0, 1, 2, 3])
print(a)

b = np.array([[0, 1, 2], [3, 4, 5]])    # 2 x 3 array
print(b)

print(b.shape)
print(b.ndim)
print(b[0])
print(b[1])


a = np.arange(10) # 0 .. n-1  (!)
print(a)

aFloat = np.array([1, 2, 3], dtype=float)
print(aFloat)

aComplex = np.array([1+2j, 3+4j, 5+6*1j])
print(aComplex)
print(aComplex.dtype)














