import pygame 

pygame.init()

display_width = 800 #Ширина дисплея 
display_height = 600 #Высота дисплея 

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("DinoGame!")

icon = pygame.image.load('Backgrounds/icon.png')
pygame.display.set_icon(icon)

usr_width = 60
usr_height = 100
usr_x = 20 
usr_y = display_height - usr_height - 100

Clock = pygame.time.Clock()

make_Jump = False
jump_counter = 30

def run_game():
	global make_Jump
	game = True

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

		pygame.draw.rect(display, (0, 255, 0), (usr_x, usr_y, usr_width, usr_height))

		pygame.display.update()

		Clock.tick(60)
def jump():
	global usr_y, jump_counter, make_Jump
	if jump_counter >= -30:
		usr_y -= jump_counter / 2.5 
		jump_counter -=1 
	else:
		jump_counter = 30 
		make_Jump = False 


run_game()