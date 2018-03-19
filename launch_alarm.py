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

def readTime ():
	date = datetime.datetime.now()
	current_time = "Il est " + str(date.hour) + ':' + str(date.minute)
	tts = gtts.gTTS(text=current_time, lang=etc.config.lang)
	tts.save("tmp/time.mp3")
	os.system('mpg123 tmp/time.mp3')
	return
def playPlaylist () :
	stopPlaylist()
	os.system('mpc add spotify:user:icelandairwaves:playlist:3dNCFy3Q9d6LtGZLWT0c2O')
	os.system('mpc play')
	return
def stopPlaylist () :
	os.system('mpc clear')
	return
def load () :
	stopPlaylist()
	os.system('amixer set Master ' + str(etc.config.volume_music) + '%')
	os.system('mpc random 1')
	os.system('mpc volume 100')
	return

load()

readTime()
playPlaylist()

def snooze():
    print("Button pressed!")
    stopPlaylist()
    time.sleep(etc.config.time_snooze)
    readTime()
    playPlaylist()
    return

#GPIO.add_event_detect(etc.config.pin_button, GPIO.RISING, callback=buttonPress, bouncetime=button_bounce_time)

while True:
    GPIO.wait_for_edge(etc.config.pin_button, GPIO.FALLING)
    print "Pressed"
    start = time.time()
    time.sleep(0.2)

    while GPIO.input(etc.config.pin_button) == GPIO.LOW:
        time.sleep(0.01)
    length = time.time() - start
    print length

    if length > 3:
        os.system('mpg123 tmp/stopping.mp3')
        sys.exit()
    else:
        print "buttonPress"

GPIO.cleanup()           # clean up GPIO on normal exit
