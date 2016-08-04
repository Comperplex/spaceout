class GameObject():

	validObjects = ['beacon', 'tower', 'default', 'asteroid', 'fighter', 'defender', 'worker', 'mine', 'scrap'] #Definition list of all possible object type strings

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
		self.mass = 10
		#Variable convention:
		#Player: a string representing the player name the object belongs to. Same for every object the player owns
		#ID: A string that, on instantiation of the object, is set as the objectType + the current count of object the player owns

	def update(self): #Each game object must be updated every tick
		v, a = self.velocity, self.acceleration
		self.velocity = [v[0] + a[0], v[1] + a[1]]

	def getUniqueID(self):
		return self.player + ' ' + self.objectType + ' ' +  str(self.ID)

class Beacon(GameObject):
	def __init__(self, **kwargs):
		GameObject.__init__(kwargs['loc'], 'beacon', kwargs['player'])

class Tower(GameObject):
	def __init__(self, **kwargs):
		GameObject.__init__(kwargs['loc'], 'tower', kwargs['player'])

class Drone(GameObject):
	def __init__(self, **kwargs):
		GameObject.__init__(kwargs['loc'], 'drone' + kwargs['droneType'], kwargs['player'])

class Worker(Drone):
	def __init__(self, **kwargs):
		Drone.__init__(kwargs['loc'], kwargs['player'], droneType='worker')

class Fighter(Drone):
	def __init__(self, **kwargs):
		Drone.__init__(kwargs['loc'], kwargs['player'], droneType='fighter')
