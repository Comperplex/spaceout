import GameObject
import Movement

class GameMap:

	def __init__(self, maxEntities, size=[500, 500]):
		self.maxEntities = maxEntities
		self.gameObjects = []
		self.playerSortedObjectDict = {} #Contains ALL game objects that ever existed
		self.size = size

	def addObject(self, gameObject): #Tries to add a new game Object to the dictionary of game objects. Returns true if successful and false otherwise
		if gameObject.loc[0] in range(self.size[0]) and gameObject.loc[1] in range(self.size[1]) and len(self.gameObjects) < self.maxEntities:
			if gameObject.player in self.playerSortedObjectDict:
				self.playerSortedObjectDict[gameObject.player].append(gameObject)
				#If the object dict contains objects from this player already, add this new object to the list
			else:
				self.playerSortedObjectDict[gameObject.player] = [gameObject]
				#If the object dict contains no objects from this player, make a new list of objects for this player
			self.gameObjects.append(gameObject)

			IDNum = 0
			IDNumList = []
			for someGameObject in self.playerSortedObjectDict[player]:
				if gameObject.objectType == someGameObject.objectType:
					IDNumList.append(someGameObject.objectType.split()[2])
			def makeID():
				for i in range(max(IDNumList)):
					if i not in IDNumList:
						return i
				return max(IDNumList) + 1

				#for i in IDNumList:
					#if IDNum = i:
						#IDNum += 1
						#makeID()
				#return IDNum
			ID = makeID()
			gameObject.ID = gameObject.player + ' ' + gameObject.objectType + ' ' + str(ID)
			return True
		else:
			return False

	def removeObject(self, player, ID): #only removes the object from the actual gameObject list
		for gameObject in self.playerSortedObjectDict[player]:
			if gameObject.ID == ID:
				self.playerSortedObjectDict[player].remove(gameObject)
				self.gameObjects.remove(gameObject)
				return True
			else:
				return False

	def getSpecificGameObject(self, player, ID):
		for gameObject in self.playerSortedObjectDict[player]:
			if gameObject.ID is ID and gameObject in self.gameObjects:
				return gameObject

	def teleportObject(self, player, ID, xIncrement, yIncrement):
		#Moves the object without any collision whatsoever. Think of this as a "Teleport"
		#Unlike moveWithCollision, this method moves an arbitary distance in both x and y
		gameObject = self.getSpecificGameObject(player, ID)
		if (gameObject.player.loc[0] + xIncrement) in range(self.size[0]) and (gameObject.loc[1] + yIncrement) in range(self.size[1]):
			gameObject.loc[0] += xIncrement
			gameObject.loc[1] += yIncrement

	def update(self):
		for gameObject in self.gameObjects:
			#TEST CODE REMOVE LATER
			Movement.vectorMovementWithoutCollision(self, gameObject)
			#TEST CODE REMOVE LATER
			gameObject.update()
