import pygame 

#Initialize Pygame and screen dimensions
pygmae.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

#Initialize display surface and set title
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Adding image and background image')

#Load and scale images directly
background_image = pygame.transform.scale(
    pygame.image.load('background.png').convert(),
    (SCREEN_WIDTH, SCREEN_HEIGHT))

penguin_image = pygame.transform.scale(
    pygame.image.load('penguin.png').convert_alpha(), (200, 200))
penguin_rect = penguin_image