# amixer cset numid=3 N
# N = 0 -> Auto audio output
# N = 1 -> Analog audio output
# N = 2 -> HDMI audio output

import pygame, time, os
from libs import Config as lib_config
from models import musicevents as model_musicevents
from threading import Thread

class Music:
	def __init__(self, bootstrap):
		pygame.init()
		pygame.mixer.init()
		
		# Defaults
		self.controller = 'KEY_1'
		self.bootstrap = bootstrap
		self.Config = lib_config.Config
		self.Logger = lib_config.Logger
		self.mixerMusic = pygame.mixer.music
		self.song_current = 0
		self.paused = False
		
		# Set queue for all files in directory
		self.music_dir = self.Config.get('model_music', 'directory')
		self.songs = []
		for path, dirs, files in os.walk(self.music_dir):
			for f in files:
				if f.endswith('.mp3'):
					self.songs.append(f)
					
		self.song_total = len(self.songs)
		
		eventThread = Thread(target=model_musicevents.MusicEvents, args=[self])
		eventThread.start()
		
	def play(self, option = 0):
		if(option != 0):
			# Next/Previous song
			if(option == -1 and self.getProgress() >= 10):
				# PreviousSong, but progress >= 10 -> rewind
				self.Logger.debug('Song didn\'t just start start -> rewind, progress: ' + str(self.getProgress()))
				self.mixerMusic.rewind()
				self.mixerMusic.play()
			else:
				# Changing song but it's playing so I'll have to stop current first
				self.song_current += option
				if(self.song_current >= self.song_total):
					# If it's the last song, go back to the beginning
					self.song_current = 0
				elif(self.song_current < 0):
					# If it's the first song and he wants to go to the previous song, go to the end
					self.song_current = self.song_total - 1
					
				self.Logger.debug('OPTION: ' + str(option))
				self.Logger.debug('Changing song but it\'s playing so I\'ll have to stop current first')
				self.Logger.debug('previous song_current = ' + str(self.song_current))
				self.Logger.debug('song_current = ' + str(self.song_current))
				self.mixerMusic.stop()
				self.mixerMusic.load(self.music_dir + self.songs[self.song_current])
				self.mixerMusic.play()
				self.mixerMusic.set_endevent(pygame.USEREVENT)
			self.paused = False
				
		else:
			# Play/Pause song
			if(self.mixerMusic.get_pos() == -1):
				# Song never started because -1 means not started
				self.Logger.debug('No song playing')
				self.mixerMusic.load(self.music_dir + self.songs[self.song_current])
				self.mixerMusic.play()
				self.paused = False
			elif(self.isPlaying()):
				# Song is playing -> pause it
				self.Logger.debug('Keep song -> pause')
				self.mixerMusic.pause()
				self.paused = True
			else:
				# The song is paused -> unpause it
				self.Logger.debug('Music unpaused: ' + str(self.mixerMusic.get_pos()))
				self.mixerMusic.unpause()
				self.paused = False
		
	def nextSong(self):
		self.play(1) 
		
		
	def prevSong(self):
		self.play(-1) 
		
	def getSong(self):
		return self.songs[self.song_current]
		
	def getSongNumber(self):
		return self.song_current + 1
		
	def getSongTotal(self):
		return self.song_total
		
	def isPlaying(self):
		result = (self.mixerMusic.get_busy() and not self.paused)
		self.Logger.debug('Result = (' + str(self.mixerMusic.get_busy()) + ' and ' + str(not self.paused) + ')')
		return result
		
	def setVolume(self, option):
		volume = self.mixerMusic.get_volume()
		if(not((volume == 0 and option == -1) or (volume == 1 and option == 1))):
			self.mixerMusic.set_volume(volume + (0.1 * option))
			self.refresh()
			return True
		else:
			return False
			
	def volumeUp(self):
		self.setVolume(1)
		
	def volumeDown(self):
		self.setVolume(-1)
			
	def getVolume(self):
		return self.mixerMusic.get_volume() * 10
		
	def getProgress(self):
		self.Logger.debug(str(self.mixerMusic.get_pos() / 1000))
		return int(self.mixerMusic.get_pos() / 1000)
		
	def refresh(self):
		self.bootstrap.refresh(self.controller)
		
