# Name : James Karuri
# Date: 09/03/2026
# Program to show an instance of a drone flight

from pysimverse import Drone
import time

# Create an instance of drone 
drone = Drone()
drone.connect()

drone.take_off()
#distance is in cm

drone.move_foward(280)
drone.move_backward(280)
time.sleep(1)
drone.move_left(280)
time.sleep(1)
drone.move_right(280)
time.sleep(1)

drone.land
