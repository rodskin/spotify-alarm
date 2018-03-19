#!/usr/bin/env python
# encoding: utf-8

import sys
import os
import gtts
import datetime
import time
import RPi.GPIO as GPIO
import etc.config

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def readTime ():
	date = datetime.datetime.now()
	current_time = "Il est " + str(date.hour) + ':' + str(date.minute)
	lang = 'fr'
	tts = gtts.gTTS(text=current_time, lang=lang)
	tts.save("tmp/time.mp3")
	os.system('mpg123 tmp/time.mp3')
	return none
def playPlaylist () :
	stopPlaylist()
	os.system('mpc random 1')
	os.system('mpc volume 100')
	os.system('mpc add spotify:user:icelandairwaves:playlist:3dNCFy3Q9d6LtGZLWT0c2O')
	os.system('mpc play')
	return none
def stopPlaylist () :
	os.system('mpc clear')
	return none

os.system('amixer set Master 50%')

readTime()
playPlaylist()

def buttonPress(channel):
    print "Button pressed!"
    stopPlaylist()
    time.sleep(5)
    readTime()
    playPlaylist()
    return none

GPIO.add_event_detect(23, GPIO.RISING, callback=buttonPress, bouncetime=300)

raw_input("Listening...")
GPIO.cleanup()           # clean up GPIO on normal exit
