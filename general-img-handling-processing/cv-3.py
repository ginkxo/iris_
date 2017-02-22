# numpy 

from PIL import Image
from matplotlib.pyplot import *
from numpy import *
import imtools as imt

""" Basic Numpy"""

# array in numpy - list but restricted to having same types
# type is autoset

"""
im = array(Image.open('cuties.png'))
print im.shape, im.dtype
"""

# output - (rows, columns, colour channels) datatype
# uint8 - unsigned 8 bit integers

# setting to floating point and grayscale:
# im = array(Image.open('cuties.png').convert('L'),'f')
	# note -- the 'f' converts to floating point, as "array" arg

# ACCESSING ELEMENTS OF ARRAY:
	# value = im[row i, column j, colour channel k]

# SLICING OF THIS ARRAY is used to ACCESS PIXEL VALUES

""" Graylevel transforms """

# We can perform mathematical operations on the arrays, e.g. graylevel transforms
# Graylevel transforms change the graylevels of an image
# f : [0,255] -> [0,255] or f : [0,1] -> [0,1] normalized (same sized range/domain)

"""
im = array(Image.open('cuties.png').convert('L'))

im2 = 255 - im # invert image
im3 = (100.0/255) * im + 100 # clamp to interval 100 ... 200
im4 = 255.0 * (im/255.0)**2 # squared 
"""

# im2 inverts the graylevels
# im3 clamps intensities/graylevels to between 100 and 200
# im4 applies a QUADRATIC FUNCTION which LOWERS VALUES OF DARKER PIXELS

"""
edited_im2 = Image.fromarray(uint8(im2))
edited_im2.save("inversion.png")

edited_im3 = Image.fromarray(uint8(im3))
edited_im3.save("clamping.png")

edited_im4 = Image.fromarray(uint8(im4))
edited_im4.save("dark-reduction.png")
"""

""" Image resizing """

# We add PIL's built in Image.resize() into a helper function in imtools.py

""" Histogram equalization """

# Consider the Graylevel histogram. Histogram equalization is "flattening" this.
# Makes ALL INTENSITIES EQUALLY COMMON -- good for NORMALIZING IMG INTENSITY

# transformation function is a CDF OF PIXEL VALUES, normalized

"""
img = array(Image.open('cuties.png').convert('L'))
img2, cdf = imt.histogram_equalize(img)

edited_im = Image.fromarray(uint8(img2))
edited_im.save("normalizing.png")
"""

""" Averaging images """

# Used for artistic effects often 
# We stick the compute average function in imtools.py

""" Principal Component Analysis of Images """

# Very useful for dimensionality reduction
# Represents variability of training data with as few dimensions as possible
	# uses orthogonal transformation (in lin alg) to convert possibly
	# correlated variables to LINEARLY UNCORRELATED VARIABLES using an
	# orthogonal transformation 

# Consider a 100 x 100 image. It also has 10000 dimensions, so exists in
# 10000 dimensional space. Megapixel images have millions of dimensions
# Thus, dimensionality reduction is important.

# Images need to be converted to 1D REPRESENTATION e.g. numpy.flatten()
# flattened images collected in a SINGLE MATRIX via STACKING THEM
# one row = one image
# next, rows are CENTERED relative to MEAN IMAGE prior to computation of
# dominant directions
# finding principal components typically involves SVD (singular value decomp.)
	# SVD is a type of matrix factorization (decomposition into products of matrices)
	# if high dimensionality, we can use a different trick instead of SVD

# coded in imtools

# test with http://webstaff.itn.liu.se/~marso/ , from which we get some images

# store the images in a file called imlist, then:

img = array(Image.open(imlist[0])) # opens one image so we can get size
m,n = im.shape[0:2] # size of each image
im_number = len(imlist) # number of images

# matrix to store all flattened images
im_matrix = array([array(Image.open(im)).flatten() for im in imlist], 'f')

# perform PCA
V,S,img_mean = imt.PCA(im_matrix)

# The images are stored in the array V. We just have to call V[i].reshape(m,n)

