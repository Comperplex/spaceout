import os
from configparser import ConfigParser

currDir = os.path.dirname(os.path.realpath(__file__))
config = ConfigParser()

def load_var(var_name, section='setup_vars', isInt=True, filename='variables.ini'):
	config.read(os.path.join(currDir, filename))
	if(isInt):
		return int(config.get(section, var_name))
	return config.get(section, var_name)

def save_var_string(section, var_name, var_string, filename='variables.ini'):
	config.read(os.path.join(currDir, filename))
	if not config.has_section(section):
		config.add_section(section)
	config[section][var_name] = var_string
	with open(os.path.join(currDir, filename), 'w') as configfile:
		config.write(configfile)

#Test code
if __name__ == '__main__':
	save_var_string('blah', 'owens var', 'hi')
