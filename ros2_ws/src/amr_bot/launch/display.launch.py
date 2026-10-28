import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # 1. Indicamos dónde está nuestro archivo URDF del robot
    urdf_file_name = 'amr_robot.urdf'
    urdf_path = os.path.join(
        get_package_share_directory('amr_bot'),
        'urdf',
        urdf_file_name
    )

    # 2. Creamos el nodo de ROS2 que publica la estructura del robot (Robot State Publisher)
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': open(urdf_path).read()}]
    )

    # 3. Devolvemos la descripción del lanzamiento para que ROS2 lo ejecute
    return LaunchDescription([
        robot_state_publisher_node
    ])