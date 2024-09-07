import pygame
from sys import exit
from random import randint

def display_score():
	current_time = int(pygame.time.get_ticks() / 1000) - start_time
	score_surf = test_font.render(f"Score: {current_time}", False, (64, 64, 64))
	score_rect = score_surf.get_rect(center = (400, 50))
	screen.blit(score_surf, score_rect)
	return current_time

def obstacle_movement(obstacle_list):
	if obstacle_list:
		for obstacle_rect in obstacle_list:
			obstacle_rect.x -= 5
			if obstacle_rect.bottom == 300:
				screen.blit(snail_surf, obstacle_rect)
			else:
				screen.blit(fly_surf, obstacle_rect)
		obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.right > 0]
	return obstacle_list

def collisions(player, obstacles):
	if obstacles:
		for obstacle in obstacles:
			if player.colliderect(obstacle):
				return False
	return True

def player_animation():
	global player_surf, player_index
	if player_rect.bottom < 300:
		player_surf = player_jump
	else:
		player_index += 0.1
		if player_index >= len(player_walk):
			player_index = 0
		player_surf = player_walk[int(player_index) % 2]

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)

sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground_surface = pygame.image.load("graphics/Ground.png").convert()

game_active = False
start_time = 0
score = 0

snail_frame_1 = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_frame_2 = pygame.image.load("graphics/snail/snail2.png").convert_alpha()
snail_frames = [snail_frame_1, snail_frame_2]
snail_frame_index = 0
snail_surf = snail_frames[snail_frame_index]

fly_frame_1 = pygame.image.load("graphics/fly/fly1.png").convert_alpha()
fly_frame_2 = pygame.image.load("graphics/fly/fly2.png").convert_alpha()
fly_frames = [fly_frame_1, fly_frame_2]
fly_frame_index = 0
fly_frame = fly_frames[fly_frame_index]

obstacle_rect_list = []

player_walk_1 = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
player_walk_2 = pygame.image.load("graphics/player/player_walk_2.png").convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_jump = pygame.image.load("graphics/player/jump.png").convert_alpha()

player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom = (80, 300))
player_gravity = 0

player_stand = pygame.image.load("graphics/player/player_stand.png").convert_alpha()
player_stand = pygame.transform.scale2x(player_stand)
player_stand_rect = player_stand.get_rect(center = (400, 200))

player_jump_sound = pygame.mixer.Sound("audio/jump.mp3")
player_jump_sound.set_volume(0.5)

game_name = test_font.render("Pixel Runner", False, (111, 196, 169))
game_name_rect = game_name.get_rect(center = (400, 80))

game_message = test_font.render("Press space to run", False, (111, 196, 169))
game_message_rect = game_message.get_rect(center = (400, 330))

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

bg_music = pygame.mixer.Sound("audio/music.wav")

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		if game_active:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
					player_gravity = -20
					player_jump_sound.play()
			if event.type == obstacle_timer:
				if randint(0, 2):
					obstacle_rect_list.append(snail_surf.get_rect(bottomright = (randint(900, 1100), 300)))
				else:
					obstacle_rect_list.append(snail_surf.get_rect(bottomright = (randint(900, 1100), 210)))
			if event.type == snail_animation_timer:
				if snail_frame_index == 0:
					snail_frame_index = 1
				else:
					snail_frame_index = 0
				snail_surf = snail_frames[snail_frame_index]
			if event.type == fly_animation_timer:
				if fly_frame_index == 0:
					fly_frame_index = 1
				else:
					fly_frame_index = 0
				fly_surf = fly_frames[fly_frame_index]
		else:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					game_active = True
					start_time = int(pygame.time.get_ticks() / 1000)
					bg_music.play(loops = -1)

	if game_active:
		screen.blit(sky_surface, (0, 0))
		screen.blit(ground_surface, (0, 300))

		score = display_score()

		player_gravity += 1
		player_rect.y += player_gravity
		if player_rect.bottom > 300:
			player_rect.bottom = 300
		player_animation()
		screen.blit(player_surf, player_rect)

		obstacle_rect_list = obstacle_movement(obstacle_rect_list)

		game_active = collisions(player_rect, obstacle_rect_list)
		if game_active == False:
			bg_music.stop()
	else:
		screen.fill((98, 129, 162))
		screen.blit(player_stand, player_stand_rect)
		obstacle_rect_list.clear()
		player_rect.midbottom = (80, 300)
		player_gravity = 0
		
		screen.blit(game_name, game_name_rect)
		score_message = test_font.render(f"Your score: {score}", False, (111, 196, 169))
		score_message_rect = score_message.get_rect(center = (400, 330))
		if score == 0:
			screen.blit(game_message, game_message_rect)
		else:
	
			screen.blit(score_message, score_message_rect)

	pygame.display.update()
	clock.tick(60)