from pygame_display_class import PygameDisplay

# Example file showing a circle moving on screen

import pygame
from pygame.locals import *
from sense_hat import SenseHat


class test(PygameDisplay):
    

    def __init__(self) -> None:
        PygameDisplay.__init__(self)
        self.font = pygame.font.Font(None, 20)
        self.sense = SenseHat()
        pass

    def run(self):
        # fill the screen with a color to wipe away anything from last frame
        PygameDisplay.screen.fill("black")

        orientation = self.sense.get_orientation()
        pitch_text = self.font.render(f'Pitch: {orientation["pitch"]}', True, (255, 255, 255))
        roll_text = self.font.render(f'Roll: {orientation["roll"]}', True, (255, 255, 255))
        yaw_text = self.font.render(f'Yaw: {orientation["yaw"]}', True, (255, 255, 255))
        PygameDisplay.screen.blit(pitch_text, (10, 30))
        PygameDisplay.screen.blit(roll_text, (10, 50))
        PygameDisplay.screen.blit(yaw_text, (10, 70))

    def quit(self):
        self.sense.clear()

game = test()

game.runngGame()