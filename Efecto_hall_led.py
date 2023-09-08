import machine

# Configura el pin GPIO que deseas leer como salida
pin_numero = 25  # Reemplaza esto con el número de pin que estás utilizando
pin_salida = machine.Pin(pin_numero, machine.Pin.IN)
led = machine.Pin(2, machine.Pin.OUT)
while True:

    
    estado_pin = pin_salida.value()
    print("Estado del pin de salida:", estado_pin)
    if(estado_pin==1):
        led.on()
    else:
        led.off()
