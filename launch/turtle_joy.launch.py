# # 課題3.2

from launch import LaunchDescription
from launch_ros.actions import Node

# 以下にコードを追加してください
def generate_launch_description():
    return LaunchDescription(
        [
            Node(
                package="turtlesim",
                executable="turtlesim_node",
            ),

            Node(
                package="joy",
                executable="joy_node",
            ),

            Node(
                package="ros2_practice",
                executable="joy2twist",
            ),
        ]
    )
