import imaplib
from libs import Config as lib_config

class Mail:
	def __init__(self):
		Config = lib_config.Config
		server = Config.get('model_mail', 'imap4_ssl')
		mail = Config.get('model_mail', 'mail')
		password = Config.get('model_mail', 'password')
		while True:
			try:
				self.obj = imaplib.IMAP4_SSL(server, '993')
				self.obj.login(mail, mail)
				self.obj.select()
				break
			except:
				continue
	def getUnread(self):
		return len(self.obj.search(None, 'UnSeen')[1][0].split())

