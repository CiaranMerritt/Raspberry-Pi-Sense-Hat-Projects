from sense_hat import SenseHat
import time
# import only system from os
from os import system

sense = SenseHat()

# alternatives
minutes = 0
seconds = 20
t_end = time.time() + (60 * minutes) + seconds
while time.time() < t_end:
    # do whatever you do
    system('clear')
    orientation = sense.get_orientation()
    print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation))

    print(sense.orientation)
    time.sleep(1)