import pygame as pg
import pygame.gfxdraw as gfxdraw
import math, random
import sys


######init
pg.init()
screen = pg.display.set_mode((800,600))

running = True


surf = pg.Surface( (50,50) )
surf.fill((255,255,255))
rect = surf.get_rect()
screen.blit(surf, (400,300))
pg.display.flip()

while running:
    
    for event in pg.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

