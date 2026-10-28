# 1. Usamos como base la imagen oficial de ROS2 Humble instalada sobre Ubuntu 22.04
FROM ros:humble-ros-base-jammy

# 2. Evitamos que la instalación pida interacción de teclado durante el despliegue
ENV DEBIAN_FRONTEND=noninteractive

# 3. Instalamos las herramientas necesarias: Gazebo (simulador), Python y paquetes de sensores ROS2
RUN apt-get update && apt-get install -y \
    ros-humble-desktop \
    ros-humble-gazebo-ros-pkgs \
    ros-humble-nav2-bringup \
    ros-humble-navigation2 \
    python3-pip \
    python3-colcon-common-extensions \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 4. Instalamos las librerías de Python para procesamiento de imágenes e IA básica
RUN pip3 install --no-cache-dir \
    opencv-python \
    numpy \
    pandas \
    duckdb \
    paho-mqtt

# 5. Creamos y establecemos la carpeta de trabajo dentro del contenedor
WORKDIR /ros2_ws

# 6. Cargamos automáticamente el entorno de ROS2 al abrir la terminal dentro del contenedor
RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc

CMD ["bash"]