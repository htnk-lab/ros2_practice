import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose


class ConsensusController(Node):
    def __init__(self):
        super().__init__("consensus_controller")

        self.n = 3  # ロボット台数
        self.x_list = [0.0] * self.n
        self.y_list = [0.0] * self.n

        # Subscriber の作成
        for i in range(self.n):
            # topic名を作成
            topic = "/turtle" + str(i + 1) + "/pose"

            # Subscribeしたときに呼ばれるコールバック関数
            def callback(msg, index=i):
                self.x_list[index] = msg.x
                self.y_list[index] = msg.y

            self.create_subscription(Pose, topic, callback, 10)

        # Publisher の作成
        self.cmd_vel_pubs = []
        for i in range(self.n):
            # topic名を作成
            topic = "/turtle" + str(i + 1) + "/cmd_vel"

            pub = self.create_publisher(Twist, topic, 10)
            self.cmd_vel_pubs.append(pub)

        self.gain = 0.2

        # タイマーの作成
        # update 関数が 0.1 秒ごとに呼ばれる
        self.timer = self.create_timer(0.1, self.update)

    def update(self):
        # 平均値を計算
        mean_x = sum(self.x_list) / self.n
        mean_y = sum(self.y_list) / self.n

        for i in range(self.n):
            dx = mean_x - self.x_list[i]
            dy = mean_y - self.y_list[i]

            cmd = Twist()
            cmd.linear.x = dx
            cmd.linear.y = dy
            cmd.linear.x *= self.gain
            cmd.linear.y *= self.gain

            # cmd_vel トピックに速度指令を送る
            self.cmd_vel_pubs[i].publish(cmd)


def main(args=None):
    rclpy.init(args=args)
    node = ConsensusController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
