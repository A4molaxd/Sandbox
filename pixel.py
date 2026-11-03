import pygame

class Pixel():
    def __init__(self, x, y, state):
        self.x = x
        self.y = y
        self.state = state
        self.color = 'white'

    def draw(self, screen, size):
        pygame.draw.rect(screen, self.color, (self.x * size, self.y * size, size, size))