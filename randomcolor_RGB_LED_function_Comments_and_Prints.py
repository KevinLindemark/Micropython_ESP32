#Importere Pin og PWM klasserne fra machine modulet
from machine import Pin, PWM
#Importere sleep klasserne fra time modulet
from time import sleep
#Importere randint funktionen fra random modulet
from random import randint
# Initialisere PWM objekter på pins
r = PWM(Pin(18))
g = PWM(Pin(5))
b = PWM(Pin(19))
# Definere en funktion kalde newColor
def newColor():
    #Starter for loop med en range fra 0 til 11 -1
    for i in range(11):
        print("New color!")
        # Laver variablen randomColor som får returneret værdi
        # mellm 0 og 1032 fra randint funktionen
        randomColor = randint(0, 1023)
        #printer strengen red og værdien i randomColor variablen
        print("red", randomColor)
        # Sætter rød LED's duty til den random color som variablen holder
        r.duty(randomColor)
        # Tildeler et nyt random tal til randomColor variablen
        randomColor = randint(0, 1023)
        print("green", randomColor)
        g.duty(randomColor)
        randomColor = randint(0, 1023)
        print("blue", randomColor)
        b.duty(randomColor)
        sleep(0.2)
# Kalder funktionen newColor og eksekvere koden defineret i dens kodeblok
#Prøv at kør funktionen i REPL ved at indtaste newColor()
newColor()
