import imaplib, sys
from libs import Config as lib_config, Model as lib_model

class Mail(lib_model.Model):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		
		self.Config = lib_config.Config
		self.Logger = lib_config.Logger
		self.server = self.Config.get('model_mail', 'imap4_ssl')
		self.mail = self.Config.get('model_mail', 'mail')
		self.password = self.Config.get('model_mail', 'password')
		self.login()
		
	def getUnread(self):
		if self.obj == None:
			self.login()
		self.obj.select()
		return len(self.obj.search(None, 'UnSeen')[1][0].split())
		
	def login(self):
		while True:
			try:
				self.obj = imaplib.IMAP4_SSL(self.server, '993')
				self.obj.login(self.mail, self.password)
				return
			except Exception as e:
				self.Logger.debug(str(e))
				continue

