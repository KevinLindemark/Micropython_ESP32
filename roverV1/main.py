# Complete project details at https://RandomNerdTutorials.com
# https://randomnerdtutorials.com/esp32-esp8266-pwm-micropython/
# https://randomnerdtutorials.com/esp32-esp8266-micropython-web-server/
from machine import Pin, PWM
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
                
control = MotorControl(0,0,0,0)

def web_page():
  if control.motor1 > 1:
    gpio_state="ON"
  else:
    gpio_state="OFF"
  
  html = """<html><head> <title>ESP Web Server</title> <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" href="data:,"> <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
  h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none; 
  border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 18px; margin: 2px; cursor: pointer;}
  .button2{ border: none; border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 18px; margin: 2px;
  cursor: pointer;background-color: #4286f4; display: flex; } .button2container{display: flex; width: 100%;height: 100px; align-items: center; justify-content: center;}
  </style></head><body> <h1>ESP Web Server</h1>
  <p>GPIO state: <strong>""" + gpio_state + """</strong></p><p><a href="/?speed=faster"><button class="button">+ForwardSpeed</button></a></p>
  <div class="button2container">
  <p><a href="/?left=turnLeft"><button class="button2">LEFT</button></a></p>
  <p><a href="/?stop=stopNow"><button class="button2">STOP!</button></a></p>
  <p><a href="/?right=turnRight"><button class="button2">RIGHT</button></a></p>
  </div>
  <p><a href="/?slow=slowDown"><button class="button button">SLOWER</button></a></p></body></html>"""
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

# stop all motors
motor01.duty(0)
motor02.duty(0)
motor03.duty(0)
motor04.duty(0)

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = str(request)
  print('Content = %s' % request)
  speed = request.find('/?speed=faster')
  slow = request.find('/?slow=slowDown')
  left = request.find('/?left=turnLeft')
  right = request.find('/?right=turnRight')
  stop = request.find('/?stop=stopNow')
  
  if speed == 6:
    print('FASTER')
    if control.motor1 >= 900:
        control.set_all_motors(1000)
        print("MAX SPEED")
    else:    
        control.set_all_motors(control.motor1 +200)
    motor01.duty(control.motor1)
    motor02.duty(control.motor2)
    motor03.duty(control.motor3)
    motor04.duty(control.motor4)
    print("motor1 val", control.motor1)
  if slow == 6:
    if control.motor1 <= 0:
        control.set_motor1(0)
        print("STOPPED")
    else:    
        control.set_all_motors(control.motor1 -200)
    motor01.duty(control.motor1)
    motor02.duty(control.motor2)
    motor03.duty(control.motor3)
    motor04.duty(control.motor4)
    print("motor1 val", control.motor1)
  if left == 6:
    print("TURN LEFT")
    control.turn(control.motor1 -200, control.motor3 + 200 )
    if control.motor1 <= 0:
        control.set_motor1(0)
        control.set_motor2(0)
    if control.motor3 >= 1000:
        control.set_motor3(1000)
        control.set_motor4(1000)
        print("MAX LEFT")
    motor01.duty(control.motor1)
    motor02.duty(control.motor2)
    motor03.duty(control.motor3)
    motor04.duty(control.motor4)
    
  
  if right == 6:
    print("TURN RIGHT")
    control.turn(control.motor1 +200, control.motor3 - 200 )
    if control.motor3 <= 0:
        control.set_motor3(0)
        control.set_motor4(0)
    if control.motor1 >= 1000:
        control.set_motor1(1000)
        control.set_motor2(1000)
        print("MAX RIGHT")
    motor01.duty(control.motor1)
    motor02.duty(control.motor2)
    motor03.duty(control.motor3)
    motor04.duty(control.motor4)
  if stop == 6:
    print("STOP!")
    control.set_all_motors(0)
    motor01.duty(control.motor1)
    motor02.duty(control.motor2)
    motor03.duty(control.motor3)
    motor04.duty(control.motor4)

  response = web_page()
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()
