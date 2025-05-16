import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # Paths
    config_default = os.path.join(
        get_package_share_directory('create_bringup'),
        'config', 'default.yaml'
    )
    desc_launch_path = os.path.join(
        get_package_share_directory('create_description'),
        'launch', 'create_2.launch.py'
    )

    # Declare launch arguments
    config_arg = DeclareLaunchArgument(
        'config',
        default_value=config_default,
        description='Path to the config file'
    )
    desc_arg = DeclareLaunchArgument(
        'desc',
        default_value='true',
        description='Whether to include the robot description'
    )

    # Nodes
    create_driver_node = Node(
        package='create_driver',
        executable='create_driver',
        name='create_driver',
        output='screen',
        parameters=[
            LaunchConfiguration('config'),
            {'robot_model': 'CREATE_2'}
        ]
    )

    create_description_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(desc_launch_path),
        condition=IfCondition(LaunchConfiguration('desc'))
    )

    return LaunchDescription([
        config_arg,
        desc_arg,
        create_driver_node,
        create_description_launch
    ])
