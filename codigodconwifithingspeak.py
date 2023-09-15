import machine, network, time, urequests
from machine import Pin, I2C
import BME280

ssid = 'Sexofono'
password = '123456789'
url = "https://api.thingspeak.com/update?api_key=PGS7UCLWDVV3IIVU"

red = network.WLAN(network.STA_IF)

red.active(True)
red.connect(ssid, password)

while red.isconnected() == False:
  pass

print('Conexión correcta')
print(red.ifconfig())

ultima_peticion = 0
intervalo_peticiones = 1

i2c = I2C(scl=Pin(22), sda=Pin(21), freq=400000)
bme = BME280.BME280(i2c=i2c)

def reconectar():
    print('Fallo de conexión. Reconectando...')
    time.sleep(10)
    machine.reset()

while True:
  
    try:
        if (time.time() - ultima_peticion) > intervalo_peticiones:
            respuesta = urequests.get(url + "&field1=" + str(bme.temperature) + "&field2=" + str(bme.pressure))
            print ("Respuesta: " + str(respuesta.status_code))
            respuesta.close ()
            ultima_peticion = time.time()
    except OSError as e:
        reconectar()
        
