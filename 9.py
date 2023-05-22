from microbit import *
import radio
from Maqueen import Maqueen

mq = Maqueen()

radio.on()
radio.config(channel=12, group=0)

while True:
    message = radio.receive()
    if message == 'forward':
        mq.forward()
        sleep(200)  
        mq.stop()
    elif message == 'backwards':
        mq.set_motor (0,-255)
        mq.set_motor (1,-255)
        sleep(200)  
        mq.stop()
    elif message == 'vuelta':
        mq.turn_right()
        sleep(600)  
        mq.stop()
    sleep(100)
