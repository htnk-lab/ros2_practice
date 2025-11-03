# ROS2講習
本パッケージはROS2講習で使用します。

## 必要環境
- Ubuntu22.04
- ROS 2 Humble
- Python

## インストール
ROS2環境構築後の説明となっております。ROS2環境構築は以下のサイトを参考に行ってください。

[ROS2公式サイト](https://docs.ros.org/en/humble/index.html)

[ROS2 Humbleインストール参考サイト](https://qiita.com/porizou1/items/5dd915402e2990e4d95f)

以下のコードをコマンドウィンドウで入力、実行してください。
```sh
mkdir ~/ros2_ws/src
cd ~/ros2_ws/src
git clone https://github.com/htnk-lab/ros2_practice.git
```
```sh
cd ~/ros2_ws/src/ros2_practice
sudo apt install xterm
python3 -m pip install -r requirements.txt
```
```sh
cd ~/ros2_ws
colcon build
source ~/ros2_ws/install/local_setup.bash
```
