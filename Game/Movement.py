
def vectorMovementWithoutCollision(gameMap, gameObject): #Returns True if successful and false otherwise
	if(gameObject.loc[0] + gameObject.velocity[0] in range(gameMap.size[0]) and
	gameObject.loc[1] + gameObject.velocity[1] in range(gameMap.size[1])):
		gameObject.loc[0] += gameObject.velocity[0]
		gameObject.loc[1] += gameObject.velocity[1]
		#print(str(gameObject.loc[0]) + ' ' + str(gameObject.loc[1]))
		return True
	else:
		return False

def vectorMovementWithCollision(gameMap, gameObject):
	obstacles = gameMap.gameObjects

class MovementRule:

	def __init__(self):
		pass
