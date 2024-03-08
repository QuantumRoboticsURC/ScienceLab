import rclpy
from std_msgs.msg import *
from rclpy.node import Node
import serial


class ScienceLab(Node):
    def __init__(self):
        super().__init__('Science_Lab')
        self.publisher_temp = self.create_publisher(Float64, 'lab/temperature', 10)
        self.publisher_hum = self.create_publisher(Float64, 'lab/humidity', 10)
        self.publisher_w = self.create_publisher(Float64, 'lab/weight', 10)

        self.ser = serial.Serial('/dev/ttyUSB0', 115200, timeout= 1)
        self.temp = Float64()
        self.hum = Float64()
        self.w= Float64()

        self.timer_ = self.create_timer(1,self.main)



    def main(self):
        print("holaaaaaa")
        data = self.ser.readline().decode().strip()
        if self.ser.in_waiting and (data != ''):
            print(f"My data {data}")
            try: 
                d = data.split(" ")
                print(d)
                a = d[0]
                b=d[1]
                c=d[2]

                self.temp.data = float(a)
                self.hum.data = float(b)
                self.w.data = float(c)

                self.publisher_temp.publish(self.temp)
                self.publisher_hum.publish(self.hum)
                self.publisher_w.publish(self.w)
            except Exception as e:
                print(e)
            




def main(args=None):
    rclpy.init(args=args)
    listener=ScienceLab()
    rclpy.spin(listener)
    listener.destroy_node()
    rclpy.shutdown()
    if __name__ == '__main__':
        main()
