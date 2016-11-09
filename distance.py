from gpiozero import DistanceSensor, LED
from signal import pause
from time import sleep

sensor = DistanceSensor(echo=17, trigger=4, max_distance=1, threshold_distance=0.1)
led = LED(16)

sensor.when_in_range = led.on
sensor.when_out_of_range = led.off

pause()

