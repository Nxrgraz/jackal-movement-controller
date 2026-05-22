import rclpy
from rclpy.node import Node 
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import math

class twocm(Node):
    def __init__(self):
        super().__init__('one_cm')
        self.create_odo_responder = self.create_subscription(Odometry, '/odom', self.callback, 10)
        self.create_one_cm = self.create_publisher(Twist , '/jackal_velocity_controller/cmd_vel_unstamped', 10)
        self.timer = self.create_timer(0.1, self.runner)
        self.has_start = False
        self.start_x =0
        self.start_y = 0
        self.start_z = 0
        self.distance = 0
    def callback(self, msg):
        self.current_x = msg.pose.pose.position.x
        self.current_y = msg.pose.pose.position.y
        self.current_z = msg.pose.pose.position.z
        if self.has_start == False:
            self.start_x = self.current_x
            self.start_y = self.current_y
            self.start_z = self.current_z
            self.has_start = True
        else:
            self.distance = math.sqrt((self.current_x-self.start_x)**2+(self.current_y-self.start_y)**2+(self.current_z-self.start_z)**2)
    def runner(self):
         if self.distance < 0.01:
                msg=Twist()
                msg.linear.x= 0.02
                msg.linear.y = 0.0
                msg.linear.z = 0.0
                msg.angular.x = 0.0
                msg.angular.y = 0.0
                msg.angular.z = 0.0
                self.create_one_cm.publish(msg)
         else:
                msg=Twist()
                msg.linear.x= 0.0
                msg.linear.y = 0.0
                msg.linear.z = 0.0
                msg.angular.x = 0.0
                msg.angular.y = 0.0
                msg.angular.z = 0.0
                self.create_one_cm.publish(msg)

def main(args=None):
        rclpy.init(args=args)
        run=twocm()
        rclpy.spin(run)
        run.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

