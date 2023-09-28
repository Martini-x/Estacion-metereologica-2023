import machine, network, time, urequests
from machine import Pin, I2C
from sh1106 import SH1106_I2C
import ahtx0
import BME280
import machine
import time

ssid = 'Sexofono'
password = '1234567891011'
url = "https://api.thingspeak.com/update?api_key=06BZMYMBYQIQ02XG"

red = network.WLAN(network.STA_IF)

red.active(True)
red.connect(ssid, password)

while red.isconnected() == False:
  pass

print('Conexión correcta')
print(red.ifconfig())

ultima_peticion = 0
intervalo_peticiones = 3

i2c = I2C(scl=Pin(22), sda=Pin(21), freq=400000)  # Configura el bus I2C en los mismos pines para ambos dispositivos.
# Define the analog pin connected to the sensor output

sensor_pin = machine.Pin(36) 
# Initialize the ADC
adc = machine.ADC(sensor_pin)
# Configura el display OLED
oled = SH1106_I2C(128, 64, i2c)

# Direcciones I2C de los dispositivos
sensor_address = 0x38
oled_address=0x3C
BME280_I2CADDR = 0x76

def read_uv_intensity():
    uv_values = []
    for _ in range(10):  # Take 10 readings and average them
        uv_values.append(adc.read())
        time.sleep_ms(10)  # Wait for 10 milliseconds between readings
    return sum(uv_values) / len(uv_values)  # Return the average

def Escala_UV(voltage_mV):
    if(voltage_mV<50):
        Escala = 0
    elif(voltage_mV>=50 and voltage_mV<227):
        Escala = 1
    elif(voltage_mV>=227 and voltage_mV<318):
        Escala = 2
    elif(voltage_mV>=318 and voltage_mV<408):
        Escala = 3
    elif(voltage_mV>=408 and voltage_mV<503):
        Escala = 4
    elif(voltage_mV>=503 and voltage_mV<606):
        Escala = 5
    elif(voltage_mV>=606 and voltage_mV<696):
        Escala = 6
    elif(voltage_mV>=696 and voltage_mV<795):
        Escala = 7
    elif(voltage_mV>=795 and voltage_mV<881):
        Escala = 8
    elif(voltage_mV>=881 and voltage_mV<976):
        Escala = 9
    elif(voltage_mV>=976 and voltage_mV<1079):
        Escala = 10
    elif(voltage_mV>=1079):
        Escala = 11
    return Escala

def reconectar():
    print('Fallo de conexión. Reconectando...')
    time.sleep(10)
    machine.reset()

while True:
    uv_value = read_uv_intensity()
    voltage = uv_value/4095*3.3
    voltage_mV= voltage*1000
    # Leer datos del sensor (por ejemplo, 4 bytes)
    data_received_sensor = bytearray(4)
    data_received_bme = bytearray(4)
    # Configura la dirección I2C para el sensor

    i2c.readfrom_into(sensor_address, data_received_sensor)
    i2c.readfrom_into(BME280_I2CADDR, data_received_bme)
    # Procesa los datos recibidos según la hoja de datos del sensor
    # Supongamos que los datos son una temperatura en grados Celsius
    sensor = ahtx0.AHT10(i2c)
    bme = BME280.BME280(i2c=i2c)
    # Borra el contenido anterior del display
    oled.fill(0)
    

    # Muestra los datos del sensor en el display OLED
    mensaje_t = "Temp: {:.2f} C".format(sensor.temperature)
    oled.text(mensaje_t, 0, 0)
    mensaje_h = "Humidity: {:.2f} %".format(sensor.relative_humidity)
    oled.text(mensaje_h, 0, 10)
    mensaje_p = "Pres: {:.6s} hPa".format(bme.pressure)
    oled.text(mensaje_p, 0, 20)
    mensaje_UV = "UV: {:.0f} ".format(uv_value)
    oled.text(mensaje_UV, 0, 30)
    mensaje_Escala_UV = "Escala UV: {:.0f} ".format(Escala_UV(voltage_mV))
    oled.text(mensaje_Escala_UV, 0, 40)
    # Actualiza el display
    oled.show()
    try:
        if (time.time() - ultima_peticion) > intervalo_peticiones:
            respuesta = urequests.get(url + "&field1=" + str(sensor.temperature) + "&field2=" + str(sensor.relative_humidity) + "&field3=" + str(bme.pressure) + "&field4=" + str(uv_value) + "&field5=" + str(Escala_UV(voltage_mV)))
            print ("Respuesta: " + str(respuesta.status_code))
            respuesta.close ()
            ultima_peticion = time.time()
    except OSError as e:
        reconectar()
        
