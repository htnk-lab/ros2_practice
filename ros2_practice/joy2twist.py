import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

class Joy2Twist(Node):
    def __init__(self):
        super().__init__('joy2twist')
        # publish
        self.pub = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        # subscribe
        self.sub = self.create_subscription(Joy, 'joy', self.callback, 10)
        # Twist (empty)
        self.vel = Twist()
    
    def callback(self, msg):
        self.vel.linear.x = msg.axes[3]
        self.vel.angular.z = msg.axes[4]
        self.pub.publish(self.vel)

def main(args=None):
    rclpy.init(args=args)
    node = Joy2Twist()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
