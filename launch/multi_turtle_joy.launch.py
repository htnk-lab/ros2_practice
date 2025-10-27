# # 課題3.3

# from launch import LaunchDescription
# from launch_ros.actions import Node

# def generate_launch_description():
#     return LaunchDescription(

#         [
#             Node(
#                 package="turtlesim",
#                 namespace="turtlesim1",
#                 executable="turtlesim_node",
#                 remappings=[("/turtlesim1/turtle1/cmd_vel", "/turtle1/cmd_vel")],
#             ),

#             Node(
#                 ??? 
#                 ???
#                 ???
#                 remappings=[("/turtlesim2/turtle1/cmd_vel", "/turtle1/cmd_vel")],
#             ),

#             Node(package="joy", executable="joy_node", name="joy"),

#             Node(
#                 package="ros2_practice",
#                 executable="joy2twist",
#                 name="joy2twist",
#             ),
#         ]
#     )