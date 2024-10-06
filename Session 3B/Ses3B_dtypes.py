# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 15:36:40 2021

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

for i in range(3):
    print('\nDetails of npObjArr[', i, ']', sep='')
    print('Type: ', type(npObjArr[i]))
    print('Value: ', npObjArr[i])

# About Overflows in NumPy which does not happen with Python ints
npPow64 = np.power(100, 8, dtype=np.int64)
print('\nAbout overflows in NumPy')
print('Value of 100^8 using int64', npPow64)
npPow32 = np.power(100, 8, dtype=np.int32)
print('Value of 100^8 using int32', npPow32)

# Incorrect even with 64-bit int, then float64 can be used instead
npPow64 = np.power(100, 100, dtype=np.int64) 
print('Value of 100^100 using npPow64', npPow64)
npPowF64 = np.power(100, 100, dtype=np.float64) 
print('Value of 100^100 using npPowF64', npPowF64)

# About byteorder
dt = np.dtype('i2') # An  integer with two bytes
print('Byte order of two bytes int is: ', dt.byteorder) # Native endianess
print('Item size is ', dt.itemsize)

# Learn about endiness of the machine this is running on
print('Endianess: ', np.dtype(np.uintc).byteorder)
print('Endianess: ', np.dtype(np.ubyte).byteorder)

print('System byteorder: ', sys.byteorder)

intNonNative = np.dtype(np.uintc).newbyteorder('S')
print(type(intNonNative))
print('Non-native byteorder is ', intNonNative.byteorder)
intNative = np.dtype(np.uintc).newbyteorder('S').newbyteorder('S')
print('Native byteorder is ', intNative.byteorder)






