#!/usr/bin/env python
# encoding: utf-8

import etc.config
import sys
import os
import gtts
import datetime
import time
try:
	import RPi.GPIO as GPIO
except ImportError:
	import GPIOmock as GPIO
	print('TESTING')

GPIO.setmode(GPIO.BCM)
GPIO.setup(etc.config.pin_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(etc.config.pin_led, GPIO.OUT)   # Set pin mode as output
#p = GPIO.PWM(etc.config.pin_led, 1000)	 # set Frequece to 1KHz

def readTime ():
	GPIO.output(etc.config.pin_led, GPIO.HIGH)
	date = datetime.datetime.now()
	current_time = "Il est " + str(date.hour) + 'h' + str(date.minute)
	tts = gtts.gTTS(text=current_time, lang=etc.config.lang)
	tts.save("tmp/time.mp3")
	os.system('mpg123 tmp/time.mp3')
	return
def playPlaylist () :
	stopPlaylist()
	os.system('mpc add spotify:user:icelandairwaves:playlist:3dNCFy3Q9d6LtGZLWT0c2O')
	os.system('mpc play')
	#ledBreathe()
	return
def stopPlaylist () :
	os.system('mpc clear')
	return
def snooze():
	GPIO.output(etc.config.pin_led, GPIO.LOW)
	stopPlaylist()
	time.sleep(etc.config.time_snooze)
	readTime()
	playPlaylist()
	return
def ledBreathe () :
	for i in range(0, 5):
		for dc in range(0, 101, 5):   # Increase duty cycle: 0~100
			p.ChangeDutyCycle(dc)	 # Change duty cycle
			time.sleep(0.05)
		time.sleep(1)
		for dc in range(100, -1, -5): # Decrease duty cycle: 100~0
			p.ChangeDutyCycle(dc)
			time.sleep(0.05)
		time.sleep(1)
	return
def stopScript () :
	print("Long Press")
	stopPlaylist()
	os.system('mpg123 tmp/stopping.mp3')
	i = 1
	for i in range(0, 3):
		GPIO.output(etc.config.pin_led, GPIO.LOW)
		time.sleep(0.5)
		GPIO.output(etc.config.pin_led, GPIO.HIGH)
		time.sleep(0.5)
	GPIO.output(etc.config.pin_led, GPIO.LOW)
	sys.exit()
def load () :
	GPIO.output(etc.config.pin_led, GPIO.LOW)
	#p.start(0)
	stopPlaylist()
	os.system('amixer set Master ' + str(etc.config.volume_music) + '%')
	os.system('mpc random 1')
	os.system('mpc volume 100')
	return

load()

readTime()
playPlaylist()


#GPIO.add_event_detect(etc.config.pin_button, GPIO.RISING, callback=buttonPress, bouncetime=button_bounce_time)

while True:
	GPIO.wait_for_edge(etc.config.pin_button, GPIO.FALLING)
	print('Pressed')
	start = time.time()
	time.sleep(0.2)

	while GPIO.input(etc.config.pin_button) == GPIO.LOW:
		time.sleep(0.01)
		if ((time.time() - start) > 3 ) :
			print("Long Press > 3")
			stopScript()
	length = time.time() - start

	if length <= 3:
		print("Short Press")
		snooze()

GPIO.cleanup()		   # clean up GPIO on normal exit
