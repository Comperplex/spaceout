import unittest
import os, sys

currDir = os.path.dirname(os.path.realpath(__file__))
rootDir = os.path.abspath(os.path.join(currDir, '..'))
gameDir = rootDir + "\\Game"
sys.path.append(gameDir)

from GameObject import Drone, Worker, GameObject

class GameObjectTest(unittest.TestCase):

	def testDrone(self):
		drone = Drone(loc=[0,0], player='sammy')
		self.assertEqual(drone.objectType, 'drone') #Testing object type
		self.assertIsInstance(drone, GameObject) #Testing instantiation of parent class

	def testWorker(self):
		worker = Worker(loc=[0,0], player='owen')
		self.assertEqual(worker.objectType, 'worker')
		self.assertIsInstance(worker, Drone) #Testing instantiation of parent class
		self.assertIsInstance(worker, GameObject) #Testing instantiation of parent's parent class

if __name__ == '__main__':
	unittest.main()
