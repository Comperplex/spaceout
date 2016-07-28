import time
from GameMap import GameMap
from GameObject import GameObject

gameMap = GameMap(1000)

def runGame():
	currentTime = time.time()
	startTime = currentTime
	tickCount = 0

	myObject = GameObject([0,0], 'drone', 'owen')
	myObject.velocity = [1, 0]
	gameMap.addObject(myObject)

	while True:
		if(time.time() - currentTime  > 1): #10,000 ticks per second. This number can be changed as necessary
			tick()
			tickCount += 1
			currentTime = time.time()


		if currentTime - startTime > 10: break #quick line to time out the code after 10 seconds

def tick():
	gameMap.update()
	#tick process:
		#Take human input
		#Introduce new game pieces
		#update all game pieces

#THIS IS WHERE THE GAME IS RUN
runGame()
#THIS IS WHERE THE GAME IS RUN
