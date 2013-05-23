from threading import Thread
from libs import Config as lib_config
import subprocess, logging, pygame, time

class MusicEvents(Thread):
	def __init__(self, music):
		global loop
		Logger = lib_config.Logger
		Logger.debug('MusicEvents initialized')
		while True:
			for event in pygame.event.get():
				if(event.type == pygame.constants.USEREVENT):
					Logger.debug('Next song...')
					music.nextSong()
			time.sleep(0.1)
			
