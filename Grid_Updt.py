from numpy.core.numeric import array_equal
import pygame
import numpy as np
import random
n = 0
z  = 0
t = 0
class Grid:
    def __init__(self, width, height, scale, offset):
        # side of the square  
        self.scale = scale

        self.columns = int(height/scale)
        self.rows = int(width/scale)

        # tuple for Example : (5, 10)
        self.size = (self.rows, self.columns)   

        # cellular automata grid 
        self.grid_array = np.ndarray(shape=(self.size))
        self.colors = np.ndarray(shape=(self.size))
        self.offset = offset
        self.prev = np.ndarray(shape=(self.size))
        self.data = np.ndarray(shape=(self.size))
    # intialize the grid with a random values
    def random2d_array(self):
        global n
        i = 0
        if n != 0:
            n += 1
        for x in range(self.rows):
            for y in range(self.columns):
                self.colors[x][y] = i
                i +=1
                self.grid_array[x][y] = random.randint(0,1)
        for x in range (self.rows):
            for y in range(self.columns):
                state = self.grid_array[x][y]
                neighbours = self.get_neighbours(x, y)
                if state == 0 and neighbours == 3 :
                        self.data[x][y] =  np.random.choice([0,1], p=[0.7,0.3])    
                elif state == 1 and (neighbours < 2 or neighbours >3):
                        if neighbours > 3 : 
                            self.data[x][y] =  np.random.choice([0,1], p=[0.5,0.5])
                            
                        elif neighbours < 2 :
                           self.data[x][y] = np.random.choice([0,1], p=[0.8,0.2])  

    def Conway(self, color, off_color, res_color, death_color, Random_color, surface, pause, Loc, Action, Random): 
        global n,z,t,iter
        if color == 1:
            if Random == True:
                t +=1
            else:    
                n += 1
        elif color ==2:
            if Random == True:
                t -=1
            else:              
                n -= 1    
        self.prev = self.grid_array     
        for x in range(self.rows):
                    for y in range(self.columns):
                        y_pos = y * self.scale
                        x_pos = x * self.scale
                        cx = (self.scale / 2 ) + (x*self.scale)
                        cy = (self.scale / 2 ) + (y*self.scale)
                        St = Action
                        if self.grid_array[x][y] == 0:
                                pygame.draw.circle(surface, off_color, (cx,cy), (self.scale-self.offset)//2)
                          #  pygame.draw.rect(surface, off_color, [x_pos, y_pos, self.scale-self.offset, self.scale-self.offset])
                        if self.grid_array[x][y] == 1:
                                if Random == True:
                                    z =int(self.colors[x][y])  
                                    on_color =  Random_color[(z+t)%100]
                                    
                                else:    
                                    on_color =  Random_color[n%100]    
                                pygame.draw.circle(surface,on_color, (cx,cy), (self.scale-self.offset)//2)
                               # pygame.draw.rect(surface, Random_color[n%100] , [x_pos, y_pos, self.scale-self.offset, self.scale-self.offset])
                        if St == 1 and Loc == (x,y):
                            self.grid_array[x][y] = 1
                            pygame.draw.circle(surface, res_color, (cx,cy), (self.scale-self.offset)//2)
                            #pygame.draw.rect(surface, res_color, [x_pos, y_pos, self.scale-self.offset, self.scale-self.offset])
                        elif St == 2 and Loc == (x,y):
                            self.grid_array[x][y] = 0
                            pygame.draw.circle(surface, death_color, (cx,cy), (self.scale-self.offset)//2)
                           # pygame.draw.rect(surface, death_color, [x_pos, y_pos, self.scale-self.offset, self.scale-self.offset])        
                         
        next = np.ndarray(shape=(self.size))
        if pause == False :
            
            
            for x in range(self.rows):
                for y in range(self.columns): 
                    St = Action
                    state = self.grid_array[x][y]
                    neighbours = self.get_neighbours(x, y)
                    if state == 0 and neighbours == 3 and (St ==0 or St == 1):
                        next[x][y] =  np.random.choice([0,1], p=[0.7,0.3])    
                    elif state == 1 and (neighbours < 2 or neighbours >3) and (St == 0 or St == 1) :
                        if neighbours > 3 : 
                            next[x][y] =  np.random.choice([0,1], p=[0.5,0.5])
                        elif neighbours < 2 :
                           next[x][y] = np.random.choice([0,1], p=[0.8,0.2]) 
                    else:
                        next[x][y] = state 
                     
            self.grid_array = next

            if Random == False and not self.final_state():
                n +=1
                
                    

    def get_neighbours(self, x, y):
        total = 0
        for n in range(-1, 2):
            for m in range(-1, 2):
                x_edge = (x+n) % self.rows
                y_edge = (y+m) % self.columns
                total += self.grid_array[x_edge][y_edge]

        total -= self.grid_array[x][y]
        return total
    def final_state(self):
        return array_equal(self.grid_array,self.prev)
    
    def Hsfn(self,location):
        next = np.ndarray(shape=(self.size))
        for x in range(self.rows):
            for y in range(self.columns): 
                    state = next[x][y]
                    neighbours = self.get_neighbours(x, y)
                    if state == 0 and neighbours == 3 :
                        self.data[x][y] =  np.random.choice([0,1], p=[0.7,0.3])    
                    if state == 1 and (neighbours < 2 or neighbours >3):
                        if neighbours > 3 : 
                            self.data[x][y] =  np.random.choice([0,1], p=[0.5,0.5])
                        elif neighbours < 2 :
                           self.data[x][y] = np.random.choice([0,1], p=[0.8,0.2])  
                    else:
                        self.data[x][y] = state  
        for x in range(self.rows):
            for y in range(self.columns): 
                if location == (x,y):
                    data = self.data[x][y]
        if data == 1:
            print ("this cell may be alive next state")    
        elif data == 0:
            print ("This cell may be dead next state")     
                