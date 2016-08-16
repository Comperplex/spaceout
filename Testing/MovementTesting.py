import unittest
import os, sys

currDir = os.path.dirname(os.path.realpath(__file__))
rootDir = os.path.abspath(os.path.join(currDir, '..'))
gameDir = os.path.join(rootDir, "Game")
sys.path.append(gameDir)

from GameObject import GameObject
from GameMap import GameMap
import Movement

class MovementTesting(unittest.TestCase):

	def testVectorMoveWithoutCollision(self):
		gameMap = GameMap(1000)
		gameObject = GameObject([0, 0], 'drone', 'owen')
		gameObject.velocity = [1, 2]
		gameObject.acceleration = [-1, -1]
		gameMap.addObject(gameObject)

		gameMap.update()
		self.assertEqual(gameObject.loc, [1,2])

		gameMap.update()
		self.assertEqual(gameObject.loc, [1, 3])

		gameMap.update()
		self.assertEqual(gameObject.loc, [0, 3])

		gameMap.update() #Here, instead of going negative, the vectorMovementWithoutCollision function does nothing
		self.assertEqual(gameObject.loc, [0, 3])

if __name__ == '__main__':
	unittest.main()
