from RPi_GPIO_Rotary import rotary
import time


def cwTurn():
    print("CW Turn")

def ccwTurn():
    print("CCW Turn")

def buttonPushed():
    print("Button Pushed")

def valueChanged(count):
    print(count)

obj = rotary.Rotary(23,24,25,4)
obj.register(increment=cwTurn, decrement=ccwTurn)
obj.register(pressed=buttonPushed, onchange=valueChanged)
obj.start()
time.sleep(5)
obj.stop()