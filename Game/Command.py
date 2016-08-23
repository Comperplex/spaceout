import Movement

class Command():
	def __init__(self, cmd_type, **kwargs):
		self.cmd_type = cmd_type
		self.params = {}
		if cmd_type == 'gotoPoint':
			if 'dest_pt' in kwargs:
				self.dest_pt = kwargs['dest_pt']

	def runCmd(self, gameObject):
		if self.cmd_type == 'drift': #Drift: Moves based on existing acceleration and velocity with NO angle change
			v, a = gameObject.velocity, gameObject.acceleration
			gameObject.velocity = [v[0] + a[0], v[1] + a[1]]

		elif self.cmd_type == 'gotoPoint':
			if 'approach_cnt' not in self.params:
				Movement.newVelocity(gameObject, self.dest_pt) #Assigning default direction and velocity
				gameObject.angle = Movement.getAngle(gameObject.velocity)
				self.params['approach_cnt'] = 0

			speed = Movement.vectMag(gameObject.velocity)
			if Movement.linDist(gameObject.loc, self.dest_pt) <= speed:
				if self.params['approach_cnt'] < 10: #Looped appoximation of setpoint using Zeno's Paradox
					self.params['approach_cnt'] += 1
					Movement.newVelocity(gameObject, self.dest_pt, speed / 2)
				else:
					gameObject.velocity = [0,0]
					self.endCmd()

	def endCmd(self):
		self.cmd_type = 'drift'
		self.params = {}

if __name__ == '__main__':
	command = Command('gotoPoint', dest_pt=[0,0])
