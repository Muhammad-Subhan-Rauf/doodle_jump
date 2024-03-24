
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

class ScoreState(State):
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
        self.scoreFont = pygame.font.Font('assets/fonts/Tenada.ttf', 16)
        self.background = random.choice([pygame.image.load("assets/images/background_main.jpeg"),pygame.image.load("assets/images/background_main2.jpeg")])
        self.background = pygame.transform.scale(self.background,(VIRTUAL_WIDTH,VIRTUAL_HEIGHT))
        
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
                self.stateManager.changeState(self.stateManager.available_states["start"]())
                

#--------------------------------------------------------------------------------------------------
    
    def update(self, dt):
        pass
    
#--------------------------------------------------------------------------------------------------
    
    def render(self, virtual_screen, dt=0.0):
        # clear screen to dark gray
        virtual_screen.fill((0, 0, 0))
        # Draw the title of the game
        virtual_screen.blit(self.background,(0,0))
        
        lst = read_scores("high_scores.txt")
        draw_text('High Scores', self.largeFont, VIRTUAL_WIDTH / 2, VIRTUAL_HEIGHT/4, (255, 255, 255), virtual_screen)
        for i in range(min(10,len(lst))):
            draw_text(f'{i+1}. {lst[i][0]}\t{lst[i][1]}', self.scoreFont, VIRTUAL_WIDTH / 2, (VIRTUAL_HEIGHT/3)+(i*20), (3, 252, 252), virtual_screen)
        
#--------------------------------------------------------------------------------------------------