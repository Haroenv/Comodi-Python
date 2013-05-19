#- coding: utf-8 -*-
from __future__ import unicode_literals

import classes.weather as weatherlib
import classes.mail as maillib
import classes.date as datelib
import classes.ir as ir
import classes.lcd as lcd
import classes.irthread as irthreadlib
import RPi.GPIO as GPIO
import time as timelib
import traceback, sys
from threading import Thread

GPIO.setwarnings(False)
LCD = lcd.Adafruit_CharLCD()
LCD.display()

irthread = Thread(target=irthreadlib.IRThread)
irthread.start()

key = ''

def update():
	# LINE 1
	if(key == ''):
		line1 = ['Comodi', True]
	else:
		line1 = [str(key), True]
		
	# LINE 2
	Mail = maillib.Mail()
	unread_messages = Mail.getUnread()
	line2 = str(unread_messages) + ' unread messages'
	
	# LINE 3
	Weather = weatherlib.Weather()
	temperature = Weather.getTemperature()
	line3 = 'Temperature: ' + temperature + '°C'
	
	# LINE 4
	# DATE & TIME
	Date = datelib.Date()
	date_info = Date.getInfo()
	line4 = date_info[1] + '  ' + date_info[0]
	
	# DISPLAY
	LCD.lines(line1, line2, line3, line4)
	
delay = 0
delay_time = 0
delay_check = 0.1
	
try:
	while True:
	
		key = irthreadlib.getKey()
		
		if(key != '' or delay >= delay_time):
			delay = 0
			print 'Start update: ' + str(delay) + ' >= ' + str(delay_time)
			update()
			delay_time = 60 - int(timelib.strftime('%S', timelib.localtime()))
			print 'Delay time set: ' + str(delay) + ' and ' + str(delay_time)
		else:
			delay += delay_check
			timelib.sleep(delay_check)
			
			
		# SLEEP
		#delay = 60 - int(timelib.strftime('%S', timelib.localtime()))
		
		#timelib.sleep(delay)

except Exception, e:
	LCD.clear()
