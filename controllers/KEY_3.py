from libs import Controller, Config as lib_config
from models import lcd as model_lcd, date as model_date

class KEY_3(Controller.Controller):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		
		lines = []
		
		# LINE 1
		lines.append(['Alarms', 'center'])
		
		# LINE 2
		Alarm = self.bootstrap.Alarm
		alarms = Alarm.getAlarm()
			
		lines.append(alarms[0][0] + ' - ' + str(alarms[0][1]))
	
		# LINE 3
		lines.append(alarms[1][0] + ' - ' + str(alarms[1][1]))
	
		# LINE 4
		Date = model_date.Date()
		date_info = Date.getInfo()
		lines.append(date_info[1] + '  ' + date_info[0])
	
		# DISPLAY
		lcd = model_lcd.Adafruit_CharLCD()
		lcd.message(lines)
