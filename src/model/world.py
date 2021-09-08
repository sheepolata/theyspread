import utils

class Element(object):

	def __init__(self, position):
		self.position = position
		self.type = "_generic_el"

class RectangleObstacle(Element):

	def __init__(self, position):
		super().__init__(position)
		self.type = "_rectangle_obstacle"


class World(object):

	def __init__(self, width, height):
		self.width  = width
		self.height = height

		self.elements = []

	def add_element(self, el):
		self.elements.append(el)

class Model(object):

	def __init__(self, w, h):
		self.world = World(w, h)

		self.allies = set()

		self.update_freq = 1/60
		self.update_thread = utils.perpetualTimer(self.update_freq, self.update)
		self.update_thread.start()

	def add_allie(self, al):
		self.allies.add(al)

	def update(self):
		for al in self.allies:
			al.update(self.update_freq, [0, self.world.width], [0, self.world.height])

	def stop_all(self):
		for a in self.allies:
			a.stop_all()
		self.update_thread.cancel()