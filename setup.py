from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'ros2_practice'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join("share", package_name, "launch"), glob("launch/*.launch.py")),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='whale',
    maintainer_email='oishi@hfg.sc.e.titech.ac.jp',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publisher = ros2_practice.publish:main',
            'subscriber = ros2_practice.subscribe:main',
            'joy2twist = ros2_practice.joy2twist:main',
            'multi_turtle_spawner = ros2_practice.multi_turtle_spawner:main',
            "robot_node = ros2_practice.robot:main",
            "consensus_controller = ros2_practice.consensus:main",
        ],
    },
)
