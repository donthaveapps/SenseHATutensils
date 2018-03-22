from subprocess import check_output
from sense_hat import SenseHat
#, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
sense = SenseHat()
sense.set_rotate(r=180)

def displayip():
    sense.show_message(check_output(['hostname', '-I']))

sense.stick.direction_up = displayip