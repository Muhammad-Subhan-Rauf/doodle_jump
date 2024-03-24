import pygame
from src.config import *
import random

class Platform:
    def __init__(self,x=0,y=200):
        '''
        Constructor for the Platforms class.
        '''
        # Load the platform image.
        
        self.y = y
        self.x = x
        self.width = 50
        self.height = 10
        self.jump_factor = 0

    
    
    def update(self,dt):
        pass
        
        
    def render(self,virtual_screen):
        virtual_screen.blit(self.image,(self.x,self.y))
        
    def move_down(self,velocity,dt):
        self.y = self.y - velocity
        
        
class Plain_Platform(Platform):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.jump_factor = 11
        self.image = pygame.image.load('assets/images/plain_platform.png')
        self.image = pygame.transform.scale(self.image,(self.width,self.height))
        
class Jumpy_Platform(Platform):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.jump_factor=40
        self.image = pygame.image.load('assets/images/jumpy_platform.png')
        self.image = pygame.transform.scale(self.image,(self.width,self.height))
        
class Decoy_Platform(Platform):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.jump_factor=0
        self.image = pygame.image.load('assets/images/decoy_platform.png')
        self.image = pygame.transform.scale(self.image,(self.width,self.height))

class Moving_Platform(Platform):
    def __init__(self,x,y):
        super().__init__(x,y)
        
        self.dx = 20
        self.direction =random.choice(["right","left"]) 
        self.jump_factor = 11
        self.image = pygame.image.load('assets/images/moving_platform.png')
        self.image = pygame.transform.scale(self.image,(self.width,self.height))
    
    def update(self,dt):
        if (self.x + self.width) >= VIRTUAL_WIDTH or self.x <= 0:
            if self.direction == "right":
                self.direction = "left"
            else:
                self.direction = "right"
        
        if self.direction == "right":
            self.x += self.dx*dt
        else:
            self.x -= self.dx*dt
                
            

        

    

