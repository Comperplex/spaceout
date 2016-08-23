import cherrypy, jinja2
import os, sys, re, ast, json
import threading

currDir = os.path.dirname(os.path.realpath(__file__))
rootDir = os.path.abspath(os.path.join(currDir, '.'))
gameDir = os.path.join(rootDir, "Game")
sys.path.append(gameDir)

from Game.GameMap import GameMap
from Game.GameObject import GameObject
from Game.Command import Command
from Game import MainGameLoop
from Game import config
from Game import Movement

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
			jsonGameMap = {
				'size': [config.load_var('map_x_size'), config.load_var('map_y_size')],
				'limits': {
					'players': config.load_var('max_players'),
					'entities': config.load_var('max_entities')
				},
				'objects': []
			}
			for i in MainGameLoop.gameMap.gameObjects:
				jsonGameMap['objects'].append(i.getDict())
			return json.dumps(jsonGameMap)
		elif args[0] == 'addObj':
			if set(['loc','type','player']).issubset(kwargs):
				loc = [int(kwargs['loc'].split(',')[0]), int(kwargs['loc'].split(',')[1])]
				myObject = GameObject(loc, kwargs['type'], kwargs['player'])
				myObject.velocity = [1,1]
				MainGameLoop.gameMap.addObject(myObject)
				return json.dumps(myObject.getDict())
		elif args[0] == 'writeMsg':
			if 'msg' in kwargs:
				print(kwargs['msg'])
		elif args[0] == 'changeDirection':
			if set(['loc','ID']).issubset(kwargs):
				loc = [int(kwargs['loc'].split(',')[0]), int(kwargs['loc'].split(',')[1])]
				Movement.newVelocity(MainGameLoop.gameMap.getObject(kwargs['ID']), loc)
		elif args[0] == 'gotoPoint':
			if set(['loc','ID']).issubset(kwargs):
				loc = [int(kwargs['loc'].split(',')[0]), int(kwargs['loc'].split(',')[1])]
				MainGameLoop.gameMap.getObject(kwargs['ID']).current_cmd = Command('gotoPoint', dest_pt=loc)
		else:
			return error(message="API method does not exist")

	@cherrypy.expose
	def default(self, *args, **kwargs):
		return error(404)

if __name__ == '__main__':
	#Just for fun, the following two lines count the number of times this code has been run and saves it in variables.ini
	init_count = config.load_var(var_name='init_count', section='global_stats')
	config.save_var_string(var_name='init_count', section='global_stats', var_string=str(init_count + 1))

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

	thr = threading.Thread(target=MainGameLoop.runGame)
	thr.do_run = True
	thr.start()
	def stopit():
		thr.do_run = False
	cherrypy.engine.subscribe('stop', stopit)

	cherrypy.quickstart(Main(), '/', conf)
