from models import infrared as model_infrared, lcd as model_lcd, music as model_music, alarm as model_alarm
from libs import Config as lib_config
from threading import Thread
from controllers import KEY_1, KEY_2, KEY_3, KEY_POWER
import logging, time, sys
		
class Bootstrap:
	def __init__(self):
		# Start the screen with 'loading'
		self.lcd = model_lcd.Adafruit_CharLCD()
		self.lcd.message(['', ['Welcome to Comodi', 'center'], ['Loading...', 'center']])
		
		
		# Initialization
		self.Config = lib_config.Config
		self.Logger = lib_config.Logger
		print('\033[1m' + 'Please wait for Comodi to finish booting.'.center(80) + '\033[0m')
		self.Music = model_music.Music(self)
		self.Alarm = model_alarm.Alarm(self)
		
		self.menus = {'KEY_1': KEY_1.KEY_1,
					'KEY_2': KEY_2.KEY_2,
					'KEY_3': KEY_3.KEY_3
						}
		
		self.displayControllers = {'KEY_POWER' : KEY_POWER.KEY_POWER }
						
		self.controllerMethods = {'KEY_NEXTSONG' : self.Music.nextSong,
							'KEY_PREVIOUSSONG' : self.Music.prevSong,
							'KEY_PLAYPAUSE' : self.Music.play,
							'KEY_VOLUMEUP' : self.Music.volumeUp,
							'KEY_VOLUMEDOWN' : self.Music.volumeDown,
							'KEY_PROG1' : self.Alarm.setFirstAlarm,
							'KEY_PROG2' : self.Alarm.setSecondAlarm
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
		print('\033[1m' + 'Welcome to Comodi, you can now control me.'.center(80))
		print('\n--------------------------------------------------------------------------------\033[0m')
		try:
			while True:
				self.start()
				
		except Exception as e:
			self.Logger.exception(e)
			self.lcd.clear()
			sys.exit()
			
	def refresh(self, key = False):
		if(key != False and key == self.current_menu_key):
			self.current_menu(self)
		elif(key == False and self.current_menu_key != 'KEY_2'):
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
					print('')
					self.current_menu_key = key
					self.current_menu = self.menus[key]
					self.current_menu(self)
				elif(key in self.controllerMethods):
					# Fire controllerMethods
					print('')
					controllerMethod = self.controllerMethods[key]()
				elif(key in self.displayControllers):
					print('')
					displayController = self.displayControllers[key](self)
				else:
					print('')
					self.Logger.debug('The key "' + key + '" has not been defined!')
			else:
				# Key not set, refresh display
				self.refresh()
			# Reset delay and set time till next minute
			self.Alarm.alarm()
			self.delay = 0
			self.delay_time = 60 - int(time.strftime('%S', time.localtime()))
		else:
			# Key not set, check again
			self.delay += self.refresh_rate
			time.sleep(self.refresh_rate)
			
