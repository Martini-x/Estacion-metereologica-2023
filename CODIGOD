from machine import Pin, I2C
from sh1106 import SH1106_I2C
import ahtx0
import BME280


# Configura el bus I2C
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


while True:
    uv_value = read_uv_intensity()
    voltage = uv_value/4095*3.3
    voltage_mV= voltage*1000
    # Leer datos del sensor (por ejemplo, 4 bytes)
    data_received = bytearray(4)
    
    # Configura la dirección I2C para el sensor

    i2c.readfrom_into(sensor_address, data_received)
    i2c.readfrom_into(BME280_I2CADDR, data_received)
    # Procesa los datos recibidos según la hoja de datos del sensor
    # Supongamos que los datos son una temperatura en grados Celsius
    sensor = ahtx0.AHT10(i2c)
    bme = BME280.BME280(i2c=i2c)
    # Borra el contenido anterior del display
    oled.fill(0)
    
    # Muestra los datos del sensor en el display OLED
    mensaje_t = "Temp1: {:.2f} C".format(sensor.temperature)
    oled.text(mensaje_t, 0, 0)
    mensaje_t2 = "Temp2: {:.5s} C".format(bme.temperature)
    oled.text(mensaje_t2, 0, 10)
    mensaje_h = "Humidity: {:.1f} %".format(sensor.relative_humidity)
    oled.text(mensaje_h, 0, 20)
    mensaje_p = "Pres: {:.6s} hPa".format(bme.pressure)
    oled.text(mensaje_p, 0, 30)
    mensaje_UV = "UV: {:.6s} ".format(uv_value)
    oled.text(mensaje_UV, 0, 40)
    # Actualiza el display
    oled.show()

