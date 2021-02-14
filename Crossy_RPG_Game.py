# Pygame development 3
#draw objects to screen
# load images into objects

import pygame

#size of the screen
SCREEN_TITLE = 'Crossy RPG'
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
# colors according to RGB
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
 # clock used to update game events
clock = pygame.time.Clock()

class Game:

     # typical rate of 60
    TICK_RATE = 60

    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        # Create window of specified size in white to display the game
        self.game_screen = pygame.display.set_mode((width, height))
        # Set the game window color to white
        self.game_screen.fill(WHITE_COLOR)
        pygame.display.set_caption(title)

    def run_game_loop(self):
        is_game_over = False

        # main game loop
        while not is_game_over:

            # loop to get all the events
            for event in pygame.event.get():
                # if we have a quit type evemt, then exit
                if event.type == pygame.QUIT:
                    is_game_over = True
                print(event)

            # Draw a rectangle
            # pygame.draw.rect(game_screen, BLACK_COLOR, [350, 350, 100, 100])
            # Draw a circle
            # pygame.draw.circle(game_screen, BLACK_COLOR, (400, 300), 50)

            # draw player image
            # game_screen.blit(player_image, (375, 375))

            # update all game graphics
            pygame.display.update()
            # tick the clock to update everything in the game
            clock.tick(self.TICK_RATE)

pygame.init()

new_game = Game(SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop()

# load images
# player_image = pygame.image.load('player.png')
# scale the image up
# player_image = pygame.transform.scale(player_image, (50, 50))


# quit pygame and the program
pygame.quit()
quit()
