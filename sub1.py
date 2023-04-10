#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
def msgCallBack(data):
	rospy.loginfo("I heard %s", data.data)
if __name__ == "__main__":
	rospy.init_node("sub1", anonymous=True)
	sub = rospy.Subscriber("lab", String, msgCallBack)
	rospy.spin()
