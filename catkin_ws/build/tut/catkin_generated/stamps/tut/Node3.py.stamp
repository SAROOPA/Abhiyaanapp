#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback1(data):
   global X 
   X=data.data
    
def callback2(data):
    print( X , data.data)
               

def Node3_sub():

    rospy.init_node('Node3',anonymous=True)
    rospy.Subscriber('/team_abhiyaan', String, callback1)
    rospy.Subscriber('/autonomy', String, callback2)
   
    rospy.spin()

if __name__ == '__main__':
    Node3_sub()
