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
		self.Logger.info('Please wait for Comodi to finish booting.')
		self.Music = model_music.Music(self)
		
		self.menus = {'KEY_1': KEY_1.KEY_1,
					'KEY_2': KEY_2.KEY_2,
					'KEY_3': KEY_3.KEY_3
						}
		
		self.displayControllers = {'KEY_POWER' : KEY_POWER.KEY_POWER }
						
		self.controllerMethods = {'KEY_NEXTSONG' : self.Music.nextSong,
							'KEY_PREVIOUSSONG' : self.Music.prevSong,
							'KEY_PLAYPAUSE' : self.Music.play,
							'KEY_VOLUMEUP' : self.Music.volumeUp,
							'KEY_VOLUMEDOWN' : self.Music.volumeDown
							}
		
		self.delay = 0
		self.delay_time = 0
		self.refresh_rate = float(self.Config.get('main', 'refresh_rate'))
		
		self.irThread = Thread(target=model_infrared.Infrared)
		self.irThread.start()
		
		self.current_menu_key = 'KEY_' + str(self.Config.get('main', 'menu_on_startup'))
		self.current_menu = self.menus[self.current_menu_key]
		
		# Start Comodi
		self.start(True)
		self.Logger.info('Welcome to Comodi, you can now control me.')
		try:
			while True:
				self.start()
				
		except Exception as e:
			self.Logger.exception(e)
			self.lcd.clear()
			sys.exit()
			
	def refresh(self, key = False):
		self.Logger.debug('Refresh: key = ' + str(key) )
		if(key != False and key == self.current_menu_key):
			self.current_menu(self)
		elif(key == False and self.current_menu_key == 'KEY_1'):
			self.current_menu(self)
		
	def start(self, first = False):
		# Check for a key pressed on the remote
		key = model_infrared.getKey()
		
		if(key != False or (self.delay >= self.delay_time and not self.lcd.sleep) or first == True):
			# Key set or (minute has passed and lcd is not in sleep mode) or when it's the first time
			# --> Will only update when a button is pressed in sleep mode
			if(key != False):
				# Key set
				if(key in self.menus):
					# If the key is a menu key, open the menu's class
					self.current_menu_key = key
					self.current_menu = self.menus[key]
					self.current_menu(self)
				elif(key in self.controllerMethods):
					# Fire controllerMethods
					controllerMethod = self.controllerMethods[key]()
				elif(key in self.displayControllers):
					displayController = self.displayControllers[key](self)
				else:
					self.Logger.debug('The key "' + key + '" has not been defined!')
				print('')
			else:
				# Key not set, refresh display
				self.refresh()
			# Reset delay and set time till next minute
			self.delay = 0
			self.delay_time = 60 - int(time.strftime('%S', time.localtime()))
		else:
			# Key not set, check again
			self.delay += self.refresh_rate
			time.sleep(self.refresh_rate)
			
