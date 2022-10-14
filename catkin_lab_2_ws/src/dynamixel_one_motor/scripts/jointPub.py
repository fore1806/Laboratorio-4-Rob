import rospy
import numpy as np
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint


#posturas
q0= [0,0,0,0,0]
q1=np.multiply([-20,20,-20,20,0],np.pi/180)
q2=np.multiply([30,-30,30,-30,0],np.pi/180)
q3=np.multiply([-90,15,-55,17,0],np.pi/180)
q4=np.multiply([-90,45,-55,45,10],np.pi/180)
q5= np.multiply([0,-110,90,5,0],np.pi/180)

q = q0

def joint_publisher():
    pub = rospy.Publisher('/joint_trajectory', JointTrajectory, queue_size=0)
    rospy.init_node('joint_publisher', anonymous=False)
    
    while not rospy.is_shutdown():
        
        #Se controla la postura deseada;
        key=input()
        if key == 'z' or key == 'Z':
            q=q0
            key = ' '
        elif key == 'x' or key == 'X':
            q=q1
            key = ' '
        elif key == 'c' or key == 'C':
            q=q2
            key = ' '
        elif key == 'v' or key == 'V':
            q=q3
            key = ' '
        elif key == 'b' or key == 'B':
            q=q4
            key = ' '
        elif key == 'n' or key == 'N':
            q=q5
            key = ' '

        state = JointTrajectory()
        state.header.stamp = rospy.Time.now()
        state.joint_names = ["joint_1"]
        point = JointTrajectoryPoint()
        point.positions = q
        point.time_from_start = rospy.Duration(1)
        state.points.append(point)
        pub.publish(state)
        print('published command')
        rospy.sleep(1)



        state = JointTrajectory()
        state.header.stamp = rospy.Time.now()
        state.joint_names = ["joint_1","joint_2"]
        point = JointTrajectoryPoint()
        point.positions = q
        point.time_from_start = rospy.Duration(1)
        state.points.append(point)
        pub.publish(state)
        print('published command')
        rospy.sleep(1)


        state = JointTrajectory()
        state.header.stamp = rospy.Time.now()
        state.joint_names = ["joint_1","joint_2","joint_3"]
        point = JointTrajectoryPoint()
        point.positions = q
        point.time_from_start = rospy.Duration(1)
        state.points.append(point)
        pub.publish(state)
        print('published command')
        rospy.sleep(1)


        state = JointTrajectory()
        state.header.stamp = rospy.Time.now()
        state.joint_names = ["joint_1","joint_2","joint_3","joint_4"]
        point = JointTrajectoryPoint()
        point.positions = q
        point.time_from_start = rospy.Duration(1)
        state.points.append(point)
        pub.publish(state)
        print('published command')
        rospy.sleep(1)


        state = JointTrajectory()
        state.header.stamp = rospy.Time.now()
        state.joint_names = ["joint_1","joint_2","joint_3","joint_4","joint_5"]
        point = JointTrajectoryPoint()
        point.positions = q
        point.time_from_start = rospy.Duration(1)
        state.points.append(point)
        pub.publish(state)
        print('published command')
        rospy.sleep(1)

        

if __name__ == '__main__':
    try:
        joint_publisher()
    except rospy.ROSInterruptException:
        pass