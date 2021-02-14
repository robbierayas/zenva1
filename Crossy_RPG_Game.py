# Pygame development 3
#draw objects to screen
# load images into objects

import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = 'Crossy RPG'
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
clock = pygame.time.Clock()
TICK_RATE = 60
is_game_over = False

# Create window of specified size in white to display the game
game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Set the game window color to white
game_screen.fill(WHITE_COLOR)
pygame.display.set_caption(SCREEN_TITLE)

# load images
player_image = pygame.image.load('player.png')
# scale the image up
player_image = pygame.transform.scale(player_image, (50, 50))
while not is_game_over:

    # loop to get all the events
    for event in pygame.event.get():
        # if we have a quit type evemt, then exit
        if event.type == pygame.QUIT:
            is_game_over = True
        print(event)

    # Draw a rectangle
    # pygame.draw.rect(game_screen, BLACK_COLOR, [350, 350, 100, 100])
    #Draw a circle
    # pygame.draw.circle(game_screen, BLACK_COLOR, (400, 300), 50)

    #draw player image
    game_screen.blit(player_image, (375, 375))

    #update all game graphics
    pygame.display.update()
    #tick the clock to update everything in the game
    clock.tick(TICK_RATE)

# quit pygame and the program
pygame.quit()
quit()
