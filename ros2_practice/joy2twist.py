# # 課題3.1

# import rclpy
# from rclpy.node import Node
# from geometry_msgs.msg import Twist
# from sensor_msgs.msg import Joy

# class Joy2Twist(Node):
#     def __init__(self):
#         super().__init__('joy2twist')
#         # publish
#         self.pub = self.create_publisher(???, 10)
#         # subscribe
#         self.sub = self.create_subscription(???, self.callback, 10)
#         # Twist (empty)
#         self.vel = Twist()
    
#     def callback(self, msg):
#         self.vel.linear.x = ???
#         self.vel.angular.z = ???
#         self.pub.publish(???)

# def main(args=None):
#     rclpy.init(args=args)
#     node = Joy2Twist()
#     rclpy.spin(node)
#     node.destroy_node()
#     rclpy.shutdown()

# if __name__ == '__main__':
#     main()


