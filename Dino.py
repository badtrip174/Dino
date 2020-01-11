import pygame 

pygame.init()

display_width = 800 #Ширина дисплея 
display_height = 600 #Высота дисплея 

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("DinoGame!")

icon = pygame.image.load('Backgrounds/icon.png')
pygame.display.set_icon(icon)

class Cactus:
	def __init__(self, x, y, width, height, speed):
		self.x = x 
		self.y = y 
		self.width = width
		self.height = height
		self.speed = speed

	def move(self):
		if self.x >= -self.width:
			pygame.draw.rect(display, (0, 255, 0), (self.x, self.y, self.width, self.height))
			self.x -= self.speed

		else:
			self.x = display_width - 50


usr_width = 60
usr_height = 100
usr_x = 20 
usr_y = display_height - usr_height - 100

cactus_width = 20
cactus_height = 70 
cactus_x = display_width - 50
cactus_y = display_height - cactus_height - 100

Clock = pygame.time.Clock()

make_Jump = False
jump_counter = 30

def run_game():
	global make_Jump
	game = True
	cactus_arr = []
	create_cactus_arr(cactus_arr)

	while game:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		keys = pygame.key.get_pressed()
		if keys[pygame.K_SPACE]:
			make_Jump = True


		if make_Jump:
			jump()

		display.fill((255, 255, 255))
		draw_array(cactus_arr)

		pygame.draw.rect(display, (255, 0, 0), (usr_x, usr_y, usr_width, usr_height))

		pygame.display.update()

		Clock.tick(60)
def jump():
	global usr_y, jump_counter, make_Jump
	if jump_counter >= -30:
		usr_y -= jump_counter / 2.5 
		jump_counter -= 1 
	else:
		jump_counter = 30 
		make_Jump = False 

def create_cactus_arr(array):
	array.append(Cactus(display_width - 50, display_height - 170, 20, 70, 4))
	array.append(Cactus(display_width + 50, display_height - 150, 30, 50, 4))
	array.append(Cactus(display_width + 50, display_height - 180, 25, 80, 4)) 

def draw_array(array):

	for Cactus in array:
		Cactus.move()


run_game()