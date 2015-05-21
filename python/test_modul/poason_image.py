from numpy.random import *
import math
import cv2

if __name__ == '__main__':
	im = cv2.imread("test.jpg")
	height, width = im.shape[:2]
	for h in xrange(int(height)):
		for w in xrange(int(width)):
			p_data = poisson(lam=2)
			if p_data > math.sqrt(p_data):
				im[h,w] = [0,0,0]
	cv2.imshow("Show image",im)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
