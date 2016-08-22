import Movement

class Command():
	def __init__(self, cmd_type, **kwargs):
		self.cmd_type = cmd_type
		self.exec_count = 0 #this is kinda a hack, will make it better later
		if cmd_type == 'gotoPoint':
			if 'dest_pt' in kwargs:
				self.dest_pt = kwargs['dest_pt']

	def runCmd(self, gameObject):
		if self.cmd_type == 'drift':
			v, a = gameObject.velocity, gameObject.acceleration
			gameObject.velocity = [v[0] + a[0], v[1] + a[1]]
		elif self.cmd_type == 'gotoPoint':
			if self.exec_count == 0:
				Movement.newVelocity(gameObject, self.dest_pt) #Assigning default direction and speed
				self.exec_count += 1
			speed = Movement.vectMag(gameObject.velocity)
			if Movement.linDist(gameObject.loc, self.dest_pt) <= speed:
				if self.exec_count < 10: #Looped appoximation of setpoint using Zeno's Paradox
					self.exec_count += 1
					Movement.newVelocity(gameObject, self.dest_pt, speed / 2)
				else:
					gameObject.velocity = [0,0]
					self.endCmd()

	def endCmd(self):
		self.cmd_type = 'drift'
		self.exec_count = 0

if __name__ == '__main__':
	command = Command('gotoPoint', dest_pt=[0,0])
