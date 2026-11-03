import pygame
import random

import pixel
import update

pygame.init()

WIDTH = 700
HEIGHT = 700

size = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))

def paint(pixels, pos, state):
    for i in range(-3, 4):
        for j in range(-3, 4):
            newi = round(pos[0] / size) + i
            newj = round(pos[1] / size) + j
            if state == 'sand':
                if newj >= WIDTH / size or newj < 0 or newi >= HEIGHT / size or newi < 0 or round(random.random() -0.1) == 1:
                    continue
                pixels[newi][newj].state = state
            elif newj >= WIDTH / size or newj < 0 or newi >= HEIGHT / size or newi < 0:
                continue    
            pixels[newi][newj].state = state

def main():
    run = True

    clock = pygame.time.Clock()

    state = 'sand'

    pixels = [[pixel.Pixel(j, i, 'air') for i in range(int(WIDTH / size))] for j in range(int(HEIGHT / size))]

    while run:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    state = 'sand'
                elif event.key == pygame.K_2:
                    state = 'brick'
                elif event.key == pygame.K_3:
                    state = 'water'

        screen.fill('black')

        buttons = pygame.mouse.get_pressed()
        if buttons[0]:
            paint(pixels, pygame.mouse.get_pos(), state)
        elif buttons[2]:
            paint(pixels, pygame.mouse.get_pos(), 'air')

        pixels = update.update(pixels)

        for i in range(len(pixels)):
            for j in range(len(pixels[0])):
                pixels[i][j].draw(screen, size)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()