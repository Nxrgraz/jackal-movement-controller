# Jackal Movement Controller

A ROS 2 Python package developed for the Clearpath Jackal autonomous ground vehicle.

## Overview

This project contains motion-control nodes that command the Jackal robot using velocity commands and odometry feedback.

The purpose of this project is to develop and test fundamental robotics control concepts in ROS 2, including:

- Publishers and Subscribers
- Odometry-based navigation
- Quaternion-to-Yaw conversion
- Feedback control loops
- Position and orientation tracking
- Autonomous motion commands

## Features

### Distance Controller

The distance controller:

- Subscribes to `/odom`
- Tracks robot displacement using odometry
- Publishes velocity commands to `/jackal_velocity_controller/cmd_vel_unstamped`
- Stops automatically after travelling a specified distance

### Rotation Controller

The rotation controller:

- Reads robot orientation from odometry
- Converts quaternion orientation data into yaw angles
- Calculates rotation relative to the starting orientation
- Rotates the robot toward the nearest 90-degree increment
- Stops once the target orientation is reached within a specified tolerance

## ROS Topics

### Subscribed Topics

| Topic | Message Type | Purpose |
|---------|---------|---------|
| `/odom` | `nav_msgs/msg/Odometry` | Robot position and orientation feedback |

### Published Topics

| Topic | Message Type | Purpose |
|---------|---------|---------|
| `/jackal_velocity_controller/cmd_vel_unstamped` | `geometry_msgs/msg/Twist` | Robot velocity commands |

## Mathematical Concepts

The rotation controller uses quaternion orientation data from the odometry message and converts it into yaw using:

```python
yaw = math.atan2(
    2.0 * (w * z + x * y),
    1.0 - 2.0 * (y * y + z * z)
)
```

The resulting yaw angle is used to determine the robot's rotational displacement and control its heading.

## Technologies

- ROS 2
- Python
- rclpy
- geometry_msgs
- nav_msgs
- Clearpath Jackal
- Linux

## Learning Objectives

This project was developed as part of ROS 2 training and robotics research preparation. The goal is to build practical experience with:

- Robot motion control
- State estimation using odometry
- Feedback-based navigation
- ROS 2 software development
- Autonomous robotic systems

## Author

Jerison Tian

University of Alberta Engineering
