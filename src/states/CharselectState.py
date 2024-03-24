
'''
    Python port of the Harward's GD50 course
    https://cs50.harvard.edu/games/2018/

    Ported by:  Fakhir Shaheen
    Website:    https://fakhirshaheen.com/
    github:     https://github.com/fakhirsh
    linkedin:   https://www.linkedin.com/in/fakhirshaheen/
'''
import pygame
from .State import State
from lib.utils import *
from src.config import *
import random

class Charselect(State):

        
    

            
    def load(self):
        # initialize our nice-looking retro text fonts having various sizes
        self.largeFont = pygame.font.Font('assets/fonts/font.ttf', 32)
        self.MedFont = pygame.font.Font('assets/fonts/Tenada.ttf', 25)
        self.background = random.choice([pygame.image.load("assets/images/background_main.jpeg"),pygame.image.load("assets/images/background_main2.jpeg")])
        self.background = pygame.transform.scale(self.background,(VIRTUAL_WIDTH,VIRTUAL_HEIGHT))
        
        self.selected = "menu"
        
        self.left_arrow = pygame.image.load('assets/images/arrow.png')
        self.left_arrow = pygame.transform.flip(self.left_arrow, True, False)
        self.left_arrow = pygame.transform.scale(self.left_arrow,(60,30))
        self.right_arrow =  pygame.image.load('assets/images/arrow.png')
        self.right_arrow = pygame.transform.scale(self.right_arrow,(60,30))
        
        self.char_width = 80
        self.char_height = 80
        self.characters = [
            pygame.image.load('assets/images/main_char.png'),
            pygame.image.load('assets/images/main_char1.png'),
            pygame.image.load('assets/images/main_char2.png'),
            pygame.image.load('assets/images/main_char3.png')
        ]
        self.selected_char = 0
#--------------------------------------------------------------------------------------------------
    
    def unload(self):
        pass

#--------------------------------------------------------------------------------------------------
    
    def init(self):
        # initialize the highlighted menu item
        self.highlighted = 1
        
    
#--------------------------------------------------------------------------------------------------
    
    def free(self):
        pass
    
#--------------------------------------------------------------------------------------------------
    
    def pause(self):
        pass
    
#--------------------------------------------------------------------------------------------------
    
    def resume(self):
        pass

#--------------------------------------------------------------------------------------------------
    
    def handle_event(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Handle the return key
                
                self.stateManager.changeState(self.stateManager.available_states["start"](self.characters[self.selected_char]))
                
            
            if event.key == pygame.K_LEFT :
                self.selected_char -= 1
                self.selected_char = self.selected_char%len(self.characters)
            elif event.key == pygame.K_RIGHT:
                self.selected_char += 1
                self.selected_char = self.selected_char%len(self.characters)
            

#--------------------------------------------------------------------------------------------------
    
    def update(self, dt):
        pass
    
#--------------------------------------------------------------------------------------------------
    
    def render(self, virtual_screen, dt=0.0):
        # clear screen to dark gray
        virtual_screen.fill((0, 0, 0))
        # Draw the title of the game
        virtual_screen.blit(self.background,(0,0))
        draw_text('Select Character', self.MedFont, VIRTUAL_WIDTH / 2, VIRTUAL_HEIGHT/3, (255, 255, 255), virtual_screen)
        self.characters[self.selected_char] = pygame.transform.scale(self.characters[self.selected_char],(self.char_width,self.char_height))
        virtual_screen.blit(self.characters[self.selected_char],((VIRTUAL_WIDTH / 2)-(self.char_width/2), (VIRTUAL_HEIGHT/2)-(self.char_height/2)))
        virtual_screen.blit(self.left_arrow,((VIRTUAL_WIDTH / 2)-(self.char_width/2)-80, (VIRTUAL_HEIGHT/2)-(self.char_height/2)+10))
        virtual_screen.blit(self.right_arrow,((VIRTUAL_WIDTH / 2)+(self.char_width/2)+20, (VIRTUAL_HEIGHT/2)-(self.char_height/2)+10))
        
    
#--------------------------------------------------------------------------------------------------