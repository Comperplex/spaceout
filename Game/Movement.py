import math

def vectorMovementWithoutCollision(gameMap, gameObject): #Returns True if successful and false otherwise
	new_loc = [0,0]
	new_loc[0] = gameObject.loc[0] + gameObject.velocity[0]
	new_loc[1] = gameObject.loc[1] + gameObject.velocity[1]
	if(withinArea(new_loc, 'rectangle', bot_pt=[0,0], top_pt=gameMap.size)):
		gameObject.loc = new_loc
		return True
	else:
		return False

def vectorMovementWithCollision(gameMap, gameObject):
	obstacles = gameMap.gameObjects

def withinArea(point, shape, **kwargs): #Will be useful for collision
	if(shape == 'rectangle'):
		if set(['bot_pt', 'top_pt']).issubset(kwargs): #boundary points, defined as the bottom left and upper right corners of the rect
			return point[0] >= kwargs['bot_pt'][0] and point[0] <= kwargs['top_pt'][0] and point[1] >= kwargs['bot_pt'][1] and point[1] <= kwargs['top_pt'][1]
	elif(shape == 'circle'):
		pass

def newVelocity(gameObject, goTo, speed=20):
	a, b = gameObject.loc, goTo
	disp = [b[0]-a[0], b[1]-a[1]]
	distance = linDist(a,b)
	gameObject.velocity = [disp[0]*(speed/distance), disp[1]*(speed/distance)]

def linDist(p1, p2):
	disp = [p2[0]-p1[0], p2[1]-p1[1]]
	return math.sqrt(disp[0]**2 + disp[1]**2)

def vectMag(v):
	return math.sqrt(sum(x**2 for x in v))

class MovementRule:

	def __init__(self):
		pass
