import os
import configparser

currDir = os.path.dirname(os.path.realpath(__file__))
config = configparser.ConfigParser()

def load_var(var_name, section='setup_vars', isInt=True, filename='\\variables.ini'):
	config.read(currDir + filename)
	if(isInt):
		return int(config.get(section, var_name))
	return config.get(section, var_name)

def save_var_string(section, var_name, var_string, filename='\\variables.ini'):
	config.read(currDir + filename)
	if not config.has_section(section):
		config.add_section(section)
	config[section][var_name] = var_string
	with open(currDir + filename, 'w') as configfile:
		config.write(configfile)

#Test code
if __name__ == '__main__':
	save_var_string('blah', 'owens var', 'hi')
