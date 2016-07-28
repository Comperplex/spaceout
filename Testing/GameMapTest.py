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

	def testRemoveObject(self):
		gameMap = GameMap(100)
		listElement1 = GameObject([0,0], 'miner1', 'sammy')
		listElement2 = GameObject([0,0], 'drone1', 'THE MAJESTIC ERIC')
		listElement3 = GameObject([50, 50], 'energy bridge1', 'owen')

		gameMap.addObject(listElement1)
		gameMap.addObject(listElement2)
		gameMap.addObject(listElement3)

		self.assertTrue(gameMap.removeObject('sammy', 'miner1'))
		self.assertFalse(gameMap.removeObject('THE MAJESTIC ERIC', 'drone2'))

		self.assertEqual(len(gameMap.gameObjects), 2)

if __name__ == '__main__':
	unittest.main()