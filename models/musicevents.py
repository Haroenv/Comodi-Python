from threading import Thread
from libs import Config as lib_config
import subprocess, logging, pygame, time

class MusicEvents(Thread):
	def __init__(self, music):
		global loop
		Logger = lib_config.Logger
		while True:
			for event in pygame.event.get():
				if(event.type == pygame.constants.USEREVENT):
					music.nextSong()
			time.sleep(0.1)
			
