import time
from GameMap import GameMap

def runGame():

	currentTime = time.time()
	tickCount = 0

	gameMap = GameMap(1000)

	while True:
		if(time.time() - currentTime  > .0001): #10,000 ticks per second. This number can be changed as necessary
			tick()
			tickCount += 1
			currentTime = time.time()

def tick():
	#tick process:
		#Take human input
		#Introduce new game pieces
		#update all game pieces
	pass

#THIS IS WHERE THE GAME IS RUN
runGame()
#THIS IS WHERE THE GAME IS RUN
