from libs import Controller, Config as lib_config
from models import lcd as model_lcd

class KEY_2(Controller.Controller):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		
		Logger = lib_config.Logger
		Music = self.bootstrap.Music
		lines = []
		
		# LINE 1
		lines.append(['Music Player', 'center'])
		
		# LINE 2
		song = Music.getSong()
		if(song == False):
			song = 'Not available'
		else:
			song = song[:-4]
		lines.append([song[:20], 'center'])
	
		# LINE 3
		lines.append([song[20:40], 'center'])
	
		# LINE 4
		song_info = str(Music.getSongNumber()) + '/' + str(Music.getSongTotal())
		volume = str(Music.getVolume()) + '/10'
		state = Music.getState()
		
		song_info_len = len(song_info)
		volume_len = len(volume)
		state_len = len(state)
		
		volume = volume.center(20-state_len-song_info_len)
		
		lines.append(song_info + volume + state)
	
		# DISPLAY
		lcd = model_lcd.Adafruit_CharLCD()
		lcd.message(lines)
