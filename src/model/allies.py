import utils
import random
import math

class Entity(object):

	def __init__(self):
		self.type = "entity"

class Allie(Entity):

	def __init__(self, position):
		super().__init__()
		self.type = "allie"

		self.position = [position[0], position[1]]
		self.orientation = 0

		self.pv_max = 10.0
		self.pv = self.pv_max
		self.regen_health = utils.perpetualTimer(1, self.regenerate_health)
		self.regen_health.start()

		self.bullets_max = 5
		self.bullets = self.bullets_max
		self.regen_bullets = utils.perpetualTimer(1, self.regenerate_bullets)
		self.regen_bullets.start()

		self.random_walk = utils.perpetualTimer(2, self.randomly_change_direction)
		self.random_walk.start()

		self.speed = 10.0

	def update(self, delta, limits_x, limits_y):
		# Move
		new_x = self.position[0] + self.speed * delta * math.cos(math.radians(self.orientation))
		new_y = self.position[1] + self.speed * delta * math.sin(math.radians(self.orientation))

		while new_x > limits_x[1] or new_x < limits_x[0] or new_y > limits_y[1] or new_y < limits_y[0]:
			self.randomly_change_direction()
			new_x = self.position[0] + self.speed * delta * math.cos(math.radians(self.orientation))
			new_y = self.position[1] + self.speed * delta * math.sin(math.radians(self.orientation))

		self.position = [new_x, new_y]

	def randomly_change_direction(self):
		self.orientation = (self.orientation + (random.random()*70)-35)%360

	def regenerate_bullets(self):
		self.bullets = min(self.bullets_max, self.bullets + 1)

	def regenerate_health(self):
		self.pv = min(self.pv_max, self.pv + 0.1)

	def stop_all(self):
		self.regen_bullets.cancel()
		self.regen_health.cancel()
		self.random_walk.cancel()
