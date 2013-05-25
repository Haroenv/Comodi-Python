import imaplib, sys
from libs import Config as lib_config

class Mail:
	def __init__(self):
		self.Config = lib_config.Config
		self.Logger = lib_config.Logger
		server = self.Config.get('model_mail', 'imap4_ssl')
		mail = self.Config.get('model_mail', 'mail')
		password = self.Config.get('model_mail', 'password')
		while True:
			try:
				self.obj = imaplib.IMAP4_SSL(server, '993')
				self.obj.login(mail, password)
				return
			except Exception as e:
				self.Logger.debug(str(e))
				continue
	def getUnread(self):
		self.obj.select()
		return len(self.obj.search(None, 'UnSeen')[1][0].split())

