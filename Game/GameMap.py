from GameObject import GameObject

class GameMap:
	size = [500, 500]
	gameObjects = {}

	def __init__(self, maxEntities):
		self.maxEntities = maxEntities

	def addObject(self, gameObject): #Tries to add a new game Object to the dictionary of game objects. Returns true if successful and false otherwise
		if gameObject.loc[0] in range(self.size[0]) and gameObject.loc[1] in range(self.size[1]) and len(self.gameObjects) < self.maxEntities + 1:
			if gameObject.player in self.gameObjects:
				#print(len(self.gameObjects[gameObject.player][0]))
				self.gameObjects[gameObject.player].append(gameObject)
				#If the object dict contains objects from this player already, add this new object to the list
			else:
				self.gameObjects[gameObject.player] = [gameObject]
				#If the object dict contains no objects from this player, make a new list of objects for this player
			return True
		else:
			return False

	def moveObject(self, player, name, xIncrement, yIncrement):
		for gameObject in self.gameObjects[player]:
			if gameObject.name is name:
				gameObject.loc[0] += xIncrement
				gameObject.loc[1] += yIncrement
				break

	def removeObject(self, player, name):
		for gameObject in self.gameObjects[player]:
			if gameObject.name is name: self.gameObjects[player].remove(gameObject)
