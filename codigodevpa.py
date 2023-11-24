import machine
import utime
import math

# Configuración del sensor de efecto Hall
hall_sensor_pin = machine.Pin(14, machine.Pin.IN)

# Inicialización de variables para el sensor de efecto Hall
last_time_hall = None

def hall_sensor_handler(pin):
    global last_time_hall
    current_time = utime.ticks_ms()
    if last_time_hall is not None:
        interval = (current_time - last_time_hall) / 1000
        print("Intervalo entre toques (s):", interval)

        velocidad_angular_rad_s = 2 * math.pi / interval
        velocidad_km = (0.023 * velocidad_angular_rad_s) * 3.6
        print("Velocidad (km/h):", velocidad_km)

    last_time_hall = current_time

try:
    hall_sensor_pin.irq(trigger=machine.Pin.IRQ_FALLING, handler=hall_sensor_handler)

    # Configuración del sensor de pulsos
    mm_per_pulse = 0.173
    mm_total = 0

    def pulse_sensor_handler(pin):
        global mm_total
        mm_total += mm_per_pulse
        print(mm_total, "mm")

    pulse_sensor_pin = machine.Pin(12, machine.Pin.IN)
    pulse_sensor_pin.irq(trigger=machine.Pin.IRQ_RISING | machine.Pin.IRQ_FALLING, handler=pulse_sensor_handler)

    # Configuración de los sensores de dirección
    sensor_norte = machine.Pin(25, machine.Pin.IN)
    sensor_sur = machine.Pin(26, machine.Pin.IN)
    sensor_este = machine.Pin(27, machine.Pin.IN)
    sensor_oeste = machine.Pin(13, machine.Pin.IN)

    while True:
        # Manejo de los sensores de dirección
        norte = sensor_norte.value()
        sur = sensor_sur.value()
        este = sensor_este.value()
        oeste = sensor_oeste.value()

        if norte and este:
            print("Noreste")
        elif norte and oeste:
            print("Noroeste")
        elif sur and este:
            print("Sureste")
        elif sur and oeste:
            print("Suroeste")
        elif norte:
            print("Norte")
        elif sur:
            print("Sur")
        elif este:
            print("Este")
        elif oeste:
            print("Oeste")

        utime.sleep(0.1)  # Pequeña pausa para evitar repeticiones rápidas

except KeyboardInterrupt:
    hall_sensor_pin.irq(handler=None)
    pulse_sensor_pin.irq(handler=None)
    print("Programa detenido")

