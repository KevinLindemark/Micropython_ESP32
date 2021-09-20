# Importere Pin og ADC klasserne fra machine modulet
from machine import Pin, ADC
# Importere sleep_ms fra time modulet
from time import sleep

# Følgende er til Lyskryds komponentet:
# Instantierer et Pin objekt med navnet r (rød) på pin 5, sat som OUTput, og værdien 0 (slukket)
r = Pin(5, Pin.OUT, value=0)
# Instantierer et Pin objekt med navnet g (grøn) på pin 16, sat som OUTput, og værdien 0 (slukket)
g = Pin(16, Pin.OUT, value=0)
# Instantierer et Pin objekt med navnet y (yellow) på pin 17, sat som OUTput, og værdien 0 (slukket)
y = Pin(17, Pin.OUT, value=0)

# Følgende er til potentiometer komponentet:
# Instantierer et ADC objekt med navnet pot på pin 32
adc_pot = ADC(Pin(32))
# Attenuationen sættes til 11DB med maximum tilladt spænding på 3.6 volt
adc_pot.atten(ADC.ATTN_11DB)
# Opløsningen sættes til 12BIT (4096)
adc_pot.width(ADC.WIDTH_12BIT)

# button instantieres som et Pin objekt på pin 12 og tager et digitalt input da værdierne 0 og 1 er tilstrækkelige
# da knappen alligevel kun har 2 mulige stadier (trykket eller ikke trykket)
button = Pin(12, Pin.IN)

# Her startes en uendelig while løkke som altid er True
while True:
    # Alt der er indrykket til dette niveau køres igen og igen i samme kodeblok

    # pot_val variablen sættes til at indeholde ADC værdien fra pot ved hjælp af read() metoden fra ADC klassen
    pot_val = adc_pot.read()
    # printer værdien af pot_val
    print(pot_val)

    # button_val variablen får værdien som knappen har
    button_val = button.value()

    # if sætning der er sand hvis pot_val er mindre end 500
    if pot_val < 500:
        # sætter grøn og gul LED til 0 (slukket)
        g.value(0)
        y.value(0)
        # sætter rød og LED til at skifte til dens modsatte værdi (fra tændt til slukket eller omvendt)
        r.value(not r.value())
        sleep(0.1)
    # if sætning der er sand hvis pot_val er større end 1500 og (and) mindre end 3000
    if pot_val > 1500 and pot_val < 3000:
        # sætter rød og grøn LED til 0 (slukket)
        r.value(0)
        g.value(0)
        # sætter rød og LED til at skifte til dens modsatte værdi (fra tændt til slukket eller omvendt)
        y.value(not y.value())
        # venter 0.1 sekund
        sleep(0.1)
    # if sætning der er sand hvis pot_val er større end 3000
    if pot_val > 3000:
        # sætter rød og gul LED til 0 (slukket)
        r.value(0)
        y.value(0)
        # sætter grøn og LED til at skifte til dens modsatte værdi (fra tændt til slukket eller omvendt)
        g.value(not g.value())
        # venter 0.1 sekund
        sleep(0.1)

     # if sætning der er sand hvis button_val er mindre end 1
    if button_val < 1:
       #slukker alle LED'er undtagen rød
       r.value(1)
       y.value(0)
       g.value(0)
       # venter 1.1 sekund
       sleep(1.1)

       #slukker alle LED'er undtagen gul
       r.value(0)
       y.value(1)
       g.value(0)
       sleep(1.1)

       #slukker alle LED'er undtagen grøn
       r.value(0)
       y.value(0)
       g.value(1)
       # venter 1.1 sekund
       sleep(1.1)
    # hvis button_val if sætningens betingelse er falsk så gøre dette
    else:
        # sluk alle LED'er
        r.value(0)
        g.value(0)
        y.value(0)

    # venter 0.1 sekund mellem hver omgang while løkken køres
    sleep(0.1)



