import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import math

class degrees(Node):
    def __init__(self):
        super().__init__('degrees')
        self.publisher = self.create_publisher(Twist, 'jackal_velocity_controller/cmd_vel_unstamped', 10)
        self.subscriber = self.create_subscription(Odometry, '/odom', self.callback, 10)
        self.timer = self.create_timer(0.1, self.rotate)
        self.start = True
        self.start_yaw = 0
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
        if not round(math.pi/2) == self.rotation:
            if self.rotation < 0:
                msg = Twist()
                msg.angular.z = 0.2
            else:
                msg.angular.z = -0.2
        if not round(math.pi)
            
        self.publisher.publish(msg)
def main(args=None):
    rclpy.init(args=args)
    rotate = degrees()
    rclpy.spin(rotate)
    rotate.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()
