#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def Node_pub():
    pub_1 = rospy.Publisher('/team_abhiyaan', String, queue_size=10)  
    rospy.init_node('Node1', anonymous=True) 
    rate = rospy.Rate(10) # 10hz
    
    pub_2 = rospy.Publisher('/autonomy', String, queue_size=10)  
    rospy.init_node('Node2', anonymous=True) 
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        str_1 = "Team Abhiyaan: %s" % rospy.get_time() 
        str_2 = "Fueled By Autonomy %s" % rospy.get_time() 
        rospy.loginfo(str_2) 
        rospy.loginfo(str_1) 
        pub_2.publish(str_2)   
        pub_1.publish(str_1) 
        rate.sleep()


if __name__ == '__main__':
    try:
        Node_pub()
    except rospy.ROSInterruptException:
        pass
