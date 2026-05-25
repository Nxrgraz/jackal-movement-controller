import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import math

class degrees(Node):
    def __init__(self):
        super().__init__('degrees')
        self.publisher = self.create_publisher(Twist, '/jackal_velocity_controller/cmd_vel_unstamped', 10)
        self.subscriber = self.create_subscription(Odometry, '/odom', self.callback, 10)
        self.timer = self.create_timer(0.1, self.rotate)
        self.start = True
        self.start_yaw = 0
        self.rotation = 0.0
    def callback(self, msg):
        self.current_x = msg.pose.pose.orientation.x
        self.current_y = msg.pose.pose.orientation.y
        self.current_z = msg.pose.pose.orientation.z
        self.current_w = msg.pose.pose.orientation.w
        self.current_yaw = math.atan2(2.0*(self.current_w*self.current_z+self.current_x*self.current_y), 1.0 - 2.0 * (self.current_y**2 + self.current_z**2))
        if self.start == True:
            self.start_yaw = self.current_yaw
            self.start = False
        else:
            self.rotation = self.current_yaw - self.start_yaw
    def rotate(self):
        error1 = 0 - self.rotation
        error2 = 1.57 - self.rotation
        error3 = 3.14 - self.rotation
        error4 = -1.57 - self.rotation
        error5 = -3.14 - self.rotation
        targets = [error1, error2, error3, error4, error5]
        if abs(error1) < 0.087 or abs(error2) < 0.087 or abs(error3) < 0.087 or abs(error4) < 0.087 or abs(error5) < 0.087:
            msg = Twist()
            msg.angular.z = 0.0
        elif min(targets, key=abs) > 0:
            msg = Twist()
            msg.angular.z = 0.2
        else:
            msg = Twist()
            msg.angular.z = -0.2
        self.publisher.publish(msg)
def main(args=None):
    rclpy.init(args=args)
    rotate = degrees()
    rclpy.spin(rotate)
    rotate.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()
