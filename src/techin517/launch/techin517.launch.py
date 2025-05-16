from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    # Launch file 1: create_bringup
    create_launch = os.path.join(
        get_package_share_directory('create_bringup'),
        'launch',
        'create_2.launch.py'
    )

    # Launch file 2: sllidar_ros2
    lidar_launch = os.path.join(
        get_package_share_directory('sllidar_ros2'),
        'launch',
        'sllidar_a1_launch.py'
    )

    # Launch file 3: stereo_inertial_node
    camera_launch = os.path.join(
        get_package_share_directory('depthai_ros_driver'),
        'launch',
        'camera.launch.py'
    )

    return LaunchDescription([
        
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(lidar_launch)
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(camera_launch)
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(create_launch)
        )
    ])

