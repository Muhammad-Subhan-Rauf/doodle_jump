
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

class OverState(State):
    def __init__(self,char_image = pygame.image.load('assets/images/main_char.png')):
        self.char_image = char_image
        
    def read_integer_from_file(self,file_path):
        try:
            with open(file_path, 'r') as file:
                line = file.readline().strip()
                return int(line)
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
        except ValueError:
            print(f"The content of the file '{file_path}' is not a valid integer.")

            
    def load(self):
        # initialize our nice-looking retro text fonts having various sizes
        self.largeFont = pygame.font.Font('assets/fonts/font.ttf', 32)
        self.MedFont = pygame.font.Font('assets/fonts/Tenada.ttf', 20)
        self.background = pygame.image.load("assets/images/background_main.png")
        self.background = pygame.transform.scale(self.background,(VIRTUAL_WIDTH,VIRTUAL_HEIGHT))
        
        self.selected = "menu"
        
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
                if self.selected == "menu":
                    self.stateManager.changeState(self.stateManager.available_states["start"](self.char_image))
                else:
                    self.stateManager.changeState(self.stateManager.available_states["play"](self.char_image))
            
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                if self.selected == "menu":
                    self.selected = "restart"
                else:
                    self.selected = "menu"

#--------------------------------------------------------------------------------------------------
    
    def update(self, dt):
        pass
    
#--------------------------------------------------------------------------------------------------
    
    def render(self, virtual_screen, dt=0.0):
        # clear screen to dark gray
        virtual_screen.fill((0, 0, 0))
        # Draw the title of the game
        virtual_screen.blit(self.background,(0,0))
        draw_text('Doodle Jump', self.largeFont, VIRTUAL_WIDTH / 2, VIRTUAL_HEIGHT/3, (255, 255, 255), virtual_screen)
        draw_text(f'You scored {self.read_integer_from_file("Last_game_score.txt")}', self.MedFont, VIRTUAL_WIDTH / 2, VIRTUAL_HEIGHT/2, (3, 252, 252), virtual_screen)
        if self.selected == "menu":
            draw_text('Main Menu', self.MedFont, VIRTUAL_WIDTH / 2, (VIRTUAL_HEIGHT/2)+20, (0, 255, 0), virtual_screen)
            draw_text('Restart Game', self.MedFont, VIRTUAL_WIDTH / 2, (VIRTUAL_HEIGHT/2)+40, (255, 0, 255), virtual_screen)
        else:
            draw_text('Main Menu', self.MedFont, VIRTUAL_WIDTH / 2, (VIRTUAL_HEIGHT/2)+20, (255, 0, 255), virtual_screen)
            draw_text('Restart Game', self.MedFont, VIRTUAL_WIDTH / 2, (VIRTUAL_HEIGHT/2)+40, (0, 255, 0), virtual_screen)
        
#--------------------------------------------------------------------------------------------------