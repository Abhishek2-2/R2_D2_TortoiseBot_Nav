#!/usr/bin/env python
# license removed for brevity
import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def movebase_client_left():

    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    pose =  [-0.448777794838,0.0338809490204,0.996909810221,-0.078554632493,-0.611010432243,-0.00167399644852,0.998847303238,0.0480006751341,-0.729749500751,-0.00228276848793,0.999902802484,-0.0139422230604]
    for i in range(0,12,4):
    	goal.target_pose.pose.position.x = pose[i]
	print(pose[i])
    	goal.target_pose.pose.position.y = pose[i+1]
	print(pose[i+1])
	goal.target_pose.pose.orientation.z = pose[i+2]
	print(pose[i+2])
    	goal.target_pose.pose.orientation.w = pose[i+3]
	print(pose[i+3])

    	client.send_goal(goal)
    	wait = client.wait_for_result()
    if not wait:
        	rospy.logerr("Action server not available!")
        	rospy.signal_shutdown("Action server not available!")
    else:
        return client.get_result()

def main():
    try:
        #rospy.init_node('movebase_client_left_py')
        result = movebase_client_left()
        if result:
            rospy.loginfo("Goal execution done!")
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")

