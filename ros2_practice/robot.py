import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, PoseStamped, PointStamped
import math


class RobotNode(Node):
    def __init__(self, node_name="robot_node"):
        super().__init__(node_name)
        self.node_name = node_name
        self.robot_name = self.get_namespace().strip("/")

        # 初期位置をパラメータとして受け取る
        self.declare_parameter("initial_x", 0.0)
        self.declare_parameter("initial_y", 0.0)
        self.declare_parameter("initial_theta", 0.0)
        self.x = self.get_parameter("initial_x").get_parameter_value().double_value
        self.y = self.get_parameter("initial_y").get_parameter_value().double_value
        self.theta = (
            self.get_parameter("initial_theta").get_parameter_value().double_value
        )

        self.twist_sub = self.create_subscription(
            Twist, "cmd_vel", self.twist_callback, 10
        )
        self.pose_pub = self.create_publisher(PoseStamped, "pose", 10)
        self.point_pub = self.create_publisher(PointStamped, "point", 10)
        self.timer = self.create_timer(0.01, self.update)

        self.vx = 0.0
        self.vy = 0.0
        self.vtheta = 0.0
        self.last_time = self.get_clock().now()

        self.get_logger().info(f"{self.robot_name} node started")

    def twist_callback(self, msg):
        self.vx = msg.linear.x
        self.vy = msg.linear.y
        self.vtheta = msg.angular.z

    def update(self):
        current_time = self.get_clock().now()
        dt = (current_time - self.last_time).nanoseconds / 1e9
        self.last_time = current_time

        # Update position and orientation
        self.x += (self.vx * math.cos(self.theta) - self.vy * math.sin(self.theta)) * dt
        self.y += (self.vx * math.sin(self.theta) + self.vy * math.cos(self.theta)) * dt
        self.theta += self.vtheta * dt

        # Publish PoseStamped
        pose_msg = PoseStamped()
        pose_msg.header.stamp = current_time.to_msg()
        pose_msg.header.frame_id = "world"
        pose_msg.pose.position.x = self.x
        pose_msg.pose.position.y = self.y
        pose_msg.pose.position.z = 0.0
        pose_msg.pose.orientation.z = math.sin(self.theta / 2.0)
        pose_msg.pose.orientation.w = math.cos(self.theta / 2.0)
        self.pose_pub.publish(pose_msg)

        # Publish PointStamped
        point_msg = PointStamped()
        point_msg.header.stamp = current_time.to_msg()
        point_msg.header.frame_id = "world"
        point_msg.point.x = self.x
        point_msg.point.y = self.y
        point_msg.point.z = 0.0
        self.point_pub.publish(point_msg)


def main(args=None):
    rclpy.init(args=args)
    node = RobotNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
