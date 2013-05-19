import time as timelib
from libs import Config as lib_config

class Date:
	
	def __init__(self):
		Config = lib_config.Config
		self.notation_date = Config.get('model_date', 'notation_date')
		self.notation_time = Config.get('model_date', 'notation_time')
	
	def getInfo(self):
		localtime = timelib.localtime()
		date = timelib.strftime(self.notation_date, localtime)
		time = timelib.strftime(self.notation_time, localtime)
		result = [time, date]
		return result
		
