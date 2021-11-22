#!/usr/bin/env python
# license removed for brevity
import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def movebase_client_right():

    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    pose =  [-0.218210965395,0.525595188141,0.875154426459,0.483843703947,-0.354642629623
,0.975210368633,0.999998290358,0.00184912973434, -0.832944452763,0.979945123196,-0.710031731817,0.704169681123]


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

def main1():
    try:
        #rospy.init_node('movebase_client_py')
        result = movebase_client_right()
        if result:
            rospy.loginfo("Goal execution done!")
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")

