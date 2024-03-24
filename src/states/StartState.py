
'''
    Python port of the Harward's GD50 course
    https://cs50.harvard.edu/games/2018/

    Ported by:  Fakhir Shaheen
    Website:    https://fakhirshaheen.com/
    github:     https://github.com/fakhirsh
    linkedin:   https://www.linkedin.com/in/fakhirshaheen/
'''
import pygame
from src.char import character
from .State import State
from lib.utils import *
from src.config import *
import random

class StartState(State):
    def __init__(self,char_image = pygame.image.load('assets/images/main_char.png')):
        self.char_image = char_image
        
    def load(self):
        # initialize our nice-looking retro text fonts having various sizes
        self.largeFont = pygame.font.Font('assets/fonts/font.ttf', 32)
        self.MedFont = pygame.font.Font('assets/fonts/Tenada.ttf', 20)
        
        self.background = pygame.image.load("assets/images/background_main.png")
        self.background = pygame.transform.scale(self.background,(VIRTUAL_WIDTH,VIRTUAL_HEIGHT))
        
        high_score = read_scores("high_scores.txt")
        self.high_score = high_score[0]
        
        self.selected = "start"
        
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
                if self.selected == "start":
                    self.stateManager.changeState(self.stateManager.available_states["play"](self.char_image))
                elif self.selected == "char":
                    self.stateManager.changeState(self.stateManager.available_states["char"]())
                else:
                    self.stateManager.changeState(self.stateManager.available_states["score"]())
                    
                
            if event.key == pygame.K_UP :
                if self.selected == "start":
                    self.selected = "scores"
                elif self.selected == "char":
                    self.selected = "start"
                else:
                    self.selected = "char"
            if event.key == pygame.K_DOWN:
                if self.selected == "start":
                    self.selected = "char"
                elif self.selected == "char":
                    self.selected = "scores"
                else:
                    self.selected = "start"
            

#--------------------------------------------------------------------------------------------------
    
    def update(self, dt):
        pass
    
#--------------------------------------------------------------------------------------------------
    
    def render(self, virtual_screen, dt=0.0):
        # clear screen to dark gray
        virtual_screen.fill((0, 0, 0))
        # Draw the title of the game
        virtual_screen.blit(self.background,(0,0))
        draw_text('Doodle Jump', self.largeFont, VIRTUAL_WIDTH / 2, VIRTUAL_HEIGHT/3, (12, 34, 237), virtual_screen)
        draw_text(f'High Score: {self.high_score[1]}', self.MedFont, VIRTUAL_WIDTH / 2, (VIRTUAL_HEIGHT/2)-40, (255, 0, 255), virtual_screen)
        draw_text('Press Enter to select', self.MedFont, VIRTUAL_WIDTH / 2, (VIRTUAL_HEIGHT/2)-20, (255, 0, 255), virtual_screen)
        
        if self.selected == "start":
            draw_text('Start Game', self.MedFont, VIRTUAL_WIDTH / 2, (VIRTUAL_HEIGHT/2)+20, (0, 255, 0), virtual_screen)
            draw_text('Character Select', self.MedFont, VIRTUAL_WIDTH / 2, (VIRTUAL_HEIGHT/2)+40, (237, 65, 12), virtual_screen)
            draw_text('High Scores', self.MedFont, VIRTUAL_WIDTH / 2, (VIRTUAL_HEIGHT/2)+60, (237, 65, 12), virtual_screen)
        
        elif self.selected == "char":
            draw_text('Start Game', self.MedFont, VIRTUAL_WIDTH / 2, (VIRTUAL_HEIGHT/2)+20, (237, 65, 12), virtual_screen)
            draw_text('Character Select', self.MedFont, VIRTUAL_WIDTH / 2, (VIRTUAL_HEIGHT/2)+40, (0, 255, 0), virtual_screen)
            draw_text('High Scores', self.MedFont, VIRTUAL_WIDTH / 2, (VIRTUAL_HEIGHT/2)+60, (237, 65, 12), virtual_screen)
        
        else:
            draw_text('Start Game', self.MedFont, VIRTUAL_WIDTH / 2, (VIRTUAL_HEIGHT/2)+20, (237, 65, 12), virtual_screen)
            draw_text('Character Select', self.MedFont, VIRTUAL_WIDTH / 2, (VIRTUAL_HEIGHT/2)+40, (237, 65, 12), virtual_screen)
            draw_text('High Scores', self.MedFont, VIRTUAL_WIDTH / 2, (VIRTUAL_HEIGHT/2)+60, (0, 255, 0), virtual_screen)
        
#--------------------------------------------------------------------------------------------------