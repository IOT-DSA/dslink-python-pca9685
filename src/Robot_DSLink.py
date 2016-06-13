from __future__ import division

import dslink

import time

# Import the PCA9685 module.
import Adafruit_PCA9685
# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 400  # Max pulse length out of 4096

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

class DSLink_Robot(dslink.DSLink):
    def start(self):
        print("Starting Robot")
        #self.update_data()

    def get_default_nodes(self, super_root):
        for i in range(16):
            print(i)
    	servo_0 = dslink.Node("servo_0", super_root)
        servo_0.set_display_name("Servo 0")
        servo_0.set_type("number")
        servo_0.set_value(0)
        servo_0.set_config("$writable", "write")
        servo_0.set_value_callback = self.set_value
        super_root.add_child(servo_0)

        servo_1 = dslink.Node("servo_1", super_root)
        servo_1.set_display_name("Servo 1")
        servo_1.set_type("number")
        servo_1.set_value(1)
        servo_1.set_config("$writable", "write")
        servo_1.set_value_callback = self.set_value
        super_root.add_child(servo_1)

        servo_2 = dslink.Node("servo_2", super_root)
        servo_2.set_display_name("Servo 2")
        servo_2.set_type("number")
        servo_2.set_value(2)
        servo_2.set_config("$writable", "write")
        servo_2.set_value_callback = self.set_value
        super_root.add_child(servo_2)

        servo_3 = dslink.Node("servo_3", super_root)
        servo_3.set_display_name("Servo 3")
        servo_3.set_type("number")
        servo_3.set_value(3)
        servo_3.set_config("$writable", "write")
        servo_3.set_value_callback = self.set_value
        super_root.add_child(servo_3)

        servo_4 = dslink.Node("servo_4", super_root)
        servo_4.set_display_name("Servo 4")
        servo_4.set_type("number")
        servo_4.set_value(4)
        servo_4.set_config("$writable", "write")
        servo_4.set_value_callback = self.set_value
        super_root.add_child(servo_4)

        servo_5 = dslink.Node("servo_5", super_root)
        servo_5.set_display_name("Servo 5")
        servo_5.set_type("number")
        servo_5.set_value(5)
        servo_5.set_config("$writable", "write")
        servo_5.set_value_callback = self.set_value
        super_root.add_child(servo_5)

        servo_6 = dslink.Node("servo_6", super_root)
        servo_6.set_display_name("Servo 6")
        servo_6.set_type("number")
        servo_6.set_value(6)
        servo_6.set_config("$writable", "write")
        servo_6.set_value_callback = self.set_value
        super_root.add_child(servo_6)

        servo_7 = dslink.Node("servo_7", super_root)
        servo_7.set_display_name("Servo 7")
        servo_7.set_type("number")
        servo_7.set_value(7)
        servo_7.set_config("$writable", "write")
        servo_7.set_value_callback = self.set_value
        super_root.add_child(servo_7)

        servo_8 = dslink.Node("servo_8", super_root)
        servo_8.set_display_name("Servo 8")
        servo_8.set_type("number")
        servo_8.set_value(8)
        servo_8.set_config("$writable", "write")
        servo_8.set_value_callback = self.set_value
        super_root.add_child(servo_8)

        servo_9 = dslink.Node("servo_9", super_root)
        servo_9.set_display_name("Servo 9")
        servo_9.set_type("number")
        servo_9.set_value(9)
        servo_9.set_config("$writable", "write")
        servo_9.set_value_callback = self.set_value
        super_root.add_child(servo_9)

        servo_10 = dslink.Node("servo_10", super_root)
        servo_10.set_display_name("Servo 10")
        servo_10.set_type("number")
        servo_10.set_value(10)
        servo_10.set_config("$writable", "write")
        servo_10.set_value_callback = self.set_value
        super_root.add_child(servo_10)

        servo_11 = dslink.Node("servo_11", super_root)
        servo_11.set_display_name("Servo 11")
        servo_11.set_type("number")
        servo_11.set_value(11)
        servo_11.set_config("$writable", "write")
        servo_11.set_value_callback = self.set_value
        super_root.add_child(servo_11)

        servo_12 = dslink.Node("servo_12", super_root)
        servo_12.set_display_name("Servo 12")
        servo_12.set_type("number")
        servo_12.set_value(12)
        servo_12.set_config("$writable", "write")
        servo_12.set_value_callback = self.set_value
        super_root.add_child(servo_12)

        servo_13 = dslink.Node("servo_13", super_root)
        servo_13.set_display_name("Servo 13")
        servo_13.set_type("number")
        servo_13.set_value(13)
        servo_13.set_config("$writable", "write")
        servo_13.set_value_callback = self.set_value
        super_root.add_child(servo_13)

        servo_14 = dslink.Node("servo_14", super_root)
        servo_14.set_display_name("Servo 14")
        servo_14.set_type("number")
        servo_14.set_value(14)
        servo_14.set_config("$writable", "write")
        servo_14.set_value_callback = self.set_value
        super_root.add_child(servo_14)

        servo_15 = dslink.Node("servo_15", super_root)
        servo_15.set_display_name("Servo 15")
        servo_15.set_type("number")
        servo_15.set_value(15)
        servo_15.set_config("$writable", "write")
        servo_15.set_value_callback = self.set_value
        super_root.add_child(servo_15)

        return super_root

    def set_value(self, node, value):
    	node_name = node.name
    	arr = node_name.split("_");
    	pwm.set_pwm(int(arr[1]), 0, value)

    #def update_data(self):
        #reactor.callLater(1, self.update_data)

if __name__ == "__main__":
    DSLink_Robot(dslink.Configuration("Robot", responder=True))
 
