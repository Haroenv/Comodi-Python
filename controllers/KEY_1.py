from models import date as model_date, mail as model_mail
from libs import Controller as lib_controller, Config as lib_config
import math

class KEY_1(lib_controller.Controller):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.lcd = self.bootstrap.lcd
		lines = []
		
		# LINE 1
		lines.append(['Home', 'center'])
		
		# LINE 2
		self.unread = str(self.bootstrap.Mail.getUnread())
		self.unread_text = ' unread messages'
		lines.append([self.unread + self.unread_text, 'center'])
	
		# LINE 3
		lines.append('')
	
		# LINE 4
		# DATE & TIME
		self.Date = self.bootstrap.Date
		date_info = self.Date.getInfo()
		self.time = date_info[0]
		self.date = date_info[1]
		lines.append(self.date + '  ' + self.time)
	
		# DISPLAY
		self.lcd.message(lines)
		
	def update(self):
		numcols = self.lcd.numcols
		# Update messages
		unread = str(self.bootstrap.Mail.getUnread())
		if unread != self.unread:
			unread_length = len(unread + self.unread_text)
		
			remain_left = math.floor((numcols - unread_length) / 2)
			remain_right = numcols - unread_length - remain_left
		
			if len(unread) != len(self.unread):
				unread_text = unread + self.unread_text
				self.lcd.write(unread_text.center(numcols), 1, 0)
			else:
				self.lcd.write(unread, 1, remain_left)
			self.unread = unread
		
		# Update time/date
		date_info = self.Date.getInfo()
		self.time = date_info[0]
		date = date_info[1]
		
		if(self.date != date):
			self.lcd.write(date + '  ' + time, 3, 0)
			self.date = date
		else:
			time_length = len(self.time)
			self.lcd.write(self.time, 3, numcols - time_length)
			
		
		
		
		
		
		
