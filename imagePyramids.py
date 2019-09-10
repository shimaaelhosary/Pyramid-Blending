import cv2
import numpy as np
from matplotlib.pyplot import imshow,subplot,imread
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
import scipy.ndimage as nd

#Pyramids Downsimple

img = imread('icon.jpg')
img = rgb2gray(img)
img = cv2.resize(img,(512,512))

simg = nd.gaussian_filter(img , 2)

outdown = []
outdown.append(img)
tmp = simg
for i in range(0,3):
    tmp = tmp[::2,::2]
    outdown.append(tmp)


#Pyramids Expand 
img = imread('C:\\Users\\Hassan\\Desktop\icon.jpg')
img = rgb2gray(img)
img = cv2.resize(img,(64,64))

outup = [img]
L = img
for i in range(0,3):
    L = cv2.pyrUp(L)
    outup.append(L)
"""
outimage = [img]
for i in range(0,3):
    L = np.zeros((img.shape[0]*2, img.shape[1]*2))
    L[::2,::2]=img[:,:]
    outimage.append(L)
    img = L
"""

#Laplacian Pyramid

lapyramid = [outdown[3]]
for i in range(3,0,-1):
    expand = cv2.pyrUp(outdown[i])
    L = cv2.subtract(outdown[i-1],expand)
    lapyramid.append(L)

#preview Images   
for i in range(1,5):
    subplot(3,4,i)
    imshow(outdown[i-1],cmap="gray")
    plt.xticks([]), plt.yticks([])
plt.title("Gaussian Pyramids(reduce)")
for i in range(5,9):
    subplot(3,4,i)
    imshow(outup[i-5],cmap="gray")
    plt.xticks([]), plt.yticks([])
plt.title("Gaussian Pyramids(expand)")
for i in range(9,13):
    subplot(3,4,i)
    imshow(lapyramid[i-9],cmap="gray")
    plt.xticks([]), plt.yticks([])
plt.title("Laplacian Pyramids")