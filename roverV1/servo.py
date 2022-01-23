import machine
from time import sleep
p18 = machine.Pin(18)
servoAxisX = machine.PWM(p18,freq=50)
# duty for servo is between 40 - 115

class ServoControl:
    def __init__(self, servoX, servoY, servoGrab):
        self.servoX = servoX
        self.servoY = servoY
        self.servoGrab = servoGrab
       
    # function to set value of servoX
    def set_servoX(self, servoXVal):
        self.servoX = servoXVal
        print(f"servoXVal setter method called with val {servoXVal}")
    # function to set value of servoY
    def set_servoYVal(self, servoYVal):
        self.servoY = servoYVal
        print(f"servoXVal setter method called with val {servoXVal}")
    def set_ServoGrab(self, ServoGrabVal):
        self.ServoGrab = ServoGrabVal
        print(f"servoGrab setter method called with val {ServoGrabVal}")
