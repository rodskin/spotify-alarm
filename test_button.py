#!/usr/bin/python3
# encoding: utf-8

from gpiozero import Button


button = Button(23, False)
i = 0

while True:
	if(button.is_pressed):
                print("Button 1 pressed " + str(i))
                i += 1
GPIO.cleanup()
