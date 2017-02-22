# computer vision 1
from PIL import Image

img = Image.open("dog.jpg.png").convert('L').rotate(45)
img.save("newdog2.jpg")