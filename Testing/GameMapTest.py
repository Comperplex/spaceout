import unittest
import os, sys

currDir = os.path.dirname(os.path.realpath(__file__))
rootDir = os.path.abspath(os.path.join(currDir, '..'))
gameDir = rootDir + "\\Game"
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
		self.assertFalse(gameMap.addObject(dupeGameObject))

	def testID(self):
		gameMap = GameMap(100)

		for i in range(10):
			gameMap.addObject(GameObject([0,0], 'drone', 'owen'))
			self.assertEqual(gameMap.gameObjects[i].ID, i)

		gameMap.addObject(GameObject([0,0], 'beacon', 'owen'))
		self.assertEqual(gameMap.playerSortedObjectDict['owen'][0].ID, 0)

		gameMap.removeObject('owen', 'drone', 2)
		self.assertEqual

if __name__ == '__main__':
	unittest.main()
