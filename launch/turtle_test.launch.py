from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # turtlesim_node を起動
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            output='screen'
        ),
        # キーボードで亀を動かすための turtle_teleop_key ノードを起動
        Node(
            package='turtlesim',
            executable='turtle_teleop_key',
            output='screen',
            prefix='xterm -e'
        )
    ])