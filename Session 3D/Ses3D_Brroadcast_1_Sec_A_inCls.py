# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 12:48:34 2024

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
arr = np.array([[1, 2, 3]])
print("2. arr shape ", arr.shape)
print("2. arr strides ", arr.strides)

arr = np.array([[1, 2, 3, 4]])
print("3. arr shape ", arr.shape)
print("3. arr strides ", arr.strides)

# What is the shape of the array below?
arr = np.array([[[1, 2, 3]]])
print("4. arr ndim ", arr.ndim)
print("4. arr shape ", arr.shape)
print("4. arr strides ", arr.strides)


# What is the shape of the array below?
arr = np.array([[[1.0, 2.0, 3.0, 4.0]]])
print("4. arr ndim ", arr.ndim)
print("4. arr shape ", arr.shape)
print("4. arr strides ", arr.strides)



























