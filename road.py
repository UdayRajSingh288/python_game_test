import pygame;

class Road:
	def __init__(self):
		self._surf: pygame.Surface = pygame.image.load("road.png").convert();
		self._rect: pygame.Rect = self._surf.get_rect();

	def draw(self, screen: pygame.Surface):
		screen.blit(self._surf, self._rect);
"""
if __name__ == "__main__":
	pygame.init();
	screen: pygame.Surface = pygame.display.set_mode((720, 480));
	road: Road = Road();
	i: int = 1;
	road.draw(screen);
	pygame.display.update();
	while (i):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				i = 0;
	pygame.quit();
"""