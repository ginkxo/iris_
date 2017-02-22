from PIL import Image
from matplotlib.pyplot import *
from numpy import *

# read image to array
img = array(Image.open('puredogs.jpg').convert('L'))

# create new figure
figure()

# no colours
gray()

# show contours with origin upper left

contour(img, origin='image')
axis('equal')
axis('off')

title('gay pokemon but evil')

figure()
hist(img.flatten(),128)
show()