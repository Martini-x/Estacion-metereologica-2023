import machine

sensor = machine.Pin(14, machine.Pin.IN)
mmPerPulse = 0.173
mmTotal = 0;
sensor = sensor.value();
previous_state = 0;

while True:
    if sensor != previous_state:
        mmTotali = mmTotali + mmPerPulse
  previous_state = sensor;


