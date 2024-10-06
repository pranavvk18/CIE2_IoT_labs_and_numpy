# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 21:26:43 2024

@author: Mouli
"""

import numpy as np

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












