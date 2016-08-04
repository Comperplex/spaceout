import cherrypy
import jinja2
import os
import re
import json

import os, sys

currDir = os.path.dirname(os.path.realpath(__file__))
rootDir = os.path.abspath(os.path.join(currDir, '.'))
gameDir = rootDir + "\\Game"
sys.path.append(gameDir)

from Game import GameMap
from Game import GameObject

#os.system("compass watch &") # This is only for testing purposes. Remove on production
env = jinja2.Environment(loader=jinja2.FileSystemLoader('private/jinja2'))

def error(code=200, message=''):
	cherrypy.response.status = code
	if message == '':
		if code == 404: message = "That page couldn't be found."
		elif code == 500: message = "Oops! Something went wrong internally."
	return env.get_template('error.html').render({'code':code, 'message':message})


class Main(object):
	@cherrypy.expose
	def index(self, *args, **kwargs):
		return env.get_template('index.html').render()

	@cherrypy.expose
	def api(self, *args, **kwargs):
		if len(args) == 0:
			return error(404)
		elif args[0] == 'getMap':
			gameMap = GameMap(100)
			gameMap.addObject(GameObject([20,30], 'drone', 'owen'))
			flatGameMap = []
			for i in gameMap.gameObjects:
				flatGameMap.append(i.__dict__)
			return json.dumps(flatGameMap)
		else:
			return error(message="API method does not exist")

	@cherrypy.expose
	def default(self, *args, **kwargs):
		return error(404)

if __name__ == '__main__':
	conf = {
		'/': {
			'tools.staticdir.root': os.path.abspath(os.getcwd())
		},
		'/static': {
			'tools.staticdir.on': True,
			'tools.staticdir.dir': 'static'
		}
	}
	cherrypy.config.update({
		'server.socket_host': '0.0.0.0',
		'server.socket_port': 8080
	})

	cherrypy.quickstart(Main(), '/', conf)
