from libs import Config as lib_config

class Controller:
	def __init__(self, bootstrap = None):
		self.bootstrap = bootstrap
		self.Logger = lib_config.Logger
		self.Config = lib_config.Config
		self.lcd = bootstrap.lcd
