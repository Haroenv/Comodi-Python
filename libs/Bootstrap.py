import models.infrared as model_infrared
import models.lcd as model_lcd
import libs.Config as libs_config
from threading import Thread
from controllers import KEY_1, KEY_2, KEY_3
import logging, time, sys
import RPi.GPIO as GPIO
		
class Bootstrap:
	def __init__(self):
		# Start the screen with 'loading'
		self.lcd = model_lcd.Adafruit_CharLCD()
		self.lcd.lines('', ['Welcome to Comodi', True], ['Loading...', True])
		
		# Initialization
		Config = libs_config.Config
		self.Logger = libs_config.Logger
		
		global KEY_1, KEY_2, KEY_3
		self.menus = {'KEY_1': KEY_1.KEY_1,
					'KEY_2': KEY_2.KEY_2,
					'KEY_3': KEY_3.KEY_3
						}
						
		self.delay = 0
		self.delay_time = 0
		self.refresh_rate = float(Config.get('main', 'refresh_rate'))
		
		irThread = Thread(target=model_infrared.Infrared)
		irThread.start()
		
		self.current_menu = self.menus['KEY_' + str(Config.get('main', 'menu_on_startup'))]
		
		# Start Comodi
		self.start(True)
		try:
			while True:
				self.start()
				
		except Exception as e:
			logging.exception(e)
			lcd.clear()
			sys.exit()
			
	def start(self, first = False):
		key = model_infrared.getKey()
		
		if(key != False or self.delay >= self.delay_time or first == True):
			self.Logger.debug(time.strftime('%H:%M:%S', time.localtime()))
			self.Logger.debug('key: ' + str(key))
			self.Logger.debug('Start update: ' + str(self.delay) + ' >= ' + str(self.delay_time))
			if(self.lcd.sleep == False and key != False and key in self.menus):
				self.Logger.debug('The key "' + str(key) + '" exists!')
				self.current_menu = self.menus[key]()
				self.Logger.debug(str(self.current_menu))
			elif(key == 'KEY_POWER'):
				if(self.lcd.sleep == True):
					self.Logger.debug('Waking up from sleep mode.')
					self.lcd.display()
				else:
					self.Logger.debug('Going into sleep mode.')
					self.lcd.noDisplay()
			elif self.current_menu != None:
				self.current_menu().__init__()
			elif(key != False):
				self.Logger.debug('The key "' + str(key) + '" has not been defined!')
			self.delay = 0
			self.delay_time = 60 - int(time.strftime('%S', time.localtime()))
			self.Logger.debug('Delay time set: ' + str(self.delay) + ' and ' + str(self.delay_time) + '\n')
		else:
			self.delay += self.refresh_rate
			time.sleep(self.refresh_rate)
			
			
			
