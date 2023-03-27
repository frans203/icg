import pygame
from pygame.locals import *

PIXEL_SIZE = 1
SCREEN_WIDTH, SCREEN_HEIGHT = 512, 512

surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT)) #surface instance
surf.fill((0,0,0)) #filling surface with black color 

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
    
    dx <<= 2 #multiplying this variables by 4, to achive more precise and smooth results of line drawing
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

pygame.init() #initialize pygame
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #creates scren surface with the height and width variables
pygame.display.set_caption("Line Drawing") #set the title of the window
clock = pygame.time.Clock() #creating instance of Clock to set framerate

running = True
while running:
    put_pixel(30, 30)
    draw_line(40, 40, 60, 60)
    draw_triangle(100, 100, 200, 200, 400, 100) #the points toguether should be possible to create a triangle
    for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

    if running:
        clock.tick(60) #framerate to 60fps

        screen.blit(surf, (0, 0)) #draw surf surface onto the screen surface
        pygame.display.update() #updates any changes of the screen 