# Importere library til at forbinde til adafruit.io
import mqttJarvisPubSub
lib = mqttJarvisPubSub

while True:
    try:
        # lib.m vil indholde strengen som indtastes i feltet "skriv til Jarvis"
        # Hvis strengen er identisk med "hej Jarvis" køres koden i if sætningen
        if lib.m == "hej Jarvis":
            # Strengen som sættes i msg="din streng her" vil komme i adafruit som "svar fra Jarvis"
            lib.client.publish(topic=lib.mqtt_pub_feedname, msg="Hej Master")
            # Tøm strengen igen, ellers vil den køre i en uendelighed og crashe :)
            lib.m = ""

        # Tjekker for nye beskeder
        lib.client.check_msg()
    # Stopper programmet når der trykkes Ctrl + c
    except KeyboardInterrupt:
        print('Ctrl-C pressed...exiting')
        lib.client.disconnect()
        lib.sys.exit()
