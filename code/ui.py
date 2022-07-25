import pygame

class UI:
	def __init__(self,surface):
		
		# setup
		self.display_surface = surface
		
		# health
		self.health_bar = pygame.image.load('../graphics/ui/health_bar.png').convert_alpha()
		self.health_bar_topleft = (7,5)
		self.bar_max_width = 56
		self.bar_height = 20
		
		# coins
		self.coin = pygame.image.load('../graphics/ui/coin.png').convert_alpha()
		self.coin_rect = self.coin.get_rect(topleft = (5,30))
		self.font = pygame.font.Font('../graphics/ui/pixel.ttf',13)

	def show_health(self,current,full):
		self.display_surface.blit(self.health_bar,(5,5))
		current_health_ratio =  current / full
		current_bar_width = self.bar_max_width * current_health_ratio
		health_bar_rect = pygame.Rect((24,13),(current_bar_width,4))
		pygame.draw.rect(self.display_surface,'#F16D6D',health_bar_rect)
		
	def show_coins(self,amount):
		self.display_surface.blit(self.coin,self.coin_rect)
		coin_amount_surf = self.font.render(str(amount),False,'black')
		coin_amount_rect = coin_amount_surf.get_rect(midleft = (self.coin_rect.right + 4,self.coin_rect.centery))
		self.display_surface.blit(coin_amount_surf,coin_amount_rect)
