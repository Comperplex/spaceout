class Command():
	def __init__(self, cmd_type, **kwargs):
		self.cmd_type = cmd_type
		if cmd_type == 'gotoPoint':
			if 'dest_pt' in kwargs:
				self.dest_pt = kwargs['dest_pt']

	def runCmd(self, gameObject):
		if self.cmd_type == 'drift':
			v, a = gameObject.velocity, gameObject.acceleration
			gameObject.velocity = [v[0] + a[0], v[1] + a[1]]
		if self.cmd_type == 'gotoPoint':
			if gameObject.loc != self.dest_pt:
				gameObject.newVelocity(self.dest_pt)
			else:
				gameObject.velocity = [0,0]
				self.endCmd()

	def endCmd(self):
		self.cmd_type = 'drift'

if __name__ == '__main__':
	command = Command('gotoPoint', dest_pt=[0,0])
	print(command.dest_pt)
