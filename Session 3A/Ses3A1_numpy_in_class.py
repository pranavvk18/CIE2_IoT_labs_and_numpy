# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 10:19:14 2024

@author: Mouli
"""
import numpy as np

A = [1, 2, 3, 4.0]
print(A)

npA = np.array(A)
print(npA)

print('Type of npA is ', type(npA))

print("Dimension of npA is ", npA.ndim)

# It returns a tuple with ints giving the no. of element in each dimension
print("Shape of nPA is ", npA.shape)

print("Size of npA ", npA.size)

print("Data type of elements in npA ", npA.dtype)

print("Memory size of each element in npA ", npA.itemsize)

print("Total size of npA in bytes is ", npA.size * npA.itemsize)

A2_3 = [[1, 2, 3], [4, 5, 6]]
print(A2_3)

npA2_3 = np.array(A2_3)
print(npA2_3)

npA = np.append(npA2_3, [7, 8, 9])
print(npA)


npA3_3 = np.append(npA2_3, [[7, 8, 9]], axis=0)
print(npA3_3)

A2_x = [[1, 2, 3], [4, 5]]

print(A2_x)

npA2_x = np.array(A2_x, dtype=object)
print(A2_x)

























