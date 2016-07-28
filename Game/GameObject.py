class GameObject:

	def __init__(self, loc, objectType, player):
		#Static attributes:
		self.loc = loc
		self.objectType = objectType
		self.ID = 0
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
