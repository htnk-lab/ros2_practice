# # 課題4 

# import rclpy
# from rclpy.node import Node
# from geometry_msgs.msg import Twist
# from turtlesim.msg import Pose


# class ConsensusController(Node):
#     def __init__(self):
#         super().__init__("consensus_controller")

#         self.n = 3  # ロボット台数
#         self.x_list = [0.0] * self.n
#         self.y_list = [0.0] * self.n

#         # Subscriber の作成
#         for i in range(self.n):
#             # topic名を作成
#             topic = ???

#             # Subscribeしたときに呼ばれるコールバック関数
#             def callback(msg, index=i):
#                 self.x_list[???] = ???
#                 self.y_list[???] = ???

#             self.create_subscription(???, topic, callback, 10)

#         # Publisher の作成
#         self.cmd_vel_pubs = []
#         for i in range(self.n):
#             # topic名を作成
#             topic = ???

#             pub = self.create_publisher(???, topic, 10)
#             self.cmd_vel_pubs.append(pub)

#         # 速度調整用のゲイン
#         self.gain = 0.2

#         # タイマーの作成
#         # update 関数が 0.1 秒ごとに呼ばれる
#         self.timer = self.create_timer(0.1, self.update)

#     def update(self):
#         # 平均値を計算
#         mean_x = ???
#         mean_y = ???

#         for i in range(self.n):
#             dx = ???
#             dy = ???

#             cmd = Twist()
#             ??? = dx
#             ??? = dy
#             ??? *= self.gain
#             ??? *= self.gain

#             # cmd_vel トピックに速度指令を送る
#             ???


# def main(args=None):
#     rclpy.init(args=args)
#     node = ConsensusController()
#     rclpy.spin(node)
#     node.destroy_node()
#     rclpy.shutdown()


# if __name__ == "__main__":
#     main()
