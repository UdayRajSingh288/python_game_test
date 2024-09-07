import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((720, 480))
fence = pygame.image.load("fence.png").convert_alpha()
tree = pygame.image.load("tree.png").convert_alpha()