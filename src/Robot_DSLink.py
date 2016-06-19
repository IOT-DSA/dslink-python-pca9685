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

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

class DSLink_Robot(dslink.DSLink):
    def start(self):
        print("Starting Robot")
        self.responder.profile_manager.create_profile("servo")
        self.responder.profile_manager.register_set_callback("servo", self.set_value)

    def get_default_nodes(self, super_root):
        for i in range(16):
            servo = dslink.Node("servo_%i" % i, super_root)
            servo.set_config("$is", "servo")
            servo.set_type("number")
            servo.set_display_name("Servo %i" % i)
            servo.set_config("$writable", "write")
            servo.set_value(i)
            super_root.add_child(servo)
    
        return super_root

    def set_value(self, data):
        node = data[0]
        value = data[1]
    	node_name = node.name
    	arr = node_name.split("_");
    	pwm.set_pwm(int(arr[1]), 0, value)

if __name__ == "__main__":
    DSLink_Robot(dslink.Configuration("Robot", responder=True))
 
