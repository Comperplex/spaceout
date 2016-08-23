import Movement
import config

def expandID(IDstr):
	a = {}
	a['player'] = str(IDstr.split('-')[0])
	a['objectType'] = str(IDstr.split('-')[1])
	a['IDnum'] = int(IDstr.split('-')[2])
	return a

class GameMap:
	def __init__(self, max_entities=config.load_var('max_entities'), size=[config.load_var('map_x_size'), config.load_var('map_y_size')]):
		#constants from config file
		self.maxEntities = max_entities
		self.size = size

		#dynamic game variables
		self.gameObjects = []
		self.playerSortedObjectDict = {}

	def addObject(self, gameObject): #Tries to add a new game Object to the dictionary of game objects. Returns true if successful and false otherwise
		if gameObject.loc[0] in range(self.size[0]) and gameObject.loc[1] in range(self.size[1]) and len(self.gameObjects) < self.maxEntities:
			IDNum = 0
			if gameObject.player in self.playerSortedObjectDict:
				#If the object dict contains objects from this player already, add this new object to the list
				IDList = []
				for someGameObject in self.playerSortedObjectDict[gameObject.player]:
					if gameObject.objectType == someGameObject.objectType:
						IDList.append(someGameObject.ID)
				for i in IDList:
					if str(IDNum) == str(i).split('-')[2]:
						IDNum += 1
				self.playerSortedObjectDict[gameObject.player].append(gameObject)
			else:
				#If the object dict contains no objects from this player, make a new list of objects for this player
				self.playerSortedObjectDict[gameObject.player] = [gameObject]
			self.gameObjects.append(gameObject)
			gameObject.ID = gameObject.player + '-' + gameObject.objectType + '-' + str(IDNum)
			print("added oject with ID " + str(gameObject.ID) + " which belongs to player: " + gameObject.player)
			return True
		else:
			return False

	def removeObject(self, ID): #only removes the object from the actual gameObject list
		gameObject = self.getObject(ID)
		if gameObject != None:
			self.playerSortedObjectDict[gameObject.player].remove(gameObject)
			self.gameObjects.remove(gameObject)
			return True
		return False

	def getObject(self, ID):
		expandedID = expandID(ID)
		for gameObject in self.playerSortedObjectDict[expandedID['player']]:
			if int(gameObject.ID.split('-')[2]) == expandedID['IDnum'] and gameObject.objectType == expandedID['objectType']:
				return gameObject

	def teleportObject(self, ID, goToXY):
		#Moves the object without any collision whatsoever. Think of this as a "Teleport"
		#Unlike moveWithCollision, this method moves an arbitary distance in both x and y
		gameObject = self.getObject(ID)
		xIncrement = goToXY[0] - gameObject.loc[0]
		yIncrement = goToXY[1] - gameObject.loc[1]
		if (gameObject.loc[0] + xIncrement) in range(self.size[0]) and (gameObject.loc[1] + yIncrement) in range(self.size[1]):
			gameObject.loc[0] += xIncrement
			gameObject.loc[1] += yIncrement

	def update(self):
		Movement.gameMap = self
		for gameObject in self.gameObjects:
			gameObject.update()
