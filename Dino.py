import pygame
import random

pygame.init()

display_width = 800 #Ширина дисплея
display_height = 600 #Высота дисплея

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("DinoGame!")

icon = pygame.image.load('Backgrounds/icon.png')
pygame.display.set_icon(icon)

cactus_img = [pygame.image.load('Objects/Cactus0.png'),pygame.image.load('Objects/Cactus1.png'),pygame.image.load('Objects/Cactus2.png')]

cactus_options = [69, 449, 37, 410, 40, 420]


class Cactus:
	def __init__(self, x, y, width, image, speed):
		self.x = x
		self.y = y
		self.width = width
		self.image = image
		self.speed = speed

	def move(self):
		if self.x >= -self.width:
			display.blit(self.image, (self.x, self.y))
			# pygame.draw.rect(display, (0, 255, 0), (self.x, self.y, self.width, self.height))
			self.x -= self.speed
			return True
		else:
			# self.x = display_width + 100 + random.randrange(-80, 60)
			return False

	def return_self(self, radius, y, width, image):
		self.x = radius
		self.y = y
		self.width = width
		self.image = image
		display.blit(self.image, (self.x, self.y))


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
	land = pygame.image.load('Backgrounds/Land.jpg')

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

		display.blit(land, (0, 0))
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
	choice = random.randrange(0, 3)
	img = cactus_img[choice]
	width =  cactus_options[choice * 2]
	height = cactus_options[choice * 2 + 1]
	array.append(Cactus(display_width + 20, height, width, img, 4))

	choice = random.randrange(0, 3)
	img = cactus_img[choice]
	width =  cactus_options[choice * 2]
	height = cactus_options[choice * 2 + 1]
	array.append(Cactus(display_width + 300, height, width, img, 4))

	choice = random.randrange(0, 3)
	img = cactus_img[choice]
	width =  cactus_options[choice * 2]
	height = cactus_options[choice * 2 + 1]
	array.append(Cactus(display_width + 600, height, width, img, 4))

def find_radius(array):
	maximum = max(array[0].x, array[1].x, array[2].x)

	if maximum < display_width:
		radius = display_width
		if radius - maximum < 50:
			radius += 150
	else:
		radius = maximum

	choice = random.randrange(0, 5)
	if choice == 0:
		radius += random.randrange(10, 15)
	else:
		radius += random.randrange(200, 350)

	return radius

def draw_array(array):

	for cactus in array:
		check = cactus.move()
		if not check:
			radius = find_radius(array)

			choice = random.randrange(0, 3)
			img = cactus_img[choice]
			width =  cactus_options[choice * 2]
			height = cactus_options[choice * 2 + 1]


			cactus.return_self(radius, height, width, img)



run_game()




# ЕЕеееее это работает !!!
