# Jackal Movement Controller

ROS 2 node developed for the Clearpath Jackal robot.

Features:
- Subscribes to /odom
- Publishes Twist commands to /jackal_velocity_controller/cmd_vel_unstamped
- Tracks robot displacement using odometry
- Stops after traveling a specified distance

Built as part of robotics and ROS 2 training.
