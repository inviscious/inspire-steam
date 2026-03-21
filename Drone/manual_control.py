from pysimverse import Drone
import time
import cv2

drone = Drone()
drone.connect()
time.sleep(1)

drone.take_off(5)
rc_speed = 200

while True:
    key = cv2.waitKey(1) & 0xff

    # get all values to 0
    left_right= 0
    foward_backward = 0
    up_down = 0
    yaw = 0

    if key == ord("w"):
        foward_backward = rc_speed
    elif key == ord("s"):
        foward_backward = -rc_speed
    elif key == ord("a"):
        left_right = rc_speed
    elif key == ord("d"):
        left_right = -rc_speed
    elif key == ord("f"):
        up_down = rc_speed
    elif key == ord("c"):
        up_down = -rc_speed
    elif key == ord("q"):
        yaw = -1
    elif key == ord("e"):
        yaw = 1
    elif key == ord("l") or key == 27:
        drone.land()
        time.sleep(2)
        break
    drone.send_rc_control(
        left_right,
        foward_backward,
        up_down,
        yaw
    )
