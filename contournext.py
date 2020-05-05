from PIL import Image
from pylab import *

# read image to array
im = array(Image.open('OpenPose_sample_image.png').convert('L'))

# create a new figure
figure()

# show contours with origin upper left corner
contour(im, origin='image')
axis('equal')

show()
