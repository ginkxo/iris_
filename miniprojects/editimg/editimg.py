from PIL import Image
from numpy import *
from scipy.ndimage import filters

from sys import argv

def gray(filename, savename):
	im = Image.open(filename).convert('L')
	im.save(savename)

def blur(filename, value, savename):
	im = array(Image.open(filename))
	convolve_target = zeros(im.shape)

	for i in range(3):
		convolve_target[:,:,i] = filters.gaussian_filter(im[:,:,i],value)

	conv_uint8 = array(convolve_target, 'uint8')

	blurred_im = Image.fromarray(conv_uint8)
	blurred_im.save(savename)


def rotate(filename, value, savename):
	im = Image.open(filename).rotate(value)
	im.save(savename)

if __name__ == "__main__":

	input_image = argv[1]
	function_choice = argv[2]
	choice_value = int(argv[3])
	output_name = argv[4]

	if function_choice == "blur":
		blur(input_image, choice_value, output_name)
	elif function_choice == "gray":
		gray(input_image, output_name)
	elif function_choice == "rotate":
		rotate(input_image, choice_value, output_name)
	else:
		print "USAGE: editimg.py <input img> <blur, gray, convert> <value> <output img>"


