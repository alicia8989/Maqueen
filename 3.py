from microbit import*
from Maqueen import*

robot = Maqueen()



while True:
    distancia = robot.read_distance()
    if distancia <= 10:
        robot.motor_stop_all()
    else:
        robot.set_motor(0,255)
        robot.set_motor(1,255)
