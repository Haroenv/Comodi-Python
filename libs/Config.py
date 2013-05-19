import configparser, logging, os

Config = configparser.RawConfigParser()

config_file_location = 'libs/config.ini'

if(not os.path.isfile(config_file_location)):
	config_file = open(config_file_location, 'w')
	
	# Create all of the default sections first
	config_sections = ['main', 'model_date', 'model_mail', 'model_weather']
	for section in config_sections:
		Config.add_section(section)
		
	# Ask the user for the necessary information
	config_properties = ({'gpio_warnings' : 0, 'refresh_rate' : 0.1, 'menu_on_startup' : 1, 'enable_console_debug' : 1},
	{'notation_date' : '%a %d %b %y', 'notation_time' : '%H:%M'},
	{'imap4_ssl' : 'imap.gmail.com', 'mail' : '', 'password' : ''},
	{'key' : '', 'city' : '', 'use_celsius' : 1})
	
	for s, p in zip(config_sections, config_properties):
		for prop, value in p.items():
			nv = input('Created property "' + prop + '" in section "' + s + '" with a default value of "' + str(value) + '". Edit it or press enter to use the default value.\n')
			if nv == '':
				nv = value
			print(s, prop, nv)
			Config.set(s, prop, nv)
			
	Config.write(config_file)
	

Config.read(config_file_location)

logging_levels = ['INFO', 'DEBUG']
Logger = logging.getLogger('main')
Logger.setLevel(logging.DEBUG)

logger_filehandler = logging.FileHandler('debug.log')
logger_filehandler.setLevel(logging.DEBUG)
logger_streamhandler = logging.StreamHandler()
logger_streamhandler.setLevel(getattr(logging, logging_levels[int(Config.get('main', 'enable_console_debug'))]))

logger_formatter_filehandler = logging.Formatter('[%(levelname)s %(asctime)s] %(message)s')
logger_formatter_streamhandler = logging.Formatter('\033[33;1m[%(levelname)s] %(message)s\033[0m')

logger_filehandler.setFormatter(logger_formatter_filehandler)
logger_streamhandler.setFormatter(logger_formatter_streamhandler)

Logger.addHandler(logger_filehandler)
Logger.addHandler(logger_streamhandler)
