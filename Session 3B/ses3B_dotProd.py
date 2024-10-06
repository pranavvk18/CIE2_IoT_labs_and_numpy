# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 21:08:09 2021

@author: Mouli
"""

# All elements in Python array must be of same type
# Arrays are more memory-efficient than lists
import array as arr

import numpy as np
import time

# Performance measurements using two methods: 
# process_time_ns(): Only measures the process excution time 
# perf_counter_ns(): This much more granular and measure I/O wait time also
# which makes it perfect for overall performance measurements.

# Create a Python array of double presion 64 bit floating point type
# Array is created with the values from 0 to 99999

A = arr.array('d', range(100000)) 

B = arr.array('d', range(100000)) 

# classic dot product of vectors in Python
Dot = 0.0;

# Measure the start and end times in nano seconds.
#startTime = time.process_time_ns() 
startTime = time.perf_counter_ns() 

for i in range(len(A)): 
      Dot += A[i] * B[i]
      
endTime = time.perf_counter_ns() 

print('Dot product computed without NumPy: ', Dot)
print('Perf count in nsecs without NumPy: ', endTime-startTime)
pyPerfCount = endTime-startTime

print(type(endTime))

npA = np.array(A)
npB = np.array(B)

startTime = time.perf_counter_ns() 

# Using the same Python arrays A, B perform dot product using np funtion dot()
npDot = np.dot(npA, npB) # Here pointers to the arrays are passed

endTime = time.perf_counter_ns() 

print('Type of returned value from np.dot() is ', type(npDot))
print('Dot product computed with NumPy: ', npDot)
print('Perf count in nsecs with NumPy: ', endTime-startTime)
npPerfCount = endTime-startTime

print("Improvement in performance because of NumPy is ", 
        int(pyPerfCount/npPerfCount))

# If "out" default optional param is given then the result 
# is written into it as well as returned
npVal = np.array(0.0) # ndarray of np.float64 type
chkVal = np.dot(A, B, out=npVal)
print('type of npVal is ', type(npVal), ' and npVal = ', npVal)
print('Typeof chkVal is ', type(chkVal), ' and chkVal is ', chkVal)

# Element-wise multiplication of matrix is given as A*B in NumPy
npA = np.array([1, 2, 3])
npB = np.array([2, 2, 2])

eleMult = npA * npB
print('eleMult is: ', eleMult)

# Dot product can also be done using the operator @
dotProduct = npA @ npB
print('dotProduct is: ', dotProduct)

# If the input matrix are 2D or more
A = np.array([[1, 1], 
              [2, 2]])
B = np.array([[3, 5], 
              [4, 6]])
npDot = np.dot(A, B)
print(npDot)

npDot = A @ B
print(npDot)


