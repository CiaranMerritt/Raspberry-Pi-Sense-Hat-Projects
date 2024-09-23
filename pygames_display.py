# Example file showing a circle moving on screen
import pygame
from pygame.locals import *
from sense_hat import SenseHat

# pygame setup
pygame.init()
pygame.font.init()
# Set up the font object
font = pygame.font.Font(None, 20)
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()


sense = SenseHat()

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

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    orientation = sense.get_orientation()
    pitch_text = font.render(f'Pitch: {orientation["pitch"]}', True, (255, 255, 255))
    roll_text = font.render(f'Roll: {orientation["roll"]}', True, (255, 255, 255))
    yaw_text = font.render(f'Yaw: {orientation["yaw"]}', True, (255, 255, 255))
    screen.blit(pitch_text, (10, 30))
    screen.blit(roll_text, (10, 50))
    screen.blit(yaw_text, (10, 70))

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()