from libs import Controller, Config as lib_config
from models import lcd as model_lcd, music as model_music

class KEY_2(Controller.Controller):
	def __init__(self, bootstrap):
		# Initialize parent class
		# super(KEY_1, self)
		
		Logger = lib_config.Logger
		Music = model_music.Music
		
		# LINE 1
		line1 = ['Music Player', True]
		
		# LINE 2
		line2 = ['Santa Fe', True]
	
		# LINE 3
		line3 = ['Meneer prot', True]
	
		# LINE 4
		line4 = '1/18'
	
		# DISPLAY
		lcd = model_lcd.Adafruit_CharLCD()
		lcd.lines(line1, line2, line3, line4)
