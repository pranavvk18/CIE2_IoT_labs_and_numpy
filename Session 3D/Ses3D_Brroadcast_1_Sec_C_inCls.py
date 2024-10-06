# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 21:26:43 2024

@author: Mouli
"""

import numpy as np

# What is the shape of the array below?
arr = np.array([1, 2, 3])
print("1. arr shape ", arr.shape)
# Strides mean the number of bytes to skip along each axis to 
# access the next element
print("1. arr.strides: ", arr.strides)

# What is the shape of the array below?
arr = np.array([1.0, 2.0, 3.0, 4.0])
print("1. arr shape ", arr.shape)
# Strides mean the number of bytes to skip along each axis to 
# access the next element
print("1. arr.strides: ", arr.strides)

# What is the shape of the array below?
arr = np.array([[1, 2, 3]])
print("2. arr shape ", arr.shape)
print("2. arr.strides: ", arr.strides)

# What is the shape of the array below?
arr = np.array([[1, 2, 3, 4]])
print("2b. arr shape ", arr.shape)
print("2b. arr.strides: ", arr.strides)

# What is the shape of the array below?
arr = np.array([[[1, 2, 3]]])
print("3. arr shape ", arr.shape)
print("3. arr strides ", arr.strides)


# This is to understand broadcasting feature of NumPy
A = np.array([1.0, 2.0, 3.0])
B = np.array([4.0, 5.0, 6.0])
print(A * B)

# Create a 3x3 matrix
A3x3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("A3x3 ndim ", A3x3.ndim)
print("A3x3 shape ", A3x3.shape)
print("A3x3.strides: ", A3x3.strides)

# With broadcasting, no restriction that both vectors have to be of
# the same size. The missing entries are filled with the given value.
A = np.array([1.0, 2.0, 3.0])
B = np.array([2.0])
C = A * B
print("A shape ", A.shape)
print("B shape ", B.shape)
print("C shape ", C.shape)
print(C)

CNew = B * A
print(CNew)

# Create a 1D array (vector)
A = np.array([1.0, 2.0, 3.0])
B = np.array([[2, 2, 2], [3, 3, 3]])
print("A shape ", A.shape)
print("B shape ", B.shape)

# Try to find the shape of these arrays and the strides of each and 
# the result array
K = np.array([[1, 1], [2, 2]])
L = np.array([3, 3])
M = np.array([[4, 4], [5, 5], [6, 6]])
print("K shape ", K.shape)
print("L shape ", L.shape)
print("M shape ", M.shape)
print("K strides ", K.strides)
print("L strides ", L.strides)
print("M strides ", M.strides)

















