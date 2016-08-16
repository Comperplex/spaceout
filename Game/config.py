import os
import configparser

def load_var(name, section='setup_vars', isInt=True):
	currDir = os.path.dirname(os.path.realpath(__file__))
	config = configparser.ConfigParser()
	config.read(currDir + '\\variables.ini')
	
	if(isInt):
		return int(config.get(section, name))
	return config.get(section, name)
