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

'''Grayscale blurring'''
image_to_convolve = array(Image.open('cuties.png').convert('L')) 
# opens image as converted grayscale, stores in array

im2 = filters.gaussian_filter(image_to_convolve, 5)
# in im2, stores the results of blurring the image in im2
# standard deviation is 5

'''TODO'''
# will try and save this image and see what it looks like
# plan: blurred_im = Image.fromarray(im2) and then blurred_im.save("blurred")

blurred_im = Image.fromarray(im2)
blurred_im.save("blurred.jpg")

'''Colour blurring'''

colour_im = array(Image.open('puredogs.jpg'))
colour_im_2 = zeros(colour_im.shape)
# the below code convolves each Gaussian channel
for i in range(3):
	colour_im_2[:,:,i] = filters.gaussian_filter(colour_im[:,:,i],5)

colour_im_2 = array(colour_im_2,'uint8')

blurred_colour = Image.fromarray(colour_im_2)
blurred_colour.save("blurredcolo.jpg")

# note: in all of these cases,
# we apply the filter on the original image and store it

'''Image Derivatives'''

# will continue afterward