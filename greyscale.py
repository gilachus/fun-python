import numpy as np
import cv2

width, height = 800, 800
# create blank image
img = np.zeros((height, width))

# initiallize parameters at 0
location = 0
shade = 0
# select number of shades
n_shades = 50
for i in range(n_shades):
    img[0:height, location:location + width//n_shades] = shade
    # increment location and shade
    location += width//n_shades
    shade += 255//n_shades

# save image
cv2.imwrite("my_img.png", img)