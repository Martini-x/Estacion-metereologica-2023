import machine, network, time, urequests
from machine import Pin, I2C
from sh1106 import SH1106_I2C
import ahtx0
import BME280
import machine
import utime
import math

ssid = 'BA Escuela'
password = ''
url = "https://api.thingspeak.com/update?api_key=06BZMYMBYQIQ02XG"

red = network.WLAN(network.STA_IF)

red.active(True)
red.connect(ssid, password)

while red.isconnected() == False:
  pass

print('Conexión correcta')
print(red.ifconfig())

ultima_peticion = 0
intervalo_peticiones = 1

i2c = I2C(scl=Pin(22), sda=Pin(21), freq=400000)  # Configura el bus I2C en los mismos pines para ambos dispositivos.



sensor_pin = machine.Pin(36) 
# Initialize the ADC
adc = machine.ADC(sensor_pin)
# Configura el display OLED
oled = SH1106_I2C(128, 64, i2c)

# Direcciones I2C de los dispositivos
sensor_address = 0x38
oled_address=0x3C
BME280_I2CADDR = 0x76

hall_sensor_pin = Pin(14, Pin.IN)
last_time = None

def button_handler(pin):
    global last_time
    current_time = utime.ticks_ms()  # Registra la marca de tiempo actual
    if last_time is not None:
        interval = (current_time - last_time) / 1000  # Calcula el intervalo entre toques
        velocidad_angular_rad_s = 2 * math.pi / interval
        velocidad_km = (0.023 * velocidad_angular_rad_s) * 3.6
        mensaje_vel = "Vel: {:.2f} km".format(velocidad_km)
        oled.text(mensaje_vel, 0, 50)
        oled.show()
    last_time = current_time  # Actualiza la marca de tiempo
    oled.fill_rect(0, 50, 128, 10, 0)
    oled.show()
    
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
    mensaje_h = "Humidity: {:.1f} %".format(sensor.relative_humidity)
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
    try:
        button_pin = Pin(14, Pin.IN)  # Assuming you have a button connected to Pin 0
        button_pin.irq(trigger=Pin.IRQ_FALLING, handler=button_handler)

    except KeyboardInterrupt:
        button_pin.irq(handler=None)  # Detiene la interrupción al salir del programa
        print("Programa detenido")
        
