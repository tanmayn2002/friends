#!/usr/bin/env python3
from geometry_msgs.msg import Twist
import rospy

rospy.init_node('circle')
rospy.loginfo("started...")
pub=rospy.Publisher("turtle1/cmd_vel",Twist,queue_size=10)
rate=rospy.Rate(2)
while not rospy.is_shutdown():
	msg=Twist()
	msg.linear.y=2.0
	msg.angular.z=1.0
	pub.publish(msg)
	rospy.sleep(2.0)
	
