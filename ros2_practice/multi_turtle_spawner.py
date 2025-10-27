import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn, Kill
import json


class MultiTurtleSpawner(Node):
    def __init__(self):
        super().__init__("multi_turtle_spawner")

        # JSON文字列で初期位置を受け取る
        self.declare_parameter("initial_positions_json", "{}")
        positions_json = (
            self.get_parameter("initial_positions_json")
            .get_parameter_value()
            .string_value
        )
        self.positions = json.loads(positions_json)

        if not self.positions:
            self.get_logger().error("initial_positions_json is empty")
            return

        self.get_logger().info(f"Initial positions: {self.positions}")

        # デフォルト turtle1 を削除
        self.kill_cli = self.create_client(Kill, "kill")
        while not self.kill_cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Waiting for /kill service...")

        req_kill = Kill.Request()
        req_kill.name = "turtle1"
        future = self.kill_cli.call_async(req_kill)
        rclpy.spin_until_future_complete(self, future)
        self.get_logger().info("Default turtle1 killed")

        # spawn サービス
        self.spawn_cli = self.create_client(Spawn, "spawn")
        while not self.spawn_cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Waiting for /spawn service...")

        # すべての turtle を spawn
        self.turtle_names = []
        for name, pos in self.positions.items():
            self.spawn_turtle(name, pos["x"], pos["y"], 0.0)
            self.turtle_names.append(name)

        self.get_logger().info(f"Turtles ready: {self.turtle_names}")

    def spawn_turtle(self, name, x, y, theta):
        req = Spawn.Request()
        req.name = name
        req.x = x
        req.y = y
        req.theta = theta
        future = self.spawn_cli.call_async(req)
        rclpy.spin_until_future_complete(self, future)
        self.get_logger().info(f"Spawned {name} at ({x},{y}, theta={theta})")


def main(args=None):
    rclpy.init(args=args)
    node = MultiTurtleSpawner()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
