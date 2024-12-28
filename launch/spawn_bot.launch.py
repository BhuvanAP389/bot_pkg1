from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():

    pkg_share = get_package_share_directory('bot_pkg1')

    urdf_path = os.path.join(pkg_share, 'urdf', 'bot.urdf')
    
    with open(urdf_path, 'r') as file:
        robot_description = file.read()

    return LaunchDescription([

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            parameters=[{'robot_description': robot_description}],
            output='screen'
        ),
        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            arguments=['/model/bot_pkg1/tf@tf2_msgs/msg/TFMessage@ignition.msgs.Pose_V'],
            output='screen'
        ),
        Node(
            package='ros_gz_sim',
            executable='create',
            name='robot_spawner',
            arguments=['-string', robot_description, 
                      '-name', 'bot_pkg1',
                      '-x', '0.0',
                      '-y', '0.0',
                      '-z', '0.5'],
            output='screen'
        )
    ])
