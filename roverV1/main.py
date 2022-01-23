# Complete project details at https://RandomNerdTutorials.com
# https://randomnerdtutorials.com/esp32-esp8266-pwm-micropython/
# https://randomnerdtutorials.com/esp32-esp8266-micropython-web-server/
from time import sleep
import motor
import servo
control = motor.MotorControl(0,0,0,0)
servoControl = servo.ServoControl(77,77,40)

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
  </style></head><body> <h1>Rover - ESP32 Web Server</h1>
  <h2>ARM CONTROL!</h2>
  <p><a href="/?servoUp=up"><button class="button">UP!</button></a></p>
  <div class="button2container">
  <p><a href="/?servoLeft=left"><button class="button2">LEFT</button></a></p>
  <p><a href="/?grabOpen=open"><button class="button2">GRAB!</button></a></p>
  <p><a href="/?grabClose=close"><button class="button2">DROP!</button></a></p>
  <p><a href="/?servoRight=right"><button class="button2">RIGHT</button></a></p>
  </div>
  <p><a href="/?servoDown=down"><button class="button button">DOWN!</button></a></p>
  <h2> MOTOR CONTROL!</h2>
  <p>Motor state: <strong>""" + gpio_state + """</strong></p> <p><a href="/?speed=faster"><button class="button">+ForwardSpeed</button></a></p>
  <div class="button2container">
  <p><a href="/?left=turnLeft"><button class="button2">LEFT</button></a></p>
  <p><a href="/?stop=stopNow"><button class="button2">STOP!</button></a></p>
  <p><a href="/?right=turnRight"><button class="button2">RIGHT</button></a></p>
  </div>
  <p><a href="/?slow=slowDown"><button class="button button">SLOWER</button></a></p>
  </body></html>"""
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

# stop all motors
print("Motors OFF!")
motor.motor01.duty(0)
motor.motor02.duty(0)
motor.motor03.duty(0)
motor.motor04.duty(0)

print("Servo in start position!")
for i in range(10):
    sleep(0.1)
    servo.servoAxisX.duty(77)

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
  # SERVO
  servoLeft = request.find('/?servoLeft=left')
  servoRight = request.find('/?servoRight=right')
  servoUp = request.find('/?servoUp=up')
  servoDown = request.find('/?servoDown=down')
  grabOpen = request.find('/?grabOpen=open')
  grabClose = request.find('/?grabClose=close')
  
  if speed == 6:
    print('FASTER')
    if control.motor1 >= 900:
        control.set_all_motors(1000)
        print("MAX SPEED")
    else:    
        control.set_all_motors(control.motor1 +200)
    motor.motor01.duty(control.motor1)
    motor.motor02.duty(control.motor2)
    motor.motor03.duty(control.motor3)
    motor.motor04.duty(control.motor4)
    print("motor1 val", control.motor1)
  if slow == 6:
    if control.motor1 <= 0:
        control.set_motor1(0)
        print("STOPPED")
    else:    
        control.set_all_motors(control.motor1 -200)
    motor.motor01.duty(control.motor1)
    motor.motor02.duty(control.motor2)
    motor.motor03.duty(control.motor3)
    motor.motor04.duty(control.motor4)
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
    motor.motor01.duty(control.motor1)
    motor.motor02.duty(control.motor2)
    motor.motor03.duty(control.motor3)
    motor.motor04.duty(control.motor4)
    
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
    motor.motor01.duty(control.motor1)
    motor.motor02.duty(control.motor2)
    motor.motor03.duty(control.motor3)
    motor.motor04.duty(control.motor4)
  if stop == 6:
    print("STOP!")
    control.set_all_motors(0)
    motor.motor01.duty(control.motor1)
    motor.motor02.duty(control.motor2)
    motor.motor03.duty(control.motor3)
    motor.motor04.duty(control.motor4)
# SERVO  
  if servoLeft ==6:
      print("SERVO LEFT!")
      servoControl.set_servoX(servoControl.servoX + 20)
      servo.servoAxisX.duty(servoControl.servoX)
  if servoRight ==6:
      print("SERVO RIGHT!")
      servoControl.set_servoX(servoControl.servoX - 20)
      servo.servoAxisX.duty(servoControl.servoX)
  if servoUp == 6:
      pass
  if servoDown == 6:
      pass
  if grabOpen == 6:
      pass
  
  if grabClose == 6:
      pass
      
  response = web_page()
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()
