#- coding: utf-8 -*-
from __future__ import unicode_literals

import models.infrared as model_infrared
import models.lcd as model_lcd
import libs.Config as libs_config
import models.mail as model_mail
import models.weather as model_weather
import models.date as model_date
from libs import Controller

class KEY_1(Controller.Controller):
	def __init__(self):
		# Initialize parent class
		super(KEY_1, self).__init__()
		
		# LINE 1
		line1 = ['Comodi', True]
		
		# LINE 2
		Mail = model_mail.Mail()
		unread_messages = Mail.getUnread()
		line2 = str(unread_messages) + ' unread messages'
	
		# LINE 3
		Weather = model_weather.Weather()
		temperature = Weather.getTemperature()
		line3 = 'Temperature: ' + temperature + '°C'
	
		# LINE 4
		# DATE & TIME
		Date = model_date.Date()
		date_info = Date.getInfo()
		line4 = date_info[1] + '  ' + date_info[0]
	
		# DISPLAY
		lcd = model_lcd.Adafruit_CharLCD()
		lcd.lines(line1, line2, line3, line4)
