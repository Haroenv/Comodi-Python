from models import infrared as model_infrared, lcd as model_lcd, music as model_music
from libs import Config as lib_config
from threading import Thread
from controllers import KEY_1, KEY_2, KEY_3, KEY_POWER
import logging, time, sys
		
class Bootstrap:
	def __init__(self):
		# Start the screen with 'loading'
		self.lcd = model_lcd.Adafruit_CharLCD()
		self.lcd.lines('', ['Welcome to Comodi', True], ['Loading...', True])
		
		# Initialization
		self.Config = lib_config.Config
		self.Logger = lib_config.Logger
		self.Music = model_music.Music()
		
		self.menus = {'KEY_1': KEY_1.KEY_1,
					'KEY_2': KEY_2.KEY_2,
					'KEY_3': KEY_3.KEY_3
						}
		
		self.controllers = {'KEY_POWER' : KEY_POWER.KEY_POWER }
						
		self.musicControllers = {'KEY_NEXTSONG' : self.Music.nextSong,
							'KEY_PREVIOUSSONG' : self.Music.prevSong,
							'KEY_PLAYPAUSE' : self.Music.play,
							'KEY_VOLUMEUP' : self.Music.volumeUp,
							'KEY_VOLUMEDOWN' : self.Music.volumeDown
							}
		
		self.delay = 0
		self.delay_time = 0
		self.refresh_rate = float(self.Config.get('main', 'refresh_rate'))
		
		irThread = Thread(target=model_infrared.Infrared)
		irThread.start()
		
		self.current_menu = self.menus['KEY_' + str(self.Config.get('main', 'menu_on_startup'))]
		
		# Start Comodi
		self.start(True)
		try:
			while True:
				self.start()
				
		except Exception as e:
			self.Logger.exception(e)
			self.lcd.clear()
			sys.exit()
			
	def start(self, first = False):
		key = model_infrared.getKey()
		
		if(key != False or self.delay >= self.delay_time or first == True):
			self.Logger.debug(time.strftime('%H:%M:%S', time.localtime()))
			self.Logger.debug('key: ' + str(key))
			if(key != False):
				if(self.lcd.sleep == False and key in self.menus):
					self.current_menu = self.menus[key]
					self.current_menu(self)
					self.Logger.debug(str(self.current_menu))
				elif(key in self.controllers):
					controller = self.controllers[key](self)
				elif(key in self.musicControllers):
					musicController = self.musicControllers[key]()
				else:
					self.Logger.debug('The key "' + str(key) + '" has not been defined!')
			elif self.current_menu != None:
				self.current_menu(self).__init__(self)
			self.delay = 0
			self.delay_time = 60 - int(time.strftime('%S', time.localtime()))
		else:
			self.delay += self.refresh_rate
			time.sleep(self.refresh_rate)
			
			
			
