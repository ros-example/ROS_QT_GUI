#!/usr/bin/env python3

from PyQt5.QtCore import QThread
import rospy
from std_msgs.msg import String
import os

class QNode(QThread):

    def __init__(self,argv):
        super(QNode, self).__init__()
        self.init_argv = argv
        print("init")

        # ros::Publisher chatter_publisher;
        # self.chatter_publisher = rospy.Publisher("pygui_topic", String, queue_size=10)
        # chatter_subscriber = rospy.Subscriber
        rospy.init_node ( 'py_imu' , anonymous=True)
        rospy.Subscriber ( "chatter", String , self.Callback,queue_size=100)

        rospy.loginfo("init")

    def run(self) -> None:
        rospy.loginfo("run : thread pid %s ...." % os.getpid())
        rospy.spin()

    def Callback( self,data):

        rospy.loginfo("%s " % rospy.Time.now())
        rospy.loginfo(rospy.get_caller_id() + "I heard %s : pid = %s"% (data.data,os.getpid()))

if __name__ == "__main__":
    from PyQt5.QtCore import QCoreApplication
    import sys
    core_app = QCoreApplication(sys.argv)
    thread = QNode(sys.argv)
    thread.start()
    core_app.exec()
