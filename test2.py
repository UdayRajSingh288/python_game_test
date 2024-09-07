import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((720, 480))
clock = pygame.time.Clock()
mario = pygame.image.load("mario.png").convert_alpha()
rect = mario.get_rect(center = (360, 240))
scale = 1.0
rate = 0.05
zoom_in = False
zoom_out = False
mario_2 = mario
offset_x = 0
go_left = False
go_right = False
sky_surf = pygame.image.load("sky1.png").convert()
sky_rect = sky_surf.get_rect(center = (360, 120))
ground_surf = pygame.image.load("ground1.png").convert()
offset_y = 0
ground_rect_1 = ground_surf.get_rect(midbottom = (360, 480 + offset_y))
ground_rect_2 = ground_surf.get_rect(midbottom = (360, 240 + offset_y))
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				zoom_in = True
			elif event.key == pygame.K_s:
				zoom_out = True
			if event.key == pygame.K_a:
				go_left = True
			elif event.key == pygame.K_d:
				go_right = True
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_w:
				zoom_in = False
			elif event.key == pygame.K_s:
				zoom_out = False
			if event.key == pygame.K_a:
				go_left = False
			elif event.key == pygame.K_d:
				go_right = False
	if zoom_in:
		scale += rate
		mario_2 = pygame.transform.scale_by(mario, scale)
		offset_y += 10
	elif zoom_out:
		scale -= rate
		mario_2 = pygame.transform.scale_by(mario, scale)
		offset_y -= 10
	if go_left:
		offset_x += 10
	elif go_right:
		offset_x -= 10
	rect = mario_2.get_rect(center = (360 + offset_x, 240))
	if offset_y < 0:
		offset_y = 0
	elif offset_y > 480:
		offset_y = 480
	screen.fill((0, 0, 0))
	ground_rect_1 = ground_surf.get_rect(midbottom = (360, 480 + offset_y))
	ground_rect_2 = ground_surf.get_rect(midbottom = (360, 240 + offset_y))
	screen.blit(ground_surf, ground_rect_1)
	screen.blit(ground_surf, ground_rect_2)
	screen.blit(sky_surf, sky_rect)
	if rect.top >= -100 and rect.bottom <= 580:
		screen.blit(mario_2, rect)
#	print(scale)
	pygame.display.update()
	clock.tick(24)