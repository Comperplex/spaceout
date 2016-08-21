import math

class GameObject():

	validObjects = ['beacon', 'tower', 'default', 'drone', 'asteroid', 'mine', 'scrap', 'worker', 'fighter'] #Definition list of all possible object type strings

	def __init__(self, loc, objectType, player):
		#Static attributes:
		self.loc = loc

		if(objectType in self.validObjects):
			self.objectType = objectType
		else:
			self.objectType = 'default'

		self.ID = None
		self.player = player

		#Dynamic attributes:
		self.velocity = [0, 0] #Velocity vector. For example: [1, 0] refers to positive x direction at 1 unit per second
		self.acceleration = [0, 0]
		self.mass = {'beacon':1000, 'tower':100, 'default':10, 'drone':10, 'asteroid':5, 'mine':1, 'scrap':1, 'worker':10, 'fighter':15}[self.objectType] #Get mass from dictionary according to the object type

		#Variable convention:
		#Player: a string representing the player name the object belongs to. Same for every object the player owns
		#ID: A unique ID that is dynamically assigned for each gameObject on the map. In the form player,objectType,number

	def update(self): #Each game object must be updated every tick
		v, a = self.velocity, self.acceleration
		self.velocity = [v[0] + a[0], v[1] + a[1]]

	def newVelocity(self, goTo):
		a, b, v = self.loc, goTo, self.velocity
		disp = [b[0]-a[0], b[1]-a[1]]
		distance = math.sqrt( disp[0]**2 + disp[1]**2 )
		speed = math.sqrt( v[0]**2 + v[1]**2 )
		self.velocity = [disp[0]*(speed/distance), disp[1]*(speed/distance)]

class Beacon(GameObject):
	def __init__(self, **kwargs):
		if('beaconType' in kwargs): #objectType support for multiple types of beacons
			objectType = kwargs['beaconType']
		else:
			objectType = 'beacon'

		GameObject.__init__(self, kwargs['loc'], objectType, kwargs['player'])

	def update(self): #Overrides update() in parent class
		GameObject.update(self)
		#include object specific update code here

class Tower(GameObject):
	def __init__(self, **kwargs):
		if('towerType' in kwargs): #objectType support for multiple types of towers
			objectType = kwargs['towerType']
		else:
			objectType = 'tower'

		GameObject.__init__(self, kwargs['loc'], objectType, kwargs['player'])

	def update(self): #Overrides update() in parent class
		GameObject.update(self)
		#include object specific update code here

class Drone(GameObject):
	def __init__(self, **kwargs):
		if('droneType' in kwargs): #objectType support for multiple types of drones
			objectType = kwargs['droneType']
		else:
			objectType = 'drone'

		GameObject.__init__(self, kwargs['loc'], objectType, kwargs['player'])

	def update(self): #Overrides update() in parent class
		GameObject.update(self)
		#include object specific update code here

class Worker(Drone):
	def __init__(self, **kwargs):
		Drone.__init__(self, droneType='worker', **kwargs)

	def update(self): #Overrides update() in parent class
		Drone.update(self)
		#include object specific update code here

class Fighter(Drone):
	def __init__(self, **kwargs):
		Drone.__init__(self, droneType='fighter', **kwargs)

	def update(self): #Overrides update() in parent class
		Drone.update(self)
		#include object specific update code here

class Asteroid(GameObject):
	def __init__(self, **kwargs):
		if('asteroidType' in kwargs): #objectType support for multiple types of beacons
			objectType = kwargs['asteroidType']
		else:
			objectType = 'asteroid'

		GameObject.__init__(self, kwargs['loc'], objectType, kwargs['player'])

	def update(self): #Overrides update() in parent class
		GameObject.update(self)
		#include object specific update code here
