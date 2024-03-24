'''
    Python port of the Harward's GD50 course
    https://cs50.harvard.edu/games/2018/

    Ported by:  Fakhir Shaheen
    Website:    https://fakhirshaheen.com/
    github:     https://github.com/fakhirsh
    linkedin:   https://www.linkedin.com/in/fakhirshaheen/
'''
from src.states.State import State

import pygame

from src.config import *
from src.char import *
from src.Platforms import *
from src.enemy import *

import random
from lib.utils import *
import time


class PlayState(State):
    """
    The State class serves as an abstract base class for game states or application states.
    It defines a common interface for all states, including lifecycle methods for loading,
    initializing, pausing, resuming, updating, and rendering. Subclasses must implement
    these methods according to their specific needs.
    
    Attributes:
        isPaused (bool): Indicates whether the state is currently paused.
    """
    
        
        
#--------------------------------------------------------------------------------------------------
    
    
    def __init__(self,char_image = pygame.image.load('assets/images/main_char.png')):
        self.char = character(char_image)
#--------------------------------------------------------------------------------------------------

    def load(self):
        """
        Placeholder for a method to load resources or data necessary for the state.
        This method should be overridden in subclasses to perform state-specific loading operations.
        
        Raises:
            NotImplementedError: If the subclass does not implement this method.
        """
        self.isPaused = False
        
        self.background = pygame.image.load('assets/images/background.jpeg')
        self.background = pygame.transform.scale(self.background,(VIRTUAL_WIDTH,VIRTUAL_HEIGHT))
        self.jump = pygame.mixer.Sound('assets/sounds/jump.wav')
        self.jump_high = pygame.mixer.Sound('assets/sounds/jump_high.wav')
        self.loose = pygame.mixer.Sound('assets/sounds/loose.wav')
        
        
        self.platforms = [Plain_Platform(100,400)]
        self.enemies = []
        
        
        self.atlas = pygame.image.load("assets/images/spritesheet.png")
        self.character_images = get_character_images()
        
        self.small_font = pygame.font.Font('assets/fonts/font.ttf', 8)
        self.MedFont = pygame.font.Font('assets/fonts/Indoor_School.otf', 32)
        
#--------------------------------------------------------------------------------------------------
        
    def generate_platforms(self):
        if self.platforms:
            plat = self.platforms[-1]
            while plat.y>15:
                
                x = plat.y - PLATFORM_Y_GAP
                variable = x-PLATFORM_Y_GAP-30
                new_plat_y = random.randint(min(int(x),int(variable)),max(int(x),int(variable)))
                new_plat_x = random.randint(15,VIRTUAL_WIDTH-plat.width-15)
                if variable > 0:
                    var = random.randint(1,30)
                    var_2 = random.randint(1,50)
                    
                    if var_2 <= 2:
                        if self.char.score>=500:
                           
                            new_enemy = Enemy(new_plat_x,new_plat_y)
                            self.enemies.append(new_enemy)        
                    if var > 5:
                        if var > 8:
                            new_platform = Plain_Platform(new_plat_x,new_plat_y)
                        else:
                            new_platform = Moving_Platform(new_plat_x, new_plat_y)
                    else:
                        if var==3:
                            new_platform = Jumpy_Platform(new_plat_x,new_plat_y)
                        else:
                            new_platform = Decoy_Platform(new_plat_x,new_plat_y)
                            
                    self.platforms.append(new_platform)
                    plat=new_platform
                else:
                    break
#--------------------------------------------------------------------------------------------------
    
    def remove_platforms(self):
        for i in self.platforms:
            if i.y >VIRTUAL_HEIGHT:
                
                self.platforms.remove(i)      
        
        for i in self.enemies:
            if i.y >VIRTUAL_HEIGHT:
                self.enemies.remove(i)
                
    
    
    
#--------------------------------------------------------------------------------------------------
    
    def unload(self):
        """
        Placeholder for a method to unload resources or data when the state is no longer needed.
        This method should be overridden in subclasses to perform state-specific unloading operations.
        
        Raises:
            NotImplementedError: If the subclass does not implement this method.
        """
        pass

#--------------------------------------------------------------------------------------------------
    
    def init(self):
        """
        Placeholder for a method to initialize the state. This method is intended to set up
        any necessary state-specific data structures or variables after loading resources.
        
        Raises:
            NotImplementedError: If the subclass does not implement this method.
        """
        
        self.char.jump(20)
    
#--------------------------------------------------------------------------------------------------
    
    def free(self):
        """
        Placeholder for a method to free up resources and perform clean-up activities for the state.
        This method is called when the state is definitively done and can be used to ensure a clean exit.
        
        Raises:
            NotImplementedError: If the subclass does not implement this method.
        """
        pass
    
#--------------------------------------------------------------------------------------------------
    
    def pause(self):
        """
        Placeholder for a method to pause the state, such as when the application loses focus or
        when transitioning to another state that does not unload the current state.
        
        Raises:
            NotImplementedError: If the subclass does not implement this method.
        """
        self.isPaused = True
        
    
