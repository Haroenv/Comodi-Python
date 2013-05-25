from libs import Config as lib_config, Model as lib_model
import time as lib_time, pygame

class Alarm(lib_model.Model):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		pygame.mixer.init()
		Config = lib_config.Config
		self.Logger = lib_config.Logger
		self.music_dir = Config.get('model_music', 'directory')
		self.alarms = [[Config.get('model_alarm', 'alarm1_time'), Config.get('model_alarm', 'alarm1_song'), False],
					[Config.get('model_alarm', 'alarm2_time'), Config.get('model_alarm', 'alarm2_song'), False]]
		
	def getAlarm(self):
		result = []
		for (time, song, enabled) in self.alarms:
			if(enabled == True):
				enabled = 'Enabled'
			else:
				enabled = 'Disabled'
			result.append([time, enabled])
		return result
		
	def alarm(self):
		localtime = lib_time.localtime()
		time_current = lib_time.strftime('%H:%M', localtime)
		current = 0
		
		for (time_alarm, song, enabled) in self.alarms:
			if(time_alarm == time_current and enabled == True):
				pygame.mixer.music.set_volume(1)
				if pygame.mixer.music.get_busy():
					pygame.mixer.music.stop()
				pygame.mixer.music.load(self.music_dir + song)
				pygame.mixer.music.play()
				self.setAlarm(current)
			current += 1
				
				
	def setAlarm(self, alarm_number):
		self.alarms[alarm_number][2] = not self.alarms[alarm_number][2]
		self.refresh()
			
	def setFirstAlarm(self):
		self.setAlarm(0)
		
	def setSecondAlarm(self):
		self.setAlarm(1)
