import pygame, sys, math, time

from pygame.locals import *
import numpy as np

# set up pygame
pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400

# set up the window
windowSurface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
pygame.display.set_caption('Hello world!')

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# set up fonts
basicFont = pygame.font.SysFont(None, 48)


vel = (0.22, 0.33)
pos = (100, 100)

def update(pos, vel):
    #Update object positions
    newpos = pos[0]+vel[0], pos[1]+vel[1]
    newvel = vel
    if newpos[0] <= 5:
        newvel = newvel[0] * -1, newvel[1]
        newpos = 5, newpos[1]
    if newpos[1] <= 5:
        newvel = newvel[0], newvel[1] * -1
        newpos = newpos[0], 5

    if newpos[0] >= SCREEN_WIDTH-5:
        newvel = newvel[0] * -1, newvel[1]
        newpos = SCREEN_WIDTH-5, newpos[1]
    if newpos[1] >= SCREEN_HEIGHT-5:
        newvel = newvel[0], newvel[1] * -1
        newpos = newpos[0], SCREEN_HEIGHT-5


    pos = newpos
    vel = newvel
    return pos, vel

def draw(fn, t):
    pixArray = pygame.PixelArray(windowSurface)
    # for y in range(SCREEN_HEIGHT):
    #     for x in range(SCREEN_WIDTH):
    #         c = fn(x, y, t)
    a = np.indices((SCREEN_WIDTH, SCREEN_HEIGHT))
    # print(a.shape)
    a = (np.sinc((a[0]-250))) * np.sinc((a[1]-200))
    # print(a.shape)
    a = np.repeat(a[:, :, np.newaxis], 3, axis=2)
    # print(a.shape)
    a[a < 0] = 0
    a[a > 1] = 1
    a *= 255
    
    a = np.floor(a)
    b = a.tolist()


    for j in range(SCREEN_HEIGHT):
        for i in range(SCREEN_WIDTH):
            pixArray[i,j] = tuple(b[i][j])
    del pixArray

def dist(x, y, t):
    return (((math.sin(1/5*x) + math.sin(1/5*y+t)) /2)*0.5)+0.5

# run the game loop
if __name__ == "__main__":
    t = 0
    while True:
        # pos,vel = update(pos, vel)
        t += 1

        # draw the white background onto the surface
        windowSurface.fill(WHITE)

        draw(dist, t)
        # draw the window onto the screen
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()