from matplotlib import pyplot as plt
import numpy as np
import cv2

img = cv2.imread('bamel.jpg')

mask = np.zeros(img.shape[:2], np.uint8)
bgdModel = np.zeros((1,65), np.float64)
fgdModel = np.zeros((1,65), np.float64)
rect = (50, 50, 450, 290)

# Grabcut 
cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

r_channel, g_channel, b_channel = cv2.split(img) 
a_channel = np.where((mask==2)|(mask==0), 0, 255).astype('uint8')  

img_RGBA = cv2.merge((r_channel, g_channel, b_channel, a_channel))
cv2.imwrite("test.png", img_RGBA)

# Now for plot correct colors : 
img_BGRA = cv2.merge((b_channel, g_channel, r_channel, a_channel))

plt.imshow(img_BGRA), plt.colorbar(),plt.show()