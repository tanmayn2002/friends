#!/usr/bin/env python3 
import rospy
from std_msgs.msg import String
if __name__ == "__main__":
	rospy.init_node("pub", anonymous=True)
	pub1 = rospy.Publisher("lab", String, queue_size=10)
	r = rospy.Rate(1)
	counter = 0
	while not rospy.is_shutdown():
		hello_msg = "Hello World %d" % counter
		pub1.publish(hello_msg)
		r.sleep()
