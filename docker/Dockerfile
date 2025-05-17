FROM osrf/ros:jazzy-desktop-full

RUN apt-get update
RUN apt-get install -y git && apt-get install -y python3-pip
RUN mkdir -p /home/corvus/Projects/ros2

## Install RQT and Colcon
RUN apt-get install -y '~nros-jazzy-rqt*'
RUN apt-get install -y python3-colcon-common-extensions

## Install Webot
RUN apt-get install -y ros-jazzy-webots-ros2

## NOTICE!!!
## <----------- Once inside the docker, set the following function to ALWAYS return False ------------>
# sudo vim /opt/ros/jazzy/lib/python3.12/site-packages/webots_ros2_driver/utils.py
# def is_wsl():
#    return False

## Add `ros` to env variable
RUN echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc

## Setup Webot
RUN export WEBOTS_HOME=/usr/local/webots

## Clone and build Package Overlay (SEQUENTIAL FLAG IS IMPORTANT)
RUN cd /home/corvus/Projects/ && git clone https://github.com/corvus-rex/ros2_webot.git 
##RUN colcon build --symlink-install --executor sequential
# RUN git clone https://github.com/corvus-rex/examples src/examples -b jazzy

## Add `colcon_cd` to env variable
RUN echo "source /usr/share/colcon_cd/function/colcon_cd.sh" >> ~/.bashrc && echo "export _colcon_cd_root=/opt/ros/jazzy/" >> ~/.bashrc

RUN echo "All good"