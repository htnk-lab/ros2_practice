from launch_ros.actions import Node
from launch import LaunchDescription

def generate_launch_description():
    return LaunchDescription(
        [
            Node(
                package="turtlesim",
                executable="turtlesim_node",
            ),

            Node(package="joy", executable="joy_node", name="joy"),

            Node(
                package="ros2_practice",
                executable="joy2twist",
            ),
        ]
    )
