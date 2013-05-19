from threading import Thread
from multiprocessing import Queue
from libs import Config as lib_config
import subprocess, logging

lirc = Queue()

class Infrared(Thread):
	def __init__(self):
		global lirc
		Thread.__init__(self)
		process = subprocess.Popen('irw', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		Logger = lib_config.Logger
		while True:
			line = process.stdout.readline()
			if(line):
				line_info = line.split(' ')
				key = line_info[2]
				lirc.put(key)
			else:
				Logger.warn('No line to read, breaking the loop.')
				break
				
def getKey():
	if(lirc.empty()):
		return False
	else:
		return lirc.get()
