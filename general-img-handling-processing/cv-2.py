from PIL import Image
from matplotlib.pyplot import *
from numpy import *

# read image to array
im = Image.open('cuties.png').convert('L')
im.save('darkness.png')
img = array(Image.open('cuties.png'))

# plot the image using "imshow"
imshow(img)

# random points
x = [100,100,400,400]
y = [200,500,200,500]

# plot points with red star markers
plot(x,y,"r*")

# LINE plot connecting FIRST TWO POINTS
plot(x[:2],y[:2])

title('gay pokemon')
show()