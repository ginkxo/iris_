import os
from PIL import Image
from matplotlib.pyplot import *
from numpy import *


def get_imlist(path):
	return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]

def image_resize(im, size):
	""" Resizes image array via PIL """
	PIL_image = Image.fromarray(uint8(im))
	return array(PIL_image.resize(size))

def histogram_equalize(im, number_of_bins=256):
	""" Histogram equalization of grayscale img"""

	# histogram of image
	imhist, bins = histogram(im.flatten(),number_of_bins,normed=True)
	# cdf & normalize the cdf
	cdf = imhist.cumsum() 
	cdf = 255 * cdf / cdf[-1]

	# linear interpolation of cdf to get new pixel vals
	# linear interpolation is a curve fitting method that uses existing
	# data points and linearly interpolates between them to construct
	# new data points
	# the linear interpolants are the "lines" between data points
	im2 = interp(im.flatten(),bins[:-1],cdf)
		# numpy.interp is 1D linear interpolation of an array-like
		# im.flatten() -> 1D array with row-wise values ; x coords of interpol. values
		# bins[:-1] -> x coordinates of data points
		# cdf -> y coords of data points
	return im2.reshape(im.shape), cdf

def compute_avg(img_list):
	""" Computes average of list of images

		Precond: all images have same size """

	# open first image, make into array of floats
	average_img = array(Image.open(img_list[0]), 'f')

	for img_name in img_list[1:]:
		try:
			average_img += array(Image.open(img_name))
		except:
			print img_name + ' was skipped!'
	average_img /= len(img_list)

	return array(average_img, 'uint8')

def PCA(X):
	""" 
	Principal Component Analysis

			input! X -> matrix with training data, flattened arrays in rows
			output! -> PROJECTION MATRIX (important dimensions FIRST), 
			VARIANCE, MEAN.
	"""

	# get dims 
	num_data, dim = X.shape

	# center data
	mean_X = X.mean(axis=0)
	X = X - mean_X

	if dim>num_data:
		# PCA COMPACTNESS trick
		M = dot(X,X.T) # covariance matrix
		e, EV = linalg.eigh(M) # eigenvalues, eigenvectors
		tmp = dot(X.T, EV).T # COMPACTNESS TRICK
		V = tmp[::-1] # reverse, because we want the LAST eigenvectors
		S = sqrt(e)[::-1] # reverse, since eigenvalues are in INCREASING order

		for i in range(V.shape[1]):
			V[:,i] /= S

	else:

		# PCA Singular Value Decomposition used
		U,S,V = linalg.svd(X)
		V = V[:num_data] # only return first num_data

	# return projection matrix, variance, mean

	return V, S, mean_X