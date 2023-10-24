import machine
import utime

sensor_norte = machine.Pin(25, machine.Pin.IN)
sensor_sur = machine.Pin(26, machine.Pin.IN)
sensor_este = machine.Pin(27, machine.Pin.IN)
sensor_oeste = machine.Pin(14, machine.Pin.IN)

while True:
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

