#from cv_bridge import CvBridge
import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
import left 
import right
#bridge = CvBridge()
#image = bridge.imgmsg_to_cv2(Image, desired_encoding='passthrough')
#threshold
def main():
	img = cv2.imread('/home/dark_knight/image.png', cv2.IMREAD_GRAYSCALE)

	pnts = cv2.findNonZero(img)
	#min area rect
	rect_center, size,  angle = cv2.minAreaRect(pnts)

	#fit line to get angle
	[vx, vy, x, y] =cv2.fitLine(pnts, cv2.DIST_L12, 0, 0.01, 0.01)
	angle = (math.atan2(vy, -vx)) * 180 / math.pi

	M = cv2.moments(img)
	gravity_center = (M["m10"] / M["m00"], M["m01"] / M["m00"])

	angle_vec = (int(gravity_center[0] + 100 * vx), int(gravity_center[1] + 100 * vy))

	#cc_vec = gravity center - rect center
	cc_vec = (gravity_center[0] - rect_center[0], gravity_center[1] - rect_center[1])

	#if dot product is positive add 180 -> angle between [0, 360]
	dot_product = cc_vec[0] * angle_vec[0] + cc_vec[1] * angle_vec[1]
	angle += (dot_product > 0) * 180


	angle += (angle < 0) * 360


	#draw rect center
	cv2.circle(img, (int(rect_center[0]), int(rect_center[1])), 3, 128, -1)
	cv2.circle(img, (int(gravity_center[0]), int(gravity_center[1])), 3, 20, -1)

	if (angle >=100 and angle <=200):
		print("Go left")
		left.main()
		
	else:
		
		print("Go right")
		right.main1()
