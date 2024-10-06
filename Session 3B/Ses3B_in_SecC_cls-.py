# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 10:15:13 2024

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

npObjX = np.object_(objX)
print('\nAbout dtype object')
print('Type: ', type(npObjX))
print('Value: ', npObjX)

npObjArr = np.ndarray(3, dtype=object)

npObjArr[0] = objX
npObjArr[1] = objY
npObjArr[2] = objZ

print('\nAbout NumPy array of objects')
print('Item size of objXArr is ', npObjArr.itemsize)
print('Number of elements in the npObjXArr is ', npObjArr.size)
print('Total size in bytes, taken by npObjXArr is ', 
      npObjArr.size * npObjArr.itemsize)

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

# Different values of the byteorder attribute of NumPy
# byteorder is an attribute of NumPy arrays (ndarray) and data types (dtype)
# ‘=’ : native
# ‘<’ : little-endian
# ‘>’ : big-endian
# ‘|’   : not applicable

# Is endianess relevant for a byte value?
print("Endianess of a byte: ", np.dtype('i1').byteorder)

# Is endianess relevant for a byte value?
print("Endianess of a short or int16: ", np.dtype('i2').byteorder)

# Change the byteorder of the NumPy variable (in-place is not allowed)
npMyInt32 = np.int32(5)
npMyInt32New = npMyInt32.byteswap()
print("Value in npMyInt32New is ", npMyInt32New)
print("Value in npMyInt32New in hex is ", hex(npMyInt32New))

print("Swapped byte contents of npMyInt32New: ", npMyInt32New.tobytes())










