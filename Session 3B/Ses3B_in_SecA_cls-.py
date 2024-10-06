# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 10:13:30 2024

@author: Mouli
"""
# This file is to understand more about object datatype supported by NumPy
import numpy as np
import sys
import platform

print('Python interpreter version running on Windows PE')
print(platform.architecture())

class X:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
      return 'I am am instance of class X\n'  + 'My name is ' + self.name

class Y:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
      return 'I am am instance of class Y\n'  + 'My name is ' + self.name

class Z:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
      return 'I am am instance of class Z\n'  + 'My name is ' + self.name

objX = X('ObjX')
objY = Y('ObjY')
objZ = Z('ObjZ')

print(objX)


npObjArr = np.ndarray(3, dtype=object)

npObjArr[0] = objX
npObjArr[1] = objY
npObjArr[2] = objZ

arr = np.array([0, 1, 2, 3])
print(arr)
print("id(arr) = ", id(arr))

# Individual elements of a NumPy array can be modified without changing its size
arr[0] = 10
print(arr)
print("id(arr) = ", id(arr))

# Adding a new element or changing the size of NumPy array creates a new array
arr = np.append(arr, 4)
print(arr)
print("id(arr) = ", id(arr))

# Let us understand the contents of different integer values in NumPy
npMyInt32 = np.int32(5)
print("value in npMyInt32 is ", npMyInt32)
print("Size of npMyInt32 is ", npMyInt32.nbytes)
print("Binary contents of npMyInt32 is ", npMyInt32.tobytes())

npMyInt64 = np.int64(-2)
print("value in npMyInt64 is ", npMyInt64)
print("Size of npMyInt64 is ", npMyInt64.nbytes)
print("Binary contents of npMyInt64 is ", npMyInt64.tobytes())















