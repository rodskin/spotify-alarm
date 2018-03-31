from gpiozero import LED
import gpiopins as GPIO
led = LED(25)
led.blink()
