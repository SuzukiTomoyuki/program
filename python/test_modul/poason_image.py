from numpy.random import *
import math
import cv2

if __name__ == '__main__':
	im = cv2.imread("test.jpg")
	height, width = im.shape[:2]
	w = 0
    for h in xrange(int(height)):
        while int(width) >= w:
            p_data = poisson(lam=2)
            w+=int(p_data)
            try: im[h,w] = [0,0,0]
            except: pass
        w = 0
	cv2.imshow("Show image",im)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
