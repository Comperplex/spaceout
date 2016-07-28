class GameObject:

	def __init__(self, loc, name, player):
		self.loc = loc
		self.name = name
		self.player = player

		#Variable convention:
		#Player: a string representing the player name the object belongs to. Same for every object the player owns
		#name: a string representing the specific object within the player's arsenal. Written as 'objectType' + 'objectNumber'
			#Where object type is one of the standard gameobjects, and objectNumber is the numeric index of the specific object
