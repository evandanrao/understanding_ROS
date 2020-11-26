 #!/usr/bin/env python  #<-----To make a python file executable, Insert at the top of the file
#This was created from the learnings of the video: https://www.youtube.com/watch?v=uip2BbaazjU
#The following is coded at publisher_node.py
#To create a publisher node using python first  lets create a directory for the catkin_package,

#Open catkin_ws and create a package as follows
#> catkin_create_pkg <pkg_name> <dep1> <dep2>
#ex: catkin_create_pkg pub_sub_test rospy roscpp
#creates:- CMakeLists.txt  include  package.xml  src
#cd src 
#code <pubnode_script.py> 
import rospy  #<----import the rospy dependency to enable ros to read this document in python
from std_msgs.msg import String #<----you can get all the std_msgs at roscd std_msgs/msg/

def publisher():
    pub = rospy.Publisher('string_publish',String,queue_size=10) #Publishername=rospy.Publisher(topic_name,message_type,queue_size)
    rate=rospy.Rate(1)#rate at which you shud be publishing the message
    msg_to_publish=String()
    counter=0
    while not rospy.is_shutdown():
        string_to_publish="Publishing the  counter: %d"%counter
        counter+=1
        msg_to_publish.data=string_to_publish
        pub.publish(msg_to_publish)
        rospy.loginfo(string_publish)
        rospy.sleep()
if __name__=="__main__":
    rospy.init_node("simple_publisher")
    publisher()
#after typing this, you got to catkin_make at the catkin_ws root, to compile all of this and then do source devel/setup.bash
#provide permissions: chmod +x publisher_node.py

        
    