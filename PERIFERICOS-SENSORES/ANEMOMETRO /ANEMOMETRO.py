from machine import Pin
import utime
import math

# Configura el pin del sensor de efecto Hall
hall_sensor_pin = Pin(14, Pin.IN)

# Inicializa variables
last_time = None  # Inicializa la variable para el primer toque

def button_handler(pin):
    global last_time
    current_time = utime.ticks_ms()  # Registra la marca de tiempo actual
    if last_time is not None:
        interval = (current_time - last_time) / 1000  # Calcula el intervalo entre toques
        print("Intervalo entre toques (s):", interval)

        # Calcula la velocidad angular en radianes por segundo
        velocidad_angular_rad_s = 2 * math.pi / interval
        velocidad_km = (0.023 * velocidad_angular_rad_s) * 3.6
        print("Velocidad (km/h):", velocidad_km)

    last_time = current_time  # Actualiza la marca de tiempo

try:
    button_pin = Pin(14, Pin.IN)  # Assuming you have a button connected to Pin 0
    button_pin.irq(trigger=Pin.IRQ_FALLING, handler=button_handler)

    while True:
        utime.sleep(1)  # Espera 1 segundo

except KeyboardInterrupt:
    button_pin.irq(handler=None)  # Detiene la interrupción al salir del programa
    print("Programa detenido")

