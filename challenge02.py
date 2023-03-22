import pygame
from pygame.locals import *

PIXEL_SIZE = 3
SCREEN_WIDTH, SCREEN_HEIGHT = 512, 512

surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
surf.fill((0,0,0))

def put_pixel(x,y):
    global surf 
    pygame.draw.rect(surf, (255, 0, 0), (x * PIXEL_SIZE, y * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

def draw_line(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    if dy < 0:
        dy = -dy
        stepy = -1
    else: 
        stepy = 1
    
    if dx < 0:
        dx = -dx
        stepy = 1
    else:
        stepx = 1
    
    dx <<= 2
    dy <<= 2
   

    put_pixel(x0, y0)

    if dx > dy: 
        fraction = dy - (dx >> 1)
        while x0 != x1:
            if fraction >= 0: 
                y0 += stepy
                fraction -= dx
            x0 += stepx
            fraction += dy
            put_pixel(x0, y0)
    else:
        fraction = dx - (dy >> 1)
        while y0 != y1:
            if fraction >= 0:
                x0 += stepx
                fraction -= dy
            y0 += stepy
            fraction += dx
            put_pixel(x0, y0)


def draw_triangle(x0, y0, x1, y1, x2, y2):
    draw_line(x0, y0, x1, y1)
    draw_line(x0, y0, x2, y2)
    draw_line(x1, y1, x2, y2)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Line Drawing")
clock = pygame.time.Clock()

running = True
while running:
    put_pixel(30, 30)
    draw_line(40, 40, 60, 60)
    draw_triangle(10, 10, 20, 20, 40, 10) #the points toguether should be possible to create a triangle
    for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

    if running:
        clock.tick(60)

        screen.blit(surf, (0, 0))
        pygame.display.update()