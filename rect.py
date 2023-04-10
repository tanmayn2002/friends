#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

def draw_rectangle():
	rospy.init_node('turtle_rectangle')
	pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
	rate = rospy.Rate(1) # set the rate to 1 Hz

# wait for the TurtleSim to start up
	rospy.sleep(1)

# move the turtle in a rectangular path
	for i in range(4):
		move_forward(pub, 2.0)
		turn_left(pub)
	rospy.spin()

def pose_callback(pose):
	rospy.loginfo("Turtle position: x=%0.2f, y=%0.2f", pose.x, pose.y)

def move_forward(pub, distance):
	vel_msg = Twist()
	vel_msg.linear.x = 2.0
	vel_msg.linear.y = 0.0
	vel_msg.linear.z = 0.0
	vel_msg.angular.x = 0.0
	vel_msg.angular.y = 0.0
	vel_msg.angular.z = 0.0
	t0 = rospy.Time.now().to_sec()
	current_distance = 0
	while current_distance < distance:
		pub.publish(vel_msg)
		t1 = rospy.Time.now().to_sec()
		current_distance = 2.0 * (t1 - t0)
	vel_msg.linear.x = 0.0
	pub.publish(vel_msg)

def turn_left(pub):
	vel_msg = Twist()
	vel_msg.linear.x = 0.0
	vel_msg.linear.y = 0.0
	vel_msg.linear.z = 0.0
	vel_msg.angular.x = 0.0
	vel_msg.angular.y = 0.0
	vel_msg.angular.z = 1.8
	t0 = rospy.Time.now().to_sec()
	current_angle = 0
	while current_angle < 1.5708:
		pub.publish(vel_msg)
		t1 = rospy.Time.now().to_sec()
		current_angle = 1.8 * (t1 - t0)
	vel_msg.angular.z = 0.0
	pub.publish(vel_msg)

if __name__ == '__main__':
	draw_rectangle()
    
