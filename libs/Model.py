from libs import Config as lib_config

class Model:
	def __init__(self, bootstrap):
		self.Logger = lib_config.Logger
		self.Config = lib_config.Config
		self.bootstrap = bootstrap
		
	def refresh(self, key = False):
		key = self.controller if hasattr(self, 'controller') else key
		self.bootstrap.refresh(key)
