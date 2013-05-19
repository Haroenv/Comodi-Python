import urllib.request as urllib_request
import json as jsonlib
from libs import Config as lib_config

class Weather:
	def __init__(self):
		self.Config = lib_config.Config
		self.Logger = lib_config.Logger
		self.free_key = Config.get('model_weather', 'key')
		self.previous_temperature = ''
		city = self.Config.get('model_weather', 'city')
		self.url = 'http://api.worldweatheronline.com/free/v1/weather.ashx?q=' + city + '&format=json&key=' + self.free_key
		self.temp = Config.get('model_weather', 'use_celsius')
	def getTemperature(self):
		tries = 0
		while True:
			tries += 1
			try:
				req = urllib_request.Request(self.url)
				raw = urllib_request.build_opener().open(req)
				json = jsonlib.load(raw)
				temp_choice = ['temp_F', 'temp_C']
				temperature = json['data']['current_condition'][0][temp_choice[self.tem]]
				self.previous_temperature = temperature
				return temperature
			except Exception as e:
				if(self.previous_temperature == ''):
					continue
				else:
					self.Logger.debug('It took ' + str(tries) + ' to get the temperature.')
					return self.previous_temperature
			break
		
