import pygame
from pygame.locals import *

import view.drawer

class View(object):

	def __init__(self, model, resolution):
		pygame.init()

		self.model = model

		self.resolution = resolution
		# Set up the drawing window
		self.screen = pygame.display.set_mode(resolution)
		self.running = True

		self.ally_image = pygame.image.load('./data/assets/ally.png')
		view.drawer.fill(self.ally_image, pygame.Color(0, 0, 255))
		self.ally_image_size = int((self.model.world.width+self.model.world.height)/2.0 * 0.15)
		self.ally_image = pygame.transform.scale(self.ally_image, (self.ally_image_size, self.ally_image_size))
		self.ally_image = pygame.transform.rotate(self.ally_image, -90)

	def run(self):
		# Did the user click the window close button?
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False

		# Fill the background with white
		self.screen.fill((255, 255, 255))

		self.draw_allies()

		# Flip the display
		pygame.display.flip()

	def draw_allies(self):
		for ally in self.model.allies:
			self.screen.blit(pygame.transform.rotate(self.ally_image, -ally.orientation), self.coord_model_to_display(ally.position))

	def coord_model_to_display(self, p):
		view_x = (p[0] / self.model.world.width) * (self.resolution[0]  - self.ally_image_size)
		view_y = (p[1] / self.model.world.height) * (self.resolution[1] - self.ally_image_size)

		return [view_x, view_y]

	def run_until_stopped(self):
		# Run until the user asks to quit

		while self.running:

			self.run()

	def quit(self):
		# Done! Time to quit.
		pygame.quit()