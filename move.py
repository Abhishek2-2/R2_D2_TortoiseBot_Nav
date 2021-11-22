#!/usr/bin/env python
# license removed for brevity
import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def movebase_client():

    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    pose =  [0.532021522522,0.220669150352,0.711419279991,0.702767819452,0.517146468163,0.942510485649,0.999947166482,-0.0102793115013,0.0421818494797,0.811336994171,-0.72572896656,0.687980717096,-0.055070400238
,0.479306101799,0.999749784725,-0.0223689056983]
    for i in range(0,16,4):
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

if __name__ == '__main__':
    try:
        rospy.init_node('movebase_client_py')
        result = movebase_client()
        if result:
            rospy.loginfo("Goal execution done!")
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")




