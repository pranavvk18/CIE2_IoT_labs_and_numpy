# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 20:20:53 2024

@author: Mouli
"""

# Session 3B about endianess

import numpy as np
import sys

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

print("Can you understand the byte contents?")
print("What is the endinaness of the machine this is running on?")

# Get the byte order (endianess of the machine)
# Ref: https://numpy.org/doc/stable/reference/generated/numpy.dtype.byteorder.html

# Get the endianess of the system
print(sys.byteorder)

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

npMyInt32 = np.int32(8)

print("Value in npMyInt32 is ", npMyInt32)
print("Value in npMyInt32 in hex is ", hex(npMyInt32))

print("Endianess or byteorder of npMyInt32 is ", npMyInt32.dtype.byteorder)
print("Print the byte contents of npMyInt32: ", npMyInt32.tobytes())

# Change the byteorder of the NumPy variable (in-place is not allowed)
npMyInt32New = npMyInt32.byteswap()
print("Value in npMyInt32New is ", npMyInt32New)
print("Value in npMyInt32New in hex is ", hex(npMyInt32New))

print("Swapped byte contents of npMyInt32New: ", npMyInt32New.tobytes())

# Byteswap in-place is not allowed on a scalar value in NumPy
#npMyInt32.byteswap(inplace=True)

intNonNative = np.dtype(np.uintc).newbyteorder('S')
print('Non-native byteorder is ', intNonNative.byteorder)
intNative = np.dtype(np.uintc).newbyteorder('S').newbyteorder('S')
print('Native byteorder is ', intNative.byteorder)









