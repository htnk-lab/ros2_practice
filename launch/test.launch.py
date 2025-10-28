from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ros2_practice',
            executable='publisher',
            output='screen'
        ),
        
        Node(
            package='ros2_practice',
            executable='subscriber',
            output='screen',
        )
    ])