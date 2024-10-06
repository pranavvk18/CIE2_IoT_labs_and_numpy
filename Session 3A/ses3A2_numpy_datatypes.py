# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 15:44:02 2021

@author: Mouli
"""

# To learn about datatypes in NumPy

# This file is to understand different  dtypes supported by NumPy

import numpy as np

npBool = np.bool_(True)
print('About dtype bool_')
print('Type: ', type(npBool))
print('Size: ', npBool.itemsize)
print('Value: ', npBool)

# It does not flag an error when more than a byte value is passed
# Check when 300 is passed to this
# When 300 is passed, it is in hex 0x12C, where 0x2C is 44 in decimal
npByte = np.byte(300) # It can only store an 8-bit value
print('\nAbout dtype byte')
print('Type: ', type(npByte))
print('Size: ', npByte.itemsize)
print('Value: ', npByte) 
print('min and max: ', np.iinfo(np.byte).min, np.iinfo(np.byte).max)

npUbyte = np.ubyte(0xFF) 
print('\nAbout dtype ubyte')
print('Type: ', type(npUbyte))
print('Size: ', npUbyte.itemsize)
print('Value: ', npUbyte) 
print('min and max: ', np.iinfo(np.ubyte).min, np.iinfo(np.ubyte).max)

npShort = np.short(0xFFFF)
print('\nAbout dtype short')
print('Type: ', type(npShort))
print('Size: ', npShort.itemsize)
print('Value: ', npShort)
print('min and max: ', np.iinfo(np.short).min, np.iinfo(np.short).max)

npUshort = np.ushort(0xFFFF)
print('\nAbout dtype ushort')
print('Type: ', type(npUshort))
print('Size: ', npUshort.itemsize)
print('Value: ', npUshort)
print('min and max: ', np.iinfo(np.ushort).min, np.iinfo(np.ushort).max)

npIntc = np.intc(-1) # a 32-bit value
print('\nAbout dtype intc')
print('Type: ', type(npIntc))
print('Size: ', npIntc.itemsize)
print('Value: ', npIntc)
print('min and max: ', np.iinfo(np.intc).min, np.iinfo(np.intc).max)

# 0xFFFFFFFF is the hex value who's decimal equivalent
# is 4294967295 or -1 can be given
#npUintc = np.uintc(4294967295) # a 32-bit value
#npUintc = np.uintc(-1) # a 32-bit value
npUintc = np.uintc(0xFFFFFFFF) # a 32-bit value
print('\nAbout dtype uintc')
print('Type: ', type(npUintc))
print('Size: ', npUintc.itemsize)
print('Value: ', npUintc)
print('min and max: ', np.iinfo(np.uintc).min, np.iinfo(np.uintc).max)

npInt_ = np.int_(-1) # a 32-bit value
print('\nAbout dtype int_')
print('Type: ', type(npInt_))
print('Size: ', npInt_.itemsize)
print('Value: ', npInt_)
print('min and max: ', np.iinfo(np.int_).min, np.iinfo(np.int_).max)

npLongLong = np.longlong(-1) # a 64-bit value
print('\nAbout dtype longlong')
print('Type: ', type(npLongLong))
print('Size: ', npLongLong.itemsize)
print('Value: ', npLongLong)
print('min and max: ', np.iinfo(np.longlong).min, np.iinfo(np.longlong).max)

npUlongLong = np.ulonglong(-1) # a 64-bit value
print('\nAbout dtype ulonglong')
print('Type: ', type(npUlongLong))
print('Size: ', npUlongLong.itemsize)
print('Value: ', npUlongLong)
print('min and max: ', np.iinfo(np.ulonglong).min, np.iinfo(np.ulonglong).max)

# Let us check floating point types now ...
npHalfFloat = np.half(-1) # a two bytes value
print('\nAbout dtype half')
print('Type: ', type(npHalfFloat))
print('Size: ', npHalfFloat.itemsize)
print('Value: ', npHalfFloat)
print('min and max: ', np.finfo(np.half).min, np.finfo(np.half).max)

# Whereas in Python float type is equivalent to double in C (64-bit)
npSingleFloat = np.single(-1) # a 4 bytes value
print('\nAbout dtype single')
print('Type: ', type(npSingleFloat))
print('Size: ', npSingleFloat.itemsize)
print('Value: ', npSingleFloat)
print('min and max: ', np.finfo(np.single).min, np.finfo(np.single).max)

npFloat_ = np.float_(-1) # an 8 bytes value
print('\nAbout dtype float_')
print('Type: ', type(npFloat_))
print('Size: ', npFloat_.itemsize)
print('Value: ', npFloat_)
print('min and max: ', np.finfo(np.float_).min, np.finfo(np.float_).max)

npLongFloat = np.longfloat(-1) # an 8 bytes value
print('\nAbout dtype longfloat')
print('Type: ', type(npLongFloat))
print('Size: ', npLongFloat.itemsize)
print('Value: ', npLongFloat)
print('min and max: ', np.finfo(np.longfloat).min, np.finfo(np.longfloat).max)

npCSingle = np.csingle(-1+2j) # two 4 bytes value
print('\nAbout dtype csingle')
print('Type: ', type(npCSingle))
print('Size: ', npCSingle.itemsize)
print('Values of real and imag: ', npCSingle.real, npCSingle.imag)
print('min and max: ', np.finfo(np.csingle).min, np.finfo(np.csingle).max)

npComplex_ = np.complex_(-1+2j) # two 8 bytes value
print('\nAbout dtype complex_')
print('Type: ', type(npComplex_))
print('Size: ', npComplex_.itemsize)
print('Values real, imag: ', npComplex_.real, npComplex_.imag)
print('min and max: ', np.finfo(np.complex_).min, np.finfo(np.complex_).max)

npClongfloat = np.clongfloat(-1+2j) # two 8 bytes value
print('\nAbout dtype clongfloat')
print('Type: ', type(npClongfloat))
print('Size: ', npClongfloat.itemsize)
print('Values real, imag: ', npClongfloat.real, npClongfloat.imag)
print('min and max: ', np.finfo(np.clongfloat).min, np.finfo(np.clongfloat).max)

# Pointers are of two types intp and uintp
npInt = np.int8(55)
npIntP = np.intp(npInt) # It points to the integer npInt
print('About intp pointer type')
print('\nType of npInt:', type(npInt))
print('Type:', type(npIntP))
print('Size:', npIntP.size)
print('nBytes:', npIntP.nbytes)
print(npInt)
print(npIntP)

npUint = np.uint8(-1)
npUintP = np.uintp(npUint) # It points to the  integer npUint
print('About uintp pointer type')
print('\nType of npUint:', type(npUint))
print('Type:', type(npUintP))
print('Size:', npUintP.size)
print('nBytes:', npUintP.nbytes)
print(npUint)
print(npUintP)

# Let us understand void which is a pointer to a chunck of memory
# An opaque sequence of bytes
npVoid = np.void(b'abcdefghi') # A pointer to a chunck memory of 5 bytes
print('\nType of npVoid:', type(npVoid))
print('About void pointer type')
print('Type:', type(npVoid))
print('Size:', npVoid.size)
print('nBytes:', npVoid.nbytes)
print(npVoid)





























































