from libs import Controller

class KEY_POWER(Controller.Controller):
	def __init__(self, bs):
		if(bs.lcd.sleep == True):
			bs.Logger.debug('Waking up from sleep mode.')
			bs.lcd.display()
		else:
			bs.Logger.debug('Going into sleep mode.')
			bs.lcd.noDisplay()
