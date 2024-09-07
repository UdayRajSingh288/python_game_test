import pygame

class Layer:
	def __init__(self, surflist):
		self.canvas = pygame.Surface((720, 480))
		for surf in surflist:
			