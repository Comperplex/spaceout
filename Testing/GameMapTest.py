import unittest
import os, sys

currDir = os.path.dirname(os.path.realpath(__file__))
rootDir = os.path.abspath(os.path.join(currDir, '..'))
gameDir = os.path.join(rootDir, "Game")
sys.path.append(gameDir)

from GameObject import GameObject
from GameMap import GameMap

class TestGameMap(unittest.TestCase):

	def testAddObject(self):
		gameMap = GameMap(2)

		#Testing a valid Game Object
		validGameObject = GameObject([0,0], 'drone', 'owen')
		self.assertTrue(gameMap.addObject(validGameObject))

		#Testing an invalid Game Object
		invalidGameObject = GameObject([gameMap.size[0], 0], 'beacon', 'charter')
		self.assertFalse(gameMap.addObject(invalidGameObject))

		dupeGameObject = GameObject([0,0], 'beacon', 'owen')
		self.assertTrue(gameMap.addObject(dupeGameObject))
		self.assertEqual(len(gameMap.playerSortedObjectDict['owen']), 2)
		self.assertFalse(gameMap.addObject(dupeGameObject)) #Testing that too many game objects cannot be added

	def testRemoveObject(self):
		gameMap = GameMap(2)
		gameMap.addObject(GameObject([0,0], 'drone', 'owen'))
		self.assertTrue(gameMap.removeObject('owen-drone-0'))
		self.assertEqual(len(gameMap.gameObjects), 0) #Testing the length of the unsorted gameObjects list

	def testID(self):
		gameMap = GameMap(100)

		for i in range(10):
			gameMap.addObject(GameObject([0,0], 'drone', 'owen'))
			self.assertEqual(gameMap.gameObjects[i].ID, 'owen-drone-' + str(i)) #Testing successful ID assignment

		gameMap.addObject(GameObject([0,0], 'beacon', 'owen'))
		self.assertEqual(gameMap.playerSortedObjectDict['owen'][0].ID, 'owen-drone-0') #Testing successful '0' ID assignment

		self.assertTrue(gameMap.removeObject('owen-drone-2')) #Testing successful removal of an object
		self.assertIsNone(gameMap.getObject('owen-drone-2')) #Testing that the object was indeed removed
		self.assertIsNotNone(gameMap.getObject('owen-drone-3')) #Testing that another object that was added indeed exists

		gameMap.addObject(GameObject([1, 1], 'drone', 'owen'))
		self.assertIsNotNone(gameMap.getObject('owen-drone-2')) #Testing that, after adding a new relevant game object, the old ID=2 has been re-used

if __name__ == '__main__':
	unittest.main()
