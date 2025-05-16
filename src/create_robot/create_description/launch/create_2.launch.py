import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    # Path to the xacro file
    xacro_file = PathJoinSubstitution([
        FindPackageShare('create_description'),
        'urdf',
        'create_2.urdf.xacro'
    ])

    # robot_state_publisher node
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{
            'robot_description': Command(['xacro ', xacro_file])
        }]
    )

    return LaunchDescription([
        robot_state_publisher_node
    ])
