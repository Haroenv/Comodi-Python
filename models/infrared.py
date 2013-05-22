from threading import Thread
from multiprocessing import Queue
from libs import Config as lib_config
import subprocess, sys, time

lirc = Queue()

class Infrared(Thread):
	def __init__(self):
		global lirc, loop
		Thread.__init__(self)
		process = subprocess.Popen('irw', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		Logger = lib_config.Logger
		try:
			while True:
				line = process.stdout.readline().decode()
				if(line):
					line_info = line.split(' ')
					key = line_info[2]
					lirc.put(key)
				else:
					Logger.warn('No line to read, breaking the loop.')
					break
				time.sleep(0.1)
		except:
			sys.exit()
				
def getKey():
	if(lirc.empty()):
		return False
	else:
		return lirc.get()
