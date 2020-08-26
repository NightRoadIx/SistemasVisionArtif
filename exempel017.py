import cv2
import numpy as np
#from matplotlib import pyplot as plt

img = cv2.imread('bamel.jpg',0)
# Umbralización
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

cv2.imshow('original', img)
cv2.imshow('tres1', thresh1)
cv2.imshow('tres2', thresh2)
cv2.imshow('tres3', thresh3)
cv2.imshow('tres4', thresh4)
cv2.imshow('tres5', thresh5)

k = cv2.waitKey()

cv2.destroyAllWindows()

'''
titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in xrange(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
'''