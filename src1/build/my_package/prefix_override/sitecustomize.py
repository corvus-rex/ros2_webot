import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/corvus/Projects/ros2_webot/src1/install/my_package'
