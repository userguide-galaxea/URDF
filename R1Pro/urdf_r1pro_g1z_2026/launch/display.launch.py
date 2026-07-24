import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def launch_setup(context, *args, **kwargs):
    urdf_name = LaunchConfiguration("urdf").perform(context)
    urdf_file = os.path.join(
        get_package_share_directory("r1pro_urdf"), "urdf", urdf_name
    )

    with open(urdf_file, "r", encoding="utf-8") as f:
        robot_description = f.read()

    return [
        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            name="robot_state_publisher",
            output="screen",
            parameters=[{"robot_description": robot_description}],
        ),
        Node(
            package="joint_state_publisher_gui",
            executable="joint_state_publisher_gui",
            name="joint_state_publisher_gui",
            condition=IfCondition(LaunchConfiguration("use_gui")),
        ),
        Node(
            package="joint_state_publisher",
            executable="joint_state_publisher",
            name="joint_state_publisher",
            condition=UnlessCondition(LaunchConfiguration("use_gui")),
        ),
        Node(
            package="rviz2",
            executable="rviz2",
            name="rviz2",
            output="screen",
            condition=IfCondition(LaunchConfiguration("use_rviz")),
        ),
    ]


def generate_launch_description():
    return LaunchDescription(
        [
            DeclareLaunchArgument(
                "urdf",
                default_value="r1pro_2026.urdf",
                description="URDF file under the package urdf directory.",
            ),
            DeclareLaunchArgument(
                "use_gui",
                default_value="true",
                description="Start joint_state_publisher_gui when true.",
            ),
            DeclareLaunchArgument(
                "use_rviz",
                default_value="true",
                description="Start RViz2 when true.",
            ),
            OpaqueFunction(function=launch_setup),
        ]
    )
