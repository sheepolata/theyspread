import pygame
from pygame.locals import *

import random

import model.world
import model.allies
import view.world

def main():
	_model = model.world.Model(100, 100)
	_view = view.world.View(_model, (1080, 720))

	for i in range(10):
		_model.add_allie(model.allies.Allie((random.random()*100, random.random()*100)))

	_view.run_until_stopped()

	# ally.stop_all()
	_model.stop_all()

if __name__=='__main__':
	main()