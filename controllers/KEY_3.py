from libs import Controller, Config as lib_config
from models import lcd as model_lcd

class KEY_3(Controller.Controller):
	def __init__(self, bootstrap):
		# Initialize parent class
		# super(KEY_1, self)
		
		Logger = lib_config.Logger
		
		# LINE 1
		line1 = ['Nothing here', True]
		
		# LINE 2
		line2 = ''
	
		# LINE 3
		line3 = ''
	
		# LINE 4
		line4 = ['Still nothing', True]
	
		# DISPLAY
		lcd = model_lcd.Adafruit_CharLCD()
		lcd.lines(line1, line2, line3, line4)
