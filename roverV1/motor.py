from machine import Pin, PWM

frequency = 5000
motor01 = PWM(Pin(2), frequency)
motor02 = PWM(Pin(12), frequency)
motor03 = PWM(Pin(13), frequency)
motor04 = PWM(Pin(23), frequency)

class MotorControl:
    def __init__(self, motor1, motor2, motor3, motor4):
        self.motor1 = motor1
        self.motor2 = motor2
        self.motor3 = motor3
        self.motor4 = motor4      
    # function to set value of motor1
    def set_motor1(self, motor1Val):
        self.motor1 = motor1Val
        print("motor1 setter method called")
    def set_motor2(self, motor2Val):
        self.motor2 = motor2Val
        print("motor2 setter method called")
    def set_motor3(self, motor3Val):
        self.motor3 = motor3Val
        print("motor3 setter method called")
    def set_motor4(self, motor4Val):
        self.motor4 = motor4Val
        print("motor4 setter method called")
    
    def set_all_motors(self, allVal):
        self.motor1 = allVal
        self.motor2 = allVal
        self.motor3 = allVal
        self.motor4 = allVal
    
    def turn(self, leftVal, rightVal):
        self.motor1 = leftVal
        self.motor2 = leftVal
        self.motor3 = rightVal
        self.motor4 = rightVal

