<div align="center">

# Pyramid Blending
</div>
### 
Merge	two	images	without	visible	seams	

here are the functions in the code and explanation:

1. Reduce: This function takes an image and out put it’s quarter size by dividing the height and width by two.

1. Expand: This function takes an image and out put it’s four times size by doubling the height and width by two.

1. Gaussian Pyramid: This function takes an image as an input and builds its pyramid and return the result as an array. The first member of the array is the original image and other members of the array are reduced form of the previous member.

1. Laplacian Pyramid: This function takes a gaussian pyramid array from the previous function, and return an array containing laplacian pyramid.

1. Blend: This function takes three arrays of laplacian pyramid two images and a gaussian pyramid of a mask image, then it performs blending of the two laplacian pyramids using mask pyramid weights.

1. Collapse: This function accepts a laplacian pyramid, then it takes the top layer, expand it, and then add it to the next layer this process continues until a single image remain and this will be returned as a result.


# screenshot

![](https://github.com/shimaaelhosary/Pyramid-Blending/blob/master/result/Capture.PNG)
