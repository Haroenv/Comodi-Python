import models.lcd as model_lcd
import libs.Config as lib_config
import models.mail as model_mail
import models.date as model_date
from libs import Controller

class KEY_1(Controller.Controller):
	def __init__(self, bootstrap):
		# Initialize parent class
		# super(KEY_1, self)
		
		Logger = lib_config.Logger
		
		# LINE 1
		line1 = ['Home', True]
		
		# LINE 2
		Mail = model_mail.Mail()
		unread_messages = Mail.getUnread()
		line2 = [str(unread_messages) + ' unread messages', True]
	
		# LINE 3
		line3 = ''
	
		# LINE 4
		# DATE & TIME
		Date = model_date.Date()
		date_info = Date.getInfo()
		line4 = date_info[1] + '  ' + date_info[0]
	
		# DISPLAY
		lcd = model_lcd.Adafruit_CharLCD()
		lcd.lines(line1, line2, line3, line4)
