from libs import Controller as lib_controller

class KEY_POWER(lib_controller.Controller):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		if(self.lcd.sleep == True):
			self.Logger.debug('Waking up from sleep mode.')
			self.lcd.display()
			self.bootstrap.refresh()
		else:
			self.Logger.debug('Going into sleep mode.')
			self.lcd.noDisplay()
