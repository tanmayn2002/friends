#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

rospy.init_node('star')
rospy.loginfo("Started...")
pub = rospy.Publisher("turtle1/cmd_vel", Twist, queue_size=1)
rate = rospy.Rate(2)

while not rospy.is_shutdown():
    # Move forward for 2 seconds
    msg = Twist()
    msg.linear.x = 2.0
    msg.angular.z = 0.0
    pub.publish(msg)
    rospy.sleep(2.0)

    # Rotate 144 degrees (2 * pi / 5) for 1 second
    msg = Twist()
    msg.linear.x = 0.0
    msg.angular.z = 2.0
    pub.publish(msg)
    rospy.sleep(1.0)
