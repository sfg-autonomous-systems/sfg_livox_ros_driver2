from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

launch_arguments = [
    DeclareLaunchArgument(
        name="xfer_format",
        default_value="1",
        description="0-Pointcloud2(PointXYZRTL), 1-customized pointcloud format",
    ),
    DeclareLaunchArgument(
        name="multi_topic",
        default_value="0",
        description="0-All LiDARs share the same topic, 1-One LiDAR one topic",
    ),
    DeclareLaunchArgument(
        name="data_src",
        default_value="0",
        description="0-lidar, others-Invalid data src",
    ),
    DeclareLaunchArgument(
        name="publish_freq",
        default_value="10.0",
        description="Frequency of publish, e.g., 5.0, 10.0, 20.0, 50.0",
    ),
    DeclareLaunchArgument(
        name="output_data_type",
        default_value="0",
        description="Output data type",
    ),
    DeclareLaunchArgument(
        name="frame_id",
        default_value="livox_frame",
        description="TF frame ID",
    ),
    DeclareLaunchArgument(
        name="user_config_path",
        description="Path to user config file",
    ),
]


def generate_launch_description() -> LaunchDescription:
    return LaunchDescription(
        launch_arguments
        + [
            Node(
                package="livox_ros_driver2",
                namespace="go2",
                executable="livox_ros_driver2_node",
                parameters=[
                    {launch_argument.name: LaunchConfiguration(launch_argument.name)}
                    for launch_argument in launch_arguments
                ],
                output="screen",
                emulate_tty=True,
            )
        ]
    )
