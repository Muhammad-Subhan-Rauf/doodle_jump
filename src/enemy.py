from src.config import *
from lib.utils import *
import pygame
import random



class Enemy:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.height = 40
        self.width  = 40
        self.image = random.choice([pygame.image.load("assets/images/enemy1.png"),pygame.image.load("assets/images/enemy2.png")])
        self.image = pygame.transform.scale(self.image, (self.width,self.height))
        
    def render(self, virtual_screen):
        virtual_screen.blit(self.image,(self.x,self.y-self.height))
    
    def move_down(self,velocity,dt):
        self.y = self.y - velocity
        
    def update(self):
        pass
    
                
