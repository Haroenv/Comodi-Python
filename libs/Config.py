import configparser, logging, os, stat

Config = configparser.RawConfigParser()

config_file_location = 'libs/config.ini'

if(not os.path.isfile(config_file_location)):
	config_file = open(config_file_location, 'w')
	os.chmod(config_file_location, stat.S_IRWXU)
	os.chmod(config_file_location, stat.S_IRWXG)
	os.chmod(config_file_location, stat.S_IRWXO)
	
	# Create all of the default sections first
	config_sections = ['main', 'model_date', 'model_mail', 'model_weather', 'model_music']
	for section in config_sections:
		Config.add_section(section)
		
	# Ask the user for the necessary information
	config_properties = ({'gpio_warnings' : 0, 'refresh_rate' : 0.1, 'menu_on_startup' : 1, 'debug' : 1},
	{'notation_date' : '%a %d %b %y', 'notation_time' : '%H:%M'},
	{'imap4_ssl' : 'imap.gmail.com', 'mail' : '', 'password' : ''},
	{'key' : '', 'city' : '', 'use_celsius' : 1}, {'directory' : ''})
	
	for s, p in zip(config_sections, config_properties):
		for prop, value in p.items():
			nv = input('\033[1mCreated property \033[32;1m' + prop + '\033[00;1m in section \033[32;1m' + s + '\033[00;1m with a default value of \033[32;1m' + str(value) + '\033[00;1m. Edit it or press enter to use the default value.\033[0m\n')
			if nv == '':
				nv = value
			Config.set(s, prop, nv)
			
	Config.write(config_file)
	config_file.close()
	

Config.read(config_file_location)

logging_levels = ['INFO', 'DEBUG']
Logger = logging.getLogger('main')
Logger.setLevel(logging.DEBUG)

logger_filehandler = logging.FileHandler('debug.log')
logger_filehandler.setLevel(logging.DEBUG)
logger_streamhandler = logging.StreamHandler()
logger_streamhandler.setLevel(getattr(logging, logging_levels[int(Config.get('main', 'debug'))]))

logger_formatter_filehandler = logging.Formatter('[%(levelname)s %(asctime)s] %(message)s')
logger_formatter_streamhandler = logging.Formatter('\033[33;1m[%(levelname)s] %(message)s\033[0m')

logger_filehandler.setFormatter(logger_formatter_filehandler)
logger_streamhandler.setFormatter(logger_formatter_streamhandler)

Logger.addHandler(logger_filehandler)
Logger.addHandler(logger_streamhandler)
