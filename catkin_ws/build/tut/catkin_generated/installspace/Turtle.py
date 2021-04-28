#!/usr/bin/env python3
import math 
import rospy 
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

 

def callback1(data):
	global pose_1
	pose_1 = data 
  
def callback2(data):
	global pose_2
	pose_2 = data
	calc(pose_2)
               
def calc(pose_2):
	distance = math.sqrt( math.pow((pose_1.x - pose_2.x),2) + math.pow((pose_1.y -pose_2.y),2))
	print(distance)
	
	vel_msg.linear.x = pose_2.linear_velocity
	vel_msg.linear.y=0
	vel_msg.linear.z=0
	
	vel_msg.angular.x=0
	vel_msg.angular.y=0
	vel_msg.angular.z=0
	if( distance <= 2 ):
		vel_msg.linear.x = 0
		vel_msg.linear.y =2
		vel_msg.angular.y=1
	if(math.ceil(pose_2.x-pose_1.x) >= 2 ):
		vel_msg.linear.x = 0	
	
	pub.publish(vel_msg)
	
	
def Turtle_init():
	
	pose_1 = Pose()
	pose_2 = Pose()
	global vel_msg
	vel_msg = Twist()
	global pub
	pub=rospy.Publisher('/turtle2/cmd_vel',Twist , queue_size =10)
     
	rospy.init_node('Turtle',anonymous=True)
   
	
	rospy.Subscriber('/turtle1/pose', Pose, callback1)
	rospy.Subscriber('/turtle2/pose', Pose, callback2)
	
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		pub.publish(vel_msg)
		rate.sleep()
		rospy.spin()

 
if __name__ == '__main__':
     try:
         Turtle_init()
                 
     except rospy.ROSInterruptException:
         pass
