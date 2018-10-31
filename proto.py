from eu.mattdw.usbrobotarm.arm_controller import *
from eu.mattdw.usbrobotarm.specification import *
import time
import sys

controller = ArmController(ArmController.create_usb_device())

controller.also_move({'base': 'clockwise'})
#controller.also_move({'base': 'anticlockwise'})
time.sleep(0.5)

controller.also_move({'shoulder': 'up'})
#controller.also_move({'shoulder': 'down'})
time.sleep(0.5)

controller.also_move({'elbow': 'up'})
#controller.also_move({'elbow': 'down'})
time.sleep(0.5)

controller.also_move({'wrist': 'up'})
#controller.also_move({'wrist': 'down'})
time.sleep(0.5)

controller.also_move({'grip': 'open'})
#controller.also_move({'grip': 'close'})
time.sleep(0.5)

#controller.move({'grip': 'open'})
#controller.move({'grip': 'open'})
#time.sleep(1)

controller.reset()