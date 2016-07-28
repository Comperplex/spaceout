from GameObject import GameObject

class GameMap:
	size = [500, 500]

	def __init__(self, maxEntities):
		self.maxEntities = maxEntities
		self.gameObjects = []
		self.playerSortedObjectDict = {}

	def addObject(self, gameObject): #Tries to add a new game Object to the dictionary of game objects. Returns true if successful and false otherwise
		if gameObject.loc[0] in range(self.size[0]) and gameObject.loc[1] in range(self.size[1]) and len(self.gameObjects) < self.maxEntities:
			if gameObject.player in self.playerSortedObjectDict:
				#print(len(self.playerSortedObjectDict[gameObject.player][0]))
				self.playerSortedObjectDict[gameObject.player].append(gameObject)
				#If the object dict contains objects from this player already, add this new object to the list
			else:
				self.playerSortedObjectDict[gameObject.player] = [gameObject]
				#If the object dict contains no objects from this player, make a new list of objects for this player
			self.gameObjects.append(gameObject)
			return True
		else:
			return False

	def removeObject(self, player, name):
		for gameObject in self.playerSortedObjectDict[player]:
			if gameObject.name is name:
				self.playerSortedObjectDict[player].remove(gameObject)
				self.gameObjects.remove(gameObject)
				return True
			else:
				return False

	def __getSpecificGameObject(self, player, name):
		for gameObject in self.playerSortedObjectDict[player]:
			if gameObject.name is name: return gameObject

	def moveObjectWithoutCollision(self, player, name, xIncrement, yIncrement):
		gameObject = self.__getSpecificGameObject(player, name)
		if (gameObject.player.loc[0] + xIncrement) in range(self.size[0]) and (gameObject.loc[1] + yIncrement) in range(self.size[1]):
			gameObject.loc[0] += xIncrement
			gameObject.loc[1] += yIncrement

	def moveObjectWithCollision(self, player, name, xIncrement, yIncrement):
		gameObject = self.__getSpecificGameObject(player, name)