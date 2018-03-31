#!/usr/bin/env python
# encoding: utf-8
# export GPIOZERO_PIN_FACTORY=pigpio
# export PIGPIO_ADDR=fe80::1%usb0

import sys
try:
    import etc.config
except ImportError:
    print('no config file, please add etc.config.py based on sample/config.py')
    sys.exit()
import os
import gtts
import datetime
import json
import math
import time
try:
    import RPi.GPIO as GPIO
except ImportError:
    import GPIOmock as GPIO
    print('TESTING')
import urllib2

dir_path = os.path.dirname(os.path.realpath(__file__))

GPIO.setmode(GPIO.BCM)
GPIO.setup(etc.config.pin_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(etc.config.pin_led, GPIO.OUT)   # Set pin mode as output
#p = GPIO.PWM(etc.config.pin_led, 1000)     # set Frequece to 1KHz

def internet_on():
    try:
        urllib2.urlopen('http://google.com', timeout=1)
        return True
    except urllib2.URLError as err: 
        return False


def readTime ():
    GPIO.output(etc.config.pin_led, GPIO.HIGH)
    date = datetime.datetime.now()
    current_time = "Il est " + str(date.hour) + 'h' + str(date.minute)

    data = data_organizer(data_fetch(url_builder(etc.config.city_id)))
    current_time += ', il fait ' +  str(data['temp']).replace('.', ',') + ' , vent ' + data['wind_deg_rosace'] + ' de ' + str(data['wind_nmi']) + ' noeuds.'
    print(current_time)
    #sys.exit()
    tts = gtts.gTTS(text=current_time, lang=etc.config.lang)
    tts.save(dir_path + '/mp3/time.mp3')
    os.system('mpg123 ' + dir_path + '/mp3/time.mp3')
    sys.exit()
    return
def playPlaylist () :
    stopPlaylist()
    os.system('mpc add ' + etc.config.playlist)
    os.system('mpc play')
    #ledBreathe()
    return
def playAlarm () :
    os.system('mpg123 --loop -1 ' + dir_path + '/mp3/alarm_sound_2.mp3')
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
            p.ChangeDutyCycle(dc)     # Change duty cycle
            time.sleep(0.05)
        time.sleep(1)
        for dc in range(100, -1, -5): # Decrease duty cycle: 100~0
            p.ChangeDutyCycle(dc)
            time.sleep(0.05)
        time.sleep(1)
    return
def data_organizer(raw_api_dict):
    data = dict(
        city=raw_api_dict.get('name'),
        country=raw_api_dict.get('sys').get('country'),
        temp=raw_api_dict.get('main').get('temp'),
        temp_max=raw_api_dict.get('main').get('temp_max'),
        temp_min=raw_api_dict.get('main').get('temp_min'),
        humidity=raw_api_dict.get('main').get('humidity'),
        pressure=raw_api_dict.get('main').get('pressure'),
        sky=raw_api_dict['weather'][0]['main'],
        wind=raw_api_dict.get('wind').get('speed'),
        wind_nmi=toNmi(raw_api_dict.get('wind').get('speed')),
        wind_deg=raw_api_dict.get('wind').get('deg'),
        wind_deg_rosace=windDirection(raw_api_dict.get('wind').get('deg')),
        cloudiness=raw_api_dict.get('clouds').get('all')
    )
    return data
def url_builder(city_id):
    unit = 'metric'  # For Fahrenheit use imperial, for Celsius use metric, and the default is Kelvin.
    api = 'http://api.openweathermap.org/data/2.5/weather?id='     # Search for your city ID here: http://bulk.openweathermap.org/sample/city.list.json.gz

    full_api_url = api + str(city_id) + '&mode=json&units=' + unit + '&APPID=' + etc.config.openweathermap_id_api
    return full_api_url
def data_fetch(full_api_url):
    url = urllib2.urlopen(full_api_url)
    output = url.read().decode('utf-8')
    raw_api_dict = json.loads(output)
    url.close()
    return raw_api_dict
def toNmi (msValue) :
    nmi = msValue * 1.9438444924406
    return int(math.floor(nmi))

def windDirection(angle) :
    #print(angle)
    rosace_list = ['Nord', 'Nord Nord Est', 'Nord Est', 'Est Nord Est', 'Est', 'Est Sud Est', 'Sud Est', 'Sud Sud Est', 'Sud', 'Sud Sud Ouest', 'Sud Ouest', 'Ouest Sud Ouest', 'Ouest', 'Ouest Nord Ouest', 'Nord Ouest', 'Nord Nord Ouest', 'Nord']
    #print(rosace_list)

    #print(rosace_list[int(math.floor(angle / (360 / 16)))])
    return rosace_list[int(math.floor(angle / (360 / 16)))]
def data_output(data):
    m_symbol = '\xb0' + 'C'
    print('---------------------------------------')
    print('Current weather in: {}, {}:'.format(data['city'], data['country']))
    print(data['temp'], m_symbol, data['sky'])
    print('Max: {}, Min: {}'.format(data['temp_max'], data['temp_min']))
    print('')
    print('Wind Speed: {}, Degree: {}'.format(data['wind'], data['wind_deg']))
    print('Wind direction: ' + data['wind_deg_rosace'])
    print('Wind nmi: {}'.format(data['wind_nmi']))
    print('Humidity: {}'.format(data['humidity']))
    print('Cloud: {}'.format(data['cloudiness']))
    print('Pressure: {}'.format(data['pressure']))
    print('')
    print('---------------------------------------')
def stopScript () :
    print("Long Press")
    stopPlaylist()
    os.system('mpg123 ' + dir_path + '/mp3/stopping.mp3')
    i = 1
    for i in range(0, 3):
        GPIO.output(etc.config.pin_led, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(etc.config.pin_led, GPIO.HIGH)
        time.sleep(0.5)
    GPIO.output(etc.config.pin_led, GPIO.LOW)
    GPIO.cleanup()
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
print('has connection: ' + str(internet_on()))


readTime()
sys.exit()
if (internet_on()):
    playPlaylist()
else :
    playAlarm()
#sys.exit()
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

GPIO.cleanup()           # clean up GPIO on normal exit
