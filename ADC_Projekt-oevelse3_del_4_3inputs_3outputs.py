# Importere Pin og ADC klasserne fra machine modulet
from machine import Pin, ADC

# Importere sleep_ms fra time modulet
from time import sleep_ms

# Følgende er til RGB komponentet:
# Instantierer et Pin objekt med navnet r (rød) på pin 18, sat som OUTput, og værdien 1 (slukket, da den er omvendt)
r = Pin(18, Pin.OUT, value=1)
# Instantierer et Pin objekt med navnet g (grøn) på pin 19, sat som OUTput, og værdien 1 (slukket, da den er omvendt)
g = Pin(19, Pin.OUT, value=1)
# Instantierer et Pin objekt med navnet b (blå) på pin 5, sat som OUTput, og værdien 1 (slukket, da den er omvendt)
b = Pin(5, Pin.OUT, value=1)

# Følgende er til vibrator komponentet:
# Instantierer et Pin objekt med navnet vibrate på pin 16, sat som OUTput, og værdien 0
vibrate = Pin(16, Pin.OUT, value=0)

# Følgende er til buzzer komponentet:
# Instantierer et Pin objekt med navnet buzz på pin 4, sat som OUTput, og værdien 0
buzz = Pin(4, Pin.OUT, value=0)

# Følgende er til temperatursensor komponentet:
# Instantierer et ADC objekt med navnet temp på pin 36
temp = ADC(Pin(36))
temp.atten(ADC.ATTN_11DB)  # Attenuationen sættes til 11DB med maximum tilladt spænding på 3.6 volt
temp.width(ADC.WIDTH_12BIT)  # Opløsningen sættes til 12BIT (4096)

# Følgende er til Light Dependant Resistor (LDR) komponentet:
# Instantierer et ADC objekt med navnet ldr på pin 32
ldr = ADC(Pin(32))
ldr.atten(ADC.ATTN_11DB)  # Attenuationen sættes til 11DB med maximum tilladt spænding på 3.6 volt
ldr.width(ADC.WIDTH_12BIT)  # Opløsningen sættes til 12BIT (4096)

# Følgende er til potentiometer komponentet:
# Instantierer et ADC objekt med navnet pot på pin 33
pot = ADC(Pin(33))
pot.atten(ADC.ATTN_11DB)  # Attenuationen sættes til 11DB med maximum tilladt spænding på 3.6 volt
pot.width(ADC.WIDTH_12BIT)  # Opløsningen sættes til 12BIT (4096

# Her startes en uendelig while løkke som altid er True
while True:
    # Alt der er indrykket til dette niveau køres igen og igen i samme kodeblok

    # pot_val variablen sættes til at indeholde ADC værdien fra pot ved hjælp af read() metoden fra ADC klassen
    pot_val = pot.read()
    # temp_val variablen sættes til at indeholde ADC værdien fra temp ved hjælp af read() metoden fra ADC klassen
    temp_val = temp.read()
    # ldr_val variablen sættes til at indeholde ADC værdien fra ldr ved hjælp af read() metoden fra ADC klassen
    ldr_val = ldr.read()

    # printer tekst strenge det som er i "" efterfulgt af ADC værdierne fra variablerne der holder dem
    print("LDR værdi: ", ldr_val, "Temperatur værdi: ", temp_val, "Potentiometer værdi: ", pot_val)

    # if sætning der er sand hvis ldr_val er mindre end 1500
    if ldr_val < 1500:
        # sætter buzz til 1 (tændt) hvis betingelsen fra if sætningen er sand (True)
        buzz.value(1)
    # Ellers så gøres dette i stedet for:
    else:
        # Hvis if sætningens betingelse er falsk (False) køres dette der sætter buzz til 0 (slukket)
        buzz.value(0)
    # if sætning der er sand hvis temp_val er større end 1400
    if temp_val > 1400:
        # sætter vibrate til 1 (tændt) hvis betingelsen fra if sætningen er sand (True)
        vibrate.value(1)
    # Ellers så gøres dette i stedet for:
    else:
        # Hvis if sætningens betingelse er falsk (False) køres dette der sætter vibrate til 0 (slukket)
        vibrate.value(0)
    # if sætning der er sand hvis pot_val er større end 2000
    if pot_val > 2000:
        # sætter r (rød) LED til 0 (tændt) hvis betingelsen fra if sætningen er sand (True)
        r.value(0)
    # Ellers så gøres dette i stedet for:
    else:
        # Hvis if sætningens betingelse er falsk (False) køres dette der sætter alle tre LED'er til 1 (slukket)
        r.value(1)
        g.value(1)
        b.value(1)
    # når alle ovenstående handlinger er eksekveret køres sleep_ms funktionen med parametret 100 som venter 100 milisekunder
    sleep_ms(100)
