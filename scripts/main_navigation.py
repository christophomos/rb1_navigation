#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from rb1_localization.srv import POI, POIRequest, POIResponse

class GoToPoint():

    SERVICE_NAME = "go_to_point"
    
    def __init__(self):
        self._service = rospy.Service(GoToPoint.SERVICE_NAME, POI, self.__service_callback)
        rospy.loginfo(f"Started service {GoToPoint.SERVICE_NAME}")
        self._ctrl_c = False
        rospy.on_shutdown(self.__shutdownhook)
    
    def __service_callback(self, request: POIRequest):
        return POIResponse()
        
    def __shutdownhook(self):
        self.ctrl_c = True
            
if __name__ == '__main__':
    rospy.init_node(GoToPoint.SERVICE_NAME, anonymous=True)
    GoToPoint()
    rospy.spin()