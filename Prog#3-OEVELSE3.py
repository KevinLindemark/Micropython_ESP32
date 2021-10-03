from machine import Pin, PWM
from time import sleep
# variabler til frquency og startcycle
frequency = 5000
# Værdien sættes til 1023 som vil være slukket på vores LED
start_cycle = 1023

# initialisere PWM objekter sat til pins på RGB-lED komponentet
# ligeledes er det sat til en frqueny på 5000 og startcycle på 1023 (SLUKKET)
r = PWM(Pin(18), frequency, start_cycle)
g = PWM(Pin(5), frequency, start_cycle)
b = PWM(Pin(19), frequency, start_cycle)
# Starter uendeligt while loop
while True:
    # printer streng og venter 1 sekund med sleep funktionen
    print("ØVELSE 3.2")
    sleep(1)
    # starter for loop med en range fra 0 - 1024 (-1)
    for duty_cycle in range(1024):
        # bruger duty metoden på r (PWM objekt til rød LED pin)
        # duty() metoden sætter duty til at være duty_cycle som vil være
        # mellem 0 og gå mod 1023 når for loopet gennemløbes
        # det gør at den røde LED starter med at have max lysintensitet og
        # derfter skrues ned til slukket
        r.duty(duty_cycle)
        # Printer en streng med øvelses nr og loop nr. samt farven r
        # efter strengen prints duty cycle så man se den og lysintensiteten som vil
        # være det samme
        print("3.2: 1 r ", duty_cycle)
        sleep(0.005)
    # kører et nyt for loop der gør det samme som sidste for loop
    # men på den grønne LED
    for duty_cycle in range(1024):
        g.duty(duty_cycle)
        print("3.2: 2 g ", duty_cycle)
        sleep(0.005)
    # kører et nyt for loop der gør det samme som sidste for loop
    # men på den blå LED
    for duty_cycle in range(1024):
        b.duty(duty_cycle)
        print("3.2: 3 b ", duty_cycle)
        sleep(0.005)
    # kører et nyt for loop der gør det samme som sidste for loop
    # men på den blå LED og den røde LED (nu blandes de to farver)
    for duty_cycle in range(1024):
        b.duty(duty_cycle)
        r.duty(duty_cycle)
        print("3.2: 4 b+r ", duty_cycle)
        sleep(0.005)
    # kører et nyt for loop der gør det samme som sidste for loop
    # men på den grønne LED og den røde LED (nu blandes de to farver)
    for duty_cycle in range(1024):
        g.duty(duty_cycle)
        r.duty(duty_cycle)
        print("3.2: 5 g+r ", duty_cycle)
        sleep(0.005)
    # kører et nyt for loop der gør det samme som sidste for loop
    # men på den blå LED og den grønne LED (nu blandes de to farver)
    for duty_cycle in range(1024):
        b.duty(duty_cycle)
        g.duty(duty_cycle)
        print("3.2: 6 b+g ", duty_cycle)
        sleep(0.005)
    # kører et nyt for loop der gør det samme som sidste for loop
    # men på den røde, grønne og blå LED (nu blandes alle farverne)
    for duty_cycle in range(1024):
        r.duty(duty_cycle)
        g.duty(duty_cycle)
        b.duty(duty_cycle)
        print("3.2: 7 r+g+b ", duty_cycle)
        sleep(0.005)
    # Printer strengen "ØVELSE 3.3"
    print("ØVELSE 3.3")
    sleep(1)
    # starter nyt for loop med range der tæller ned fra 1024 til 0 med -1 per
    # iteration i for loopet
    for duty_cycle in range(1024, 0, -1):
        # Her sættes blå og grøn led til at være slukket
        # Så vi er sikre på ingen anden LED end den røde tændes
        # Det er for at undgå at farvene blandes forkert da de nu slutter med at
        # være tændte når det næste for loop eksekveres
        b.duty(1023)
        g.duty(1023)
        # nu vil duty_cycle variablen starte på 1023 (Slukket)
        # og skrue op for den røde LED's lysintensitet med en inkrementering på -1
        # per gennemløbning af for loopet
        r.duty(duty_cycle)
        print("3.3: 1 r ", duty_cycle)
        sleep(0.005)
    # samme som sidste for loop men slukker blå og rød og tænder grøn LED
    for duty_cycle in range(1024, 0, -1):
        b.duty(1023)
        r.duty(1023)
        g.duty(duty_cycle)
        print("3.3: 2 g ", duty_cycle)
        sleep(0.005)
    # samme som sidste for loop men slukker rød og grøn og tænder blå LED
    for duty_cycle in range(1024, 0, -1):
        r.duty(1023)
        g.duty(1023)
        b.duty(duty_cycle)
        print("3.3: 3 b ", duty_cycle)
        sleep(0.005)
    # samme som sidste for loop men slukker grøn og tænder blå og rød LED
    for duty_cycle in range(1024, 0, -1):
        g.duty(1023)
        b.duty(duty_cycle)
        r.duty(duty_cycle)
        print("3.3: 4 b+r ", duty_cycle)
        sleep(0.005)
    # samme som sidste for loop men slukker blå og tænder grøn og rød LED
    for duty_cycle in range(1024, 0, -1):
        b.duty(1023)
        g.duty(duty_cycle)
        r.duty(duty_cycle)
        print("3.3: 5 g+r ", duty_cycle)
        sleep(0.005)
    # samme som sidste for loop men slukker rød og tænder blå og grøn LED
    for duty_cycle in range(1024, 0, -1):
        r.duty(1023)
        b.duty(duty_cycle)
        g.duty(duty_cycle)
        print("3.3: 6 b+g ", duty_cycle)
        sleep(0.005)
    # Tænder alle LED'er og slukker dem igen med en if sætning
    for duty_cycle in range(1024, 0, -1):
        r.duty(duty_cycle)
        g.duty(duty_cycle)
        b.duty(duty_cycle)
        print("3.3: 7 r+g+b ", duty_cycle)
        sleep(0.005)
        # Tjekker om duty_cycle er 1 køre kodeblokken inde i når den er sand
        if duty_cycle == 1:
            print("Turn OFF all LED's")
            sleep(2)
            # slukker alle LED'erne inden næste for loops startes
            r.duty(1023)
            g.duty(1023)
            b.duty(1023)
    print("ØVELSE 3.4")
    sleep(1)
    # starter for loop der med range der starter fra 0 og går mod 1024
    # og inkrementere med 10 per gennemløbning
    for duty_cycle in range(0, 1024, 10):
        # slukker blå og grøn
        b.duty(1023)
        g.duty(1023)
        # skruer ned for den røde LEDS lysintensitet
        r.duty(duty_cycle)
        print("3.4: 1 r ", duty_cycle)
        sleep(0.005)
    # samme som sidste for loop men ny farve
    for duty_cycle in range(0, 1024, 10):
        b.duty(1023)
        r.duty(1023)
        g.duty(duty_cycle)
        print("3.4: 2 g ", duty_cycle)
        sleep(0.005)
    # samme som sidste for loop men ny farve
    for duty_cycle in range(0, 1024, 10):
        r.duty(1023)
        g.duty(1023)
        b.duty(duty_cycle)
        print("3.4: 3 b ", duty_cycle)
        sleep(0.005)
    # samme som sidste for loop men ny farve
    for duty_cycle in range(0, 1024, 10):
        g.duty(1023)
        b.duty(duty_cycle)
        r.duty(duty_cycle)
        print("3.4: 4 b+r ", duty_cycle)
        sleep(0.005)
    # samme som sidste for loop men ny farve
    for duty_cycle in range(0, 1024, 10):
        b.duty(1023)
        g.duty(duty_cycle)
        r.duty(duty_cycle)
        print("3.4: 5 g+r ", duty_cycle)
        sleep(0.005)
    # samme som sidste for loop men ny farve
    for duty_cycle in range(0, 1024, 10):
        r.duty(1023)
        b.duty(duty_cycle)
        g.duty(duty_cycle)
        print("3.4: 6 b+g ", duty_cycle)
        sleep(0.005)
    # samme som sidste for loop men ny farve
    for duty_cycle in range(0, 1024, 10):
        r.duty(duty_cycle)
        g.duty(duty_cycle)
        b.duty(duty_cycle)
        print("3.4: 7 r+g+b ", duty_cycle)
        sleep(0.005)
        # Slukker alle LED'er når loopet når 1020
        if duty_cycle == 1020:
            print("Turn OFF all LED's")
            r.duty(1023)
            g.duty(1023)
            b.duty(1023)
            sleep(2)

    print("Øvelse 3.5")
    sleep(1)
    # Vi er nu nået til while loopets ende og der printes en besked
    # Efter den sidste linje starter while loopet forfra
    print("Restarting while loop")
    sleep(1)
