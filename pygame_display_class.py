import pygame
from pygame.locals import *

class PygameDisplay(object):

    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()

    def __init__(self) -> None:
        pygame.init()
        pygame.font.init() 
        pass

    def runngGame(self):
        
        running = True
        dt = 0

        while running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

            self.run()

            # flip() the display to put your work on screen
            pygame.display.flip()

            # limits FPS to 60
            # dt is delta time in seconds since last frame, used for framerate-
            # independent physics.
            dt = self.clock.tick(60) / 1000

        pygame.quit()