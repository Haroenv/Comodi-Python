import time as lib_time
from libs import Controller as lib_controller

class Date(lib_controller.Controller):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		
		self.notation_date = self.Config.get('model_date', 'notation_date')
		self.notation_time = self.Config.get('model_date', 'notation_time')
	
	def getInfo(self):
		localtime = lib_time.localtime()
		date = lib_time.strftime(self.notation_date, localtime)
		time = lib_time.strftime(self.notation_time, localtime)
		result = [time, date]
		return result
		
