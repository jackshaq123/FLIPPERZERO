# MicroPython starter: blinking LED and serial print
from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)

while True:
    led.value(1)
    print("heartbeat:on")
    sleep(0.5)
    led.value(0)
    print("heartbeat:off")
    sleep(0.5)
