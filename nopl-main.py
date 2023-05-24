from microbit import *
import radio
from Maqueen import Maqueen

mq = Maqueen()

radio.on()
radio.config(channel=18, group=0)

while True:
    message = radio.receive()
    if message == 'izquierda':
        mq.turn_left()
        sleep(100)  
        mq.stop()
    elif message == 'derecha':
        mq.turn_right()
        sleep(100)  
        mq.stop()
    elif message == 'vuelta':
        mq.turn_right()
        sleep(600)  
        mq.stop()
    sleep(100)