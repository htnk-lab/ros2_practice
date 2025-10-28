from launch import LaunchDescription
from launch.actions import TimerAction
from launch_ros.actions import Node
import json


def generate_launch_description():
    # turtleの名前と初期位置
    robots = {
        "turtle1": {"x": 1.0, "y": 1.0},
        "turtle2": {"x": 8.0, "y": 5.0},
        "turtle3": {"x": 8.0, "y": 3.0},
    }

    return LaunchDescription(
        [
            # turtlesim ノード
            Node(
                package="turtlesim",
                executable="turtlesim_node",
                name="turtlesim",
                output="screen",
            ),
            # turtleを複数出現させるためのもの
            Node(
                package="ros2_practice",
                executable="multi_turtle_spawner",
                name="multi_turtle_spawner",
                output="screen",
                parameters=[{"initial_positions_json": json.dumps(robots)}],
            ),
            # 合意制御ノード
            Node(
                package="ros2_practice",
                executable="consensus_controller",
                name="consensus_controller",
                output="screen",
            ),
        ]
    )
