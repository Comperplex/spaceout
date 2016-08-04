import unittest
import os, sys

currDir = os.path.dirname(os.path.realpath(__file__))
rootDir = os.path.abspath(os.path.join(currDir, '..'))
gameDir = rootDir + "\\Game"
sys.path.append(gameDir)

from GameObject import GameObject
from GameMap import GameMap
import Movement

class MovementTesting(unittest.TestCase):

	def testVectorMoveWithoutCollision(self):
		map = GameMap(1000)
		object = GameObject([0, 0], 'drone', 'owen')
		object.velocity = [1, 2]
		map.addObject(object)

		Movement.vectorMovementWithoutCollision(map, object)
		self.assertEqual(1, 2)

if __name__ == 'main':
	unittest.main()
