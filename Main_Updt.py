import pygame
import time
import random
import numpy as np
import os
import Grid_Updt
from pygame.locals import *

os.environ["SDL_VIDEO_CENTERED"]='1'

#resolution
width, height = 900,600
size = (width, height)

pygame.init()

pygame.display.set_caption("CONWAY'S GAME OF LIFE")

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 15

black = (0, 0, 0)

white = (255, 255, 255)
red = (153,0,0)
green = (0,102,0)

scaler = 30
offset = 3
Location = None
Grid = Grid_Updt.Grid(width,height, scaler, offset)
Grid.random2d_array()
pause = False
run = True

pos = pygame.mouse.get_pos()
Location = (None, None)
Random_colors = []
i = 0
while i < 100 :
    Random_colors.append((random.randint(0,190),random.randint(0,180),random.randint(0,160)))
    i += 1
Random = False                          
while run:
    color = 0
    clock.tick(fps)
    screen.fill(black)
    state =0
    # 0 for neutral, 1 for birth, 2 for death
    for event in pygame.event.get():
        if event.type == QUIT: 
            run = False
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                run = False
            if event.key ==  K_SPACE:
                pause = not pause
            if event.key == K_r:
                Grid.random2d_array()    
            if event.key == K_a:
                Random = not Random      
            if event.key == K_c:
                color = 1   
            if event.key == K_z:
                color = 2  
            if event.key == K_x:
                pos = pygame.mouse.get_pos()
                Location = ((pos[0] // scaler), (pos[1] // scaler)) 
                Grid.Hsfn(Location)    
                
        if event.type == MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                state = 1
                pos = pygame.mouse.get_pos()
                Location = ((pos[0] // scaler), (pos[1 ] // scaler))
            elif pygame.mouse.get_pressed()[2]:
                state = 2
                pos = pygame.mouse.get_pos()
                Location = ((pos[0] // scaler) , (pos[1 ] // scaler))
        
                      
               

                
            
       



            
     
    Grid.Conway(color = color, off_color=white, res_color=green, death_color=red, Random_color= Random_colors, surface=screen, pause=pause, Loc = Location, Action = state, Random = Random)
    pygame.display.update()
pygame.quit()

