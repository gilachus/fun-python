import numpy as np
from PIL import Image

width, height = 600, 800
# create blank image
img = np.zeros((height, width, 3), dtype=np.uint8)

# draw background
img[:] = (35, 29, 43)
img[int(height*0.85):height, 0:width] = (35, 55, 43)

# draw building
img[int(height*0.1):int(height*0.9), int(width*0.2):int(width*0.8)] = (94, 101, 107)

# office windows logic
for row in range(6):
    for column in range(5):
        # select random window colours
        if np.random.randint(0,8) == 5:
            window_colour = (240, 230, 140)
        else:
            window_colour = (28, 23, 35)
        # draw windows
        img[
            int(height*0.1 + 100*row + 20):int(height*0.1 + 100*row + 60 + 20),
            int(width*0.2 + 75*column + 15): int(width*0.2 + 75*column + 30 + 15)
            ] = window_colour

# save image
Image.fromarray(img).save("my_img.png")