from PIL import Image
from numpy import *
from scipy.ndimage import filters

from sys import argv

''' iteration 1 '''

image_name = argv[1]
saved_name = argv[2]
blur_val = int(argv[3])

colour_im = array(Image.open(image_name))
zeros_im = zeros(colour_im.shape)

for i in range(3):
	zeros_im[:,:,i] = filters.gaussian_filter(colour_im[:,:,i], blur_val)

output_im = array(zeros_im, 'uint8')

blurred_out = Image.fromarray(output_im)
blurred_out.save(saved_name)

