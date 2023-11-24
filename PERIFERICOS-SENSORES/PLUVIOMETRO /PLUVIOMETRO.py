import machine

# Declaración de variables
mmPerPulse = 0.173
mmTotal = 0

# Función de manejo de interrupción
def handle_interrupt(pin):
    global mmTotal
    mmTotal += mmPerPulse
    print(mmTotal, "mm")

# Configurar el pin del sensor como entrada para la interrupción
sensor = machine.Pin(12, machine.Pin.IN)

# Configurar la interrupción en el flanco de subida del pin
sensor.irq(trigger=machine.Pin.IRQ_RISING | machine.Pin.IRQ_FALLING, handler=handle_interrupt)

# Bucle principal
while True:
    pass

