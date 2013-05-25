import models.lcd as model_lcd
import libs.Config as lib_config
import models.mail as model_mail
import models.date as model_date
from libs import Controller

class KEY_1(Controller.Controller):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		lines = []
		
		# LINE 1
		lines.append(['Home', 'center'])
		
		# LINE 2
		Mail = model_mail.Mail()
		unread_messages = Mail.getUnread()
		lines.append([str(unread_messages) + ' unread messages', 'center'])
	
		# LINE 3
		lines.append('')
	
		# LINE 4
		# DATE & TIME
		Date = model_date.Date()
		date_info = Date.getInfo()
		lines.append(date_info[1] + '  ' + date_info[0])
	
		# DISPLAY
		lcd = model_lcd.Adafruit_CharLCD()
		lcd.message(lines)
