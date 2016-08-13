import time
import threading
import random

from GameMap import GameMap
from GameObject import GameObject
from Variables import Variables

from functools import wraps
def delay(delay=0.): # sets a timer to run a function later on - http://fredericiana.com/2014/11/14/settimeout-python-delay/
    def wrap(f):
        @wraps(f)
        def delayed(*args, **kwargs):
            timer = threading.Timer(delay, f, args=args, kwargs=kwargs)
            timer.start()
        return delayed
    return wrap

variable = Variables()

gameMap = GameMap(variable.max_entities)

for a in range(variable.max_asteroids + 1):#Creates Asteroids Before game starts
    loc = [randint(0, variable.map_size), randint(0, variable.map_size)]
    asteroid = GameObject(loc, "asteroid", "map")
    gameMap.addObject(asteroid)

def runGame(tickFreq=.1):
	currentTime = time.time()
	startTime = currentTime
	tickCount = 0

	t = threading.currentThread()
	print("Game loop has started.")
	while getattr(t, "do_run", True):
		if(time.time() - currentTime  > tickFreq): #10 ticks per second. This number can be changed as necessary
			tick()
			tickCount += 1
			currentTime = time.time()

		# if currentTime - startTime > 10: break #quick line to time out the code after 10 seconds
	print("Game loop has been terminated.")

def tick():
	gameMap.update()
	#tick process:
		#Take human input
		#Introduce new game pieces
		#update all game pieces

#START TEST CODE
if __name__ == '__main__':
	thr = threading.Thread(target=runGame, args=(), kwargs={})
	thr.start()

	myObject = GameObject([0,0], 'drone', 'owen')
	myObject.velocity = [1, 0]
	gameMap.addObject(myObject)
	while True:
		flatGameMap = []
		for i in gameMap.gameObjects:
			flatGameMap.append(i.__dict__)
		print(flatGameMap)
		time.sleep(.1)
#END TEST CODE
