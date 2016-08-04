import GameMap

def vectorMovementWithoutCollision(gameMap, gameObject):
	if(gameObject.loc[0] + gameObject.velocity[0] in range(gameMap.size[0]) and
	gameObject.loc[1] + gameObject.velocity[1] in range(gameMap.size[1])):
		gameObject.loc[0] += gameObject.velocity[0]
		gameObject.loc[1] += gameObject.velocity[1]
		print(str(gameObject.loc[0]) + ' ' + str(gameObject.loc[1]))

def vectorMovementWithCollision(gameMap, gameObject):
	obstacles = gameMap.gameObjects
