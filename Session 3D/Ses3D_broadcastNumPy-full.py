# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 17:04:44 2021

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

# What is the shape of the array below?
arr = np.array([[[1, 2, 3]]])
print("3. arr shape ", arr.shape)

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

# Create a 1D array (vector)
A = np.array([1.0, 2.0, 3.0])
B = np.array([[2, 2, 2], [3, 3, 3]])
print("A shape ", A.shape)
print("B shape ", B.shape)

# Broadcasting allows adding a 1D array to a 2D array
C = A + B
print("C shape ", C.shape)
print("C strides ", C.strides)
print(C)

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

# Can this operation be done? Will broadcasting work here?
#result = K + L + M

# How to make it work with one change either to K or M in its shape?
# Either make the shape K as (3, 2) or M as (2, 2)
# Let us try one at a time
# Change shape of K as (3, 2)
K = np.array([[1, 1], [2, 2], [3, 3]])
L = np.array([3, 3])
M = np.array([[4, 4], [5, 5], [6, 6]])
result = K + L + M
print("result shape ", result.shape)
print(result)


# From here, in the file Ses3D_Broadcast_2
# Broadcasting: Scaling an RGB array with a 1D array
colourPlanes = (8, 8, 3)
npImage = np.ones(colourPlanes)
print('\nInitalized Image:')
print('   R  G  B planes each of 8x8 npImage')
print(npImage)

# The last entry (3) refers to three colour planes RGB
# How can we access the Red plane which is 8x8?
# We can use slicing. Just mentioning : means all the elements of that axis
redPlane = npImage[:, :, 0] # Red plane
print('\nRed plane')
print(redPlane)

# Note that redPlane is a new object view of the same original npImage
# Any changes to the redPlane affects the original npImage
colourScale = np.array([2, 3, 4])
print('Colour scaling 1D array')
print(' R G B scaling factor 1x3 size')
print(colourScale)
scaledImage = npImage * colourScale
print('\nScaled Image:')
print('   R  G  B planes each of 8x8 size')
print(scaledImage)

# does scaledImage and npImage refer to the same memory?
print("id of npImage ", id(npImage))
print("id of scaledImage ", id(scaledImage))
# Note that element-wise operations in NumPy create new arrays, 
# rather than modifying the original array in place

# Let us use slicing to see different planes of the scaled image
redPlane = scaledImage[:, :, 0] # Red plane of scaled image
print('\nRed plane of scaled image')
print(redPlane)

# Note that slicing does not create a new copy, the redPlane is a 
# new view of the original scaledImage, though new object is created
# to refer to a new view of the original object
print("id of the scaledImage ", id(scaledImage))
print('id of redPlane before scaling', id(redPlane))

greenPlane = scaledImage[:, :, 1] # Green plane of scaled image
print('\nGreen plane of scaled image')
print(greenPlane)

bluePlane = scaledImage[:, :, 2] # Blue plane of scaled image
print('\nBlue plane of scaled image')
print(bluePlane)

# Let us see the shape of these colour planes
print('Shaeps of RGB planes are: ', redPlane.shape, 
      greenPlane.shape, bluePlane.shape)

# Let us scale up differnt colour components by different values
redScale = 10
greenScale = 20
blueScale = 30

# Scale down by dividing the Red plane with redScale
# Here, a new redPlane is created for the element-wise operation
redPlane = redPlane / redScale
print('id of redPlane after scaling', id(redPlane))

print('\nScaled down Red plane')
print(redPlane)

print('\n scaledImage is not affected now ...')
print(scaledImage)

redPlane = scaledImage[:, :, 0] # Red plane of scaled image
# The operator /= is in-place operator for mutable objects in Python
# It does not create a new object, the orginal scaledImage is modified.
redPlane /= redScale
print('\nScaled down Red plane now')
print(redPlane)

print('\n scaledImage is affected now with /= in-place operator ...')
print(scaledImage)

print('id of scaledImage before scaling', id(scaledImage))
# To apply the scaling on the original image itself
# Another method of performing an in-place operation is given below
scaledImage[:, :, 0] = scaledImage[:, :, 0] / redScale
print('id of scaledImage after scaling', id(scaledImage))

print('\n Affected scaled image after the scaling done on it...')
print(scaledImage)

# Some more Broadcasting examples
npA3 = np.arange(2, 5)
print("npA3: ", npA3)

npB5_4_3 = np.ones((5, 4, 3))
print("npB5_4_3:\n", npB5_4_3)

npNew5_4_3 = npB5_4_3 + npA3
print("npNew5_4_3:\n", npNew5_4_3)

npA2 = np.arange(2, 4)
print("npA2:", npA2)

# Is it possible to do this operation? 
# Uncomment and check it out.
#npNew = npNew5_4_3 + npA2

# Define A (4D array)
A = np.ones((8, 1, 6, 1))

# Define B (3D array)
B = np.ones((7, 1, 5))

# Perform broadcasting (e.g., addition)
result = A + B

print("Shape of A:", A.shape)


print("Shape of B:", B.shape)


print("Shape of result:", result.shape)
print("result:\n", result)







# Sample code explaining the slice and the original arrays
# referring to the same data in the memory

# Create a 2D NumPy array
original_arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Slice the array (create a view)
sliced_arr = original_arr[:, 1]

# Check the id of the original and sliced array
print("ID of original array:", id(original_arr))  # Different object
print("ID of sliced array:", id(sliced_arr))      # Different object

print("Original array contents:", original_arr)

print("Sliced array contents:", sliced_arr)


# Modify the sliced array
sliced_arr[0] = 100

# Check if the change is reflected in the original array
print("Original array after modifying the slice:")
print(original_arr)



















