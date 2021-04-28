#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def Node2_pub():
    pub2 = rospy.Publisher('/autonomy', String, queue_size=10)  
    rospy.init_node('Node2', anonymous=True) 
    rate = rospy.Rate(4) 
    while not rospy.is_shutdown():
        str_2 = "Fueled By Autonomy " 
        print(str_2) 
        pub2.publish(str_2)
        rate.sleep()


if __name__ == '__main__':
    try:
        Node2_pub()
    except rospy.ROSInterruptException:
        pass
