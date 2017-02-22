from PIL import Image
from imtools import *
from numpy import *
from scipy.ndimage import filters

'''Blurring Images'''

'''
The idea here is a CONVOLUTION of image I and a GAUSSIAN KERNEL.
The result is a BLURRED IMAGE.

	I_sigma = I * G_sigma

where the * denotes convolving. Recall that in this context, 
"convolving" is an action done for matrix values. (see wiki)
'''

image_to_convolve = array(Image.open('cuties.jpg').convert('L')) 
# opens image as converted grayscale, stores in array

im2 = filters.gaussian_filter(im, 5)
# in im2, stores the results of blurring the image in im2
# standard deviation is 5

'''TODO'''
# will try and save this image and see what it looks like
# plan: blurred_im = Image.fromarray(im2) and then blurred_im.save("blurred")