#--------------------------------------------------------------------------------------------------
    
    def resume(self):
        """
        Placeholder for a method to resume the state from a paused state, restoring
        activity and possibly re-initializing resources that were freed on pause.
        
        Raises:
            NotImplementedError: If the subclass does not implement this method.
        """
        self.isPaused = False
        
    
#--------------------------------------------------------------------------------------------------
    def write_score(self, file_name, score):
        with open(file_name,"w+") as f:
            f.write(str(score))
            
        
    
    def update_scores(self,file_name,lst):
        
        with open(file_name,"w+") as file:
            for i in lst:
                if lst.index(i) == len(lst)-1:
                    file.write(f"{i[0]}:{i[1]}")
                else:
                    file.write(f"{i[0]}:{i[1]}\n")
                    
    def update_player_score(self,player_scores, new_player, new_score):
        
        player_scores.append([new_player, new_score])
        player_scores.sort(key=lambda x: x[1], reverse=True)
        return player_scores        
    
    def update(self, dt):
        """
        Placeholder for the update method, which is called regularly to update the state of the game
        or application. This method should contain the logic for updating the state's data.
        
        Args:
            dt (float): The delta time, or time elapsed since the last update call, in seconds.
        
        Raises:
            NotImplementedError: If the subclass does not implement this method.
        """
        if not self.is_paused():
            if self.char.loose == True:
                self.loose.play()
                time.sleep(3)
                self.write_score("Last_game_score.txt",self.char.score)
                high_scores = read_scores("high_scores.txt")
                lst = self.update_player_score(high_scores,"player",self.char.score)
                self.update_scores("high_scores.txt",lst)
                self.stateManager.changeState(self.stateManager.available_states["over"](self.char.image))
                
                
                
            
            self.char.update(dt)
            for i in self.platforms:
                i.update(dt)
            sound_check = self.char.check_collision(self.platforms,self.enemies)
            if sound_check!= False and sound_check>=40:
                self.jump.play()
                self.jump_high.play()
            elif sound_check != False and sound_check<40:
                self.jump.play()
            if self.char.hit_max_height():
                for i in self.platforms:
                    i.move_down(self.char.dy,dt)
                for i in self.enemies:
                    i.move_down(self.char.dy,dt)
            self.generate_platforms()
            self.remove_platforms()
        
        
        
    
#--------------------------------------------------------------------------------------------------
    
    def render(self, virtual_screen, dt=0.0):
        """
        Placeholder for the render method, which is called regularly to draw the state's visual elements.
        This method should contain all the drawing logic.
        
        Args:
            dt (float): Optional. The delta time, or time elapsed since the last render call, in seconds.
                        Defaults to 0.0 if not provided.
        
        Raises:
            NotImplementedError: If the subclass does not implement this method.
        """
        virtual_screen.fill((0, 0, 0))
        virtual_screen.blit(self.background,(0,0))
        
        
        
        
        draw_text(str(self.char.score), self.small_font, 10,20,(255,255,0),virtual_screen )
        
        #pygame.draw.rect(virtual_screen, (255,0,255), (0, 200, 100, 20))
        for platform in self.platforms:
            platform.render(virtual_screen)
        for enemy in  self.enemies:
            enemy.render(virtual_screen)
        self.char.render(virtual_screen)
        
        if self.is_paused():
            draw_text('Press P to unpause', self.MedFont, VIRTUAL_WIDTH / 2, VIRTUAL_HEIGHT/2, (255, 0, 255), virtual_screen)
            draw_text('and', self.MedFont, VIRTUAL_WIDTH / 2, (VIRTUAL_HEIGHT/2)+20, (255, 0, 255), virtual_screen)
            draw_text('Press Space to Pause', self.MedFont, VIRTUAL_WIDTH / 2, (VIRTUAL_HEIGHT/2)+40, (255, 0, 255), virtual_screen)
            
#--------------------------------------------------------------------------------------------------
    def handle_event(self, event):
        """
        Placeholder for the method to handle events, such as user input or system events.
        This method should contain the logic for handling events.

        Args:
            event (pygame.event.Event): The event to handle.

        Raises:
            NotImplementedError: If the subclass does not implement this method.
        """
        
        # if event.type == pygame.KEYDOWN:
        #     self.Flag = True
        # elif event.type == pygame.KEYUP:
        #     self.Flag = False
        
        # if self.Flag:
        #     print("Flag is true")
        #     if event.key == pygame.K_LEFT:
        #         self.char.move_left()
        #     elif event.key == pygame.K_RIGHT:
        #         self.char.move_right()
                
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.char.move_left()
        if keys[pygame.K_RIGHT]:
            self.char.move_right()
        if keys[pygame.K_UP]:
            self.char.jump(5)
            
        if keys[pygame.K_SPACE]:
            self.pause()
        if keys[pygame.K_p]:
            self.resume()
        
        
        

#--------------------------------------------------------------------------------------------------
    
    def is_paused(self):
        """
        Checks if the state is currently paused.
        
        Returns:
            bool: True if the state is paused, False otherwise.
        """
        return self.isPaused

#--------------------------------------------------------------------------------------------------