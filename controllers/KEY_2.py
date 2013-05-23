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
		if(song == False):
			song = 'Not available'
		else:
			song = song[:-4]
		line2 = [song[:20], True]
	
		# LINE 3
		line3 = [song[20:40], True]
	
		# LINE 4
		song_info = str(Music.getSongNumber()) + '/' + str(Music.getSongTotal())
		volume = str(Music.getVolume()) + '/10'
		state = Music.getState()
		
		song_info_len = len(song_info)
		volume_len = len(volume)
		state_len = len(state)
		
		Logger.debug('"'+song_info+'"')
		Logger.debug('"'+volume+'"')
		Logger.debug('"'+state+'"')
		
		volume = volume.center(20-state_len-song_info_len)
		
		line4 = song_info + volume + state
	
		# DISPLAY
		lcd = model_lcd.Adafruit_CharLCD()
		lcd.lines(line1, line2, line3, line4)
