#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def Node1_pub():
    pub = rospy.Publisher('/team_abhiyaan', String, queue_size=10)  
    rospy.init_node('Node1', anonymous=True) 
    rate = rospy.Rate(4) 
    while not rospy.is_shutdown():
        str_1 = "Team Abhiyaan: " 
        print(str_1)
        pub.publish(str_1)
        rate.sleep()


if __name__ == '__main__':
    try:
        Node1_pub()
    except rospy.ROSInterruptException:
        pass
