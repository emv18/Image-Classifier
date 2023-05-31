# Load basic libraries.
from skimage.io import imread, imshow
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import copy, math


folder_path = './Images/All Dogs/'
image_list = []
image_index = 1

while True:
    image_path = os.path.join(folder_path, f'perro{image_index}.jpg')
    
    if not os.path.isfile(image_path):
        break
    
    image = imread(image_path)
    image_list.append(image)
    
    image_index += 1

# Load and show an image
#image = imread('./images/perro1.jpg')
#imshow(image)

# Check the image shape 
image_shape= image.shape
'''
print("IMAGE SHAPE: ")
print(image_shape)
print('')

#print("IMAGE SHAPE: " + image.shape) 
# Watch the content of the image in grayscale
print("IMAGE:")
print(image)
print("")
'''

size = image.shape[0]*image.shape[1]

# ----------------------------------------- FEATURES AS VECTORS --------------------------------------------------
# Red channel values Feature
feature1_reds = image[:,:,0].ravel() #We get the red value of the rgb and save it in a 1D array
'''
print("REDS: ")
print(feature1_reds)
print('')
'''
# Red channel values Feature
'''
fig, ax = plt.subplots(figsize=(6,3))
ax.hist(feature1_reds, bins=256, range=(0, 256))
ax.set_title('Red Channel Histogram')
ax.set_xlabel('Pixels')
ax.set_ylabel('Red Value')
plt.show()
'''


# Green channel values Feature
feature2_greens = image[:,:,1].ravel() #We get the green value of the rgb and save it in a 1D array
'''
print("GREENS: ")
print(feature2_greens)
print('')
'''
# Green channel values Feature
'''
fig, ax = plt.subplots(figsize=(6,3))
ax.hist(feature2_greens, bins=256, range=(0, 256))
ax.set_title('Green Channel Histogram')
ax.set_xlabel('Pixels')
ax.set_ylabel('Green Value')
plt.show()
'''

# Blue channel values Feature
feature3_blues = image[:,:,2].ravel() #We get the green value of the rgb and save it in a 1D array
'''
print("BLUES: ")
print(feature3_blues)
print('')
'''
# Blue channel values Feature
'''
fig, ax = plt.subplots(figsize=(6,3))
ax.hist(feature3_blues, bins=256, range=(0, 256))
ax.set_title('Blue Channel Histogram')
ax.set_xlabel('Pixels')
ax.set_ylabel('Blue Value')
plt.show()
'''

#Whites Feature
feature4_whites = image[((image[:,:,0] >= 230) & (image[:,:,1] >= 230) & (image[:,:,2] >= 230)) 
                     & ((image[:,:,0] <= 250) & (image[:,:,1] <= 250) & (image[:,:,2] <= 250))]
'''
print("WHITES: ")
print(feature4_whites)
print('')
'''
# White channel values Feature
'''
fig, ax = plt.subplots(figsize=(6,3))
ax.hist(feature4_whites, bins=256, range=(0, 256))
ax.set_title('White Channel Histogram')
ax.set_xlabel('Pixels')
ax.set_ylabel('White Value')
plt.show()
'''

#Blacks Feature
feature5_blacks = image[((image[:,:,0] >= 0) & (image[:,:,1] >= 0) & (image[:,:,2] >= 0)) 
                     & ((image[:,:,0] <= 30) & (image[:,:,1] <= 30) & (image[:,:,2] <= 30))]
'''
print("BLACKS: ")
print(feature5_blacks)
print('')
'''
# Black channel values Feature
'''
fig, ax = plt.subplots(figsize=(6,3))
ax.hist(feature5_blacks, bins=256, range=(0, 256))
ax.set_title('Black Channel Histogram')
ax.set_xlabel('Pixels')
ax.set_ylabel('Black Value')
plt.show()
'''

#Browns Feature
feature6_browns = image[((image[:,:,0] >= 20) & (image[:,:,1] >= 50) & (image[:,:,2] >= 90)) 
                     & ((image[:,:,0] <= 220) & (image[:,:,1] <= 190) & (image[:,:,2] <= 140))]
'''
print("BROWNS: ")
print(feature6_browns)
print('')
'''
# Brown channel values Feature
'''
fig, ax = plt.subplots(figsize=(6,3))
ax.hist(feature6_browns, bins=256, range=(0, 256))
ax.set_title('Brown Channel Histogram')
ax.set_xlabel('Pixels')
ax.set_ylabel('Brown Value')
plt.show()
'''
#print(feature.shape) 
#print(feature)

# ----------------------------------------- FEATURES AS MATRIX --------------------------------------------------
features= [feature1_reds, feature2_greens, feature3_blues, feature4_whites, feature5_blacks, feature6_browns]
x_train = np.array(features)
print(x_train)