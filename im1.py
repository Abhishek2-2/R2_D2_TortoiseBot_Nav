#!/usr/bin/env python3

import roslib
import image
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
a=1
def callback(data):
	global a
	try:
		bridge = CvBridge()
		cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
	except CvBridgeError as e:
		print(e)
	cv2.imshow('hi',cv_image)
	cv2.waitKey(1)
	while a==1:
		cv2.imwrite('image.png',cv_image)
		a=0
		print('image saved')
		image.main()
		break
	
	
	cv2.destroyAllWindows()	

rospy.init_node('listener', anonymous=True)
rospy.Subscriber("camera/image_raw",Image,callback)
rospy.spin()


