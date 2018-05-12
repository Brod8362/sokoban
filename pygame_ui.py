import pygame
from contextlib import contextmanager
class UI():
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((720,540))
		self.sprites = {
		'player':pygame.image.load("img/player.png"),
		'box':pygame.image.load("img/box.png"),
		'boxDone':pygame.image.load("img/box_in_goal.png"),
		'goal':pygame.image.load("img/goal.png"),
		'ground':pygame.image.load("img/ground.png"),
		'wall':pygame.image.load("img/wall.png")
		}
		self.reference = {
		0:self.sprites['ground'],
		1:self.sprites['wall'],
		2:self.sprites['ground'],
		3:self.sprites['ground'],
		4:self.sprites['goal'],
		5:self.sprites['goal']
		}
		self.twidth = pygame.Surface.get_width(self.reference[0])
		self.theight = pygame.Surface.get_height(self.reference[0])
		self.done = False
		self.clock = pygame.time.Clock()
	@contextmanager
	def setup(self):
		yield
	
	def get_input(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_w:
						return "w"
					elif event.key == pygame.K_s:
						return "s"
					elif event.key == pygame.K_a:
						return "a"
					elif event.key == pygame.K_d:
						return "d"	
					elif event.key == pygame.K_q:
						sys.exit()
	def draw_entity_at(self,ent,x=None,y=None): #add specifc cords later
		if ent.isBox():
			if ent.checkSatisfied():
				self.screen.blit(self.reference[0], (ent.x*self.twidth,ent.y*self.theight))
				self.screen.blit(self.sprites['boxDone'], (ent.x*self.twidth, ent.y*self.theight))
			else:
				self.screen.blit(self.reference[0], (ent.x*self.twidth,ent.y*self.theight))
				self.screen.blit(self.sprites['box'], (ent.x*self.twidth, ent.y*self.theight))
		if ent.isBox() == False:
			self.screen.blit(self.reference[0], (ent.x*self.twidth,ent.y*self.theight))
			self.screen.blit(self.sprites['player'], (ent.x*self.twidth, ent.y*self.theight))
	def draw_tile_at(self,tile,x,y,tileset):
			self.screen.blit(self.reference[0], (x*self.twidth,y*self.theight))
			self.screen.blit(self.reference[tile], (x*self.twidth,y*self.theight))
	def clear(self):
		self.screen.fill((0,0,0))
	def update(self):
		pygame.display.flip()
		pygame.clock.tick(60)
		
