from libs import Controller, Config as lib_config
from models import lcd as model_lcd

class KEY_2(Controller.Controller):
	def __init__(self, bootstrap):
		# Initialize parent class
		# super(KEY_1, self)
		
		Logger = lib_config.Logger
		Music = bootstrap.Music
		
		# LINE 1
		line1 = ['Music Player', True]
		
		# LINE 2
		song = Music.getSong()
		line2 = [song[:20], True]
	
		# LINE 3
		line3 = [song[21:40], True]
	
		# LINE 4
		line4 = [str(Music.getSongNumber()) + '/' + str(Music.getSongTotal()), True]
	
		# DISPLAY
		lcd = model_lcd.Adafruit_CharLCD()
		lcd.lines(line1, line2, line3, line4)
