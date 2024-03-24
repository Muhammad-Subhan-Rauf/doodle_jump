import pygame
from src.config import *
from lib.utils import *


class character:
    def __init__(self, image = pygame.image.load('assets/images/main_char.png')):
        '''
        Constructor for the Character class.
        '''
        # Load the character image.
        self.image = image
      
        pygame.init()
        self.width = 50
        self.height = 50
        self.image = pygame.transform.scale(self.image,(self.width,self.height))
        self.jumpi = pygame.mixer.Sound('assets/sounds/jump.wav')

        self.y = VIRTUAL_HEIGHT-50
        self.x = VIRTUAL_WIDTH//2
        
        #self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
        self.rect = pygame.rect.Rect(self.x,self.y,self.width,self.height)
        
        
        
        self.direction = "Right"
        
        self.kill_mode = False
 
        self.dx = 0
        self.dy = 0

        self.loose = False
        self.score = 0
    
    def update(self,dt):
        if not self.loose:
            if self.dy > 0 :
                self.kill_mode = False
            if self.x>VIRTUAL_WIDTH:  #
                self.x=0-self.width   #
                                        #these lines are used to warp the character from either side of the 
                                        #display
            if self.x+self.width<0:   #
                self.x=VIRTUAL_WIDTH  #
            
            
            self.x += self.dx*dt
            
            
            if self.dx>0:
                self.dx = max(0,self.dx-PLAYER_FRICTION) #PLAYER_FRICTION is the factor of slowing the character while moving left and right
            else:                                        # this is done to give the illusion of fluid motion
                self.dx = min(0,self.dx+PLAYER_FRICTION)
            
            
            self.dy += GRAVITY * dt
            
            if self.y>VIRTUAL_HEIGHT//2:
                self.y = min(VIRTUAL_HEIGHT,self.y+self.dy)
            else:
                self.score+=1
                self.y= max(VIRTUAL_HEIGHT//2,self.y+self.dy) #This will only allow player to move to half
                                                            #of the screen height after which the platforms
                                                            # will move down
                                                            
            
            
            self.rect.x = self.x
            self.rect.y = self.y
            if self.y+self.height>VIRTUAL_HEIGHT:
                self.loose = True
        else:
            if self.y >VIRTUAL_HEIGHT:
                self.y = 0-self.height
            
            
        
    def render(self,virtual_screen):
        virtual_screen.blit(self.image,self.rect)
        #pygame.draw.rect(virtual_screen,(0,0,0),self.rect)
        #virtual_screen.blit(self.image,(self.x,self.y))

    def move_left(self):
        if self.direction == "Right":
            self.image = pygame.transform.flip(self.image, True, False)
            self.direction = "Left"
        
        self.dx = -PLAYER_SPEED
    
    
    
    def move_right(self):
        if self.direction == "Left":
            self.image = pygame.transform.flip(self.image, True, False)
            self.direction = "Right"
        
        self.dx = PLAYER_SPEED
    
    
    def jump(self, value):
        #print("Jumping",value,self.dy,self.y)
        if value>25:
            self.kill_mode = True
        self.dy = -value
        
        
    def hit_max_height(self):
        if self.y>VIRTUAL_HEIGHT//2:
            return False
        return True   
    
    def check_collision(self,platforms=[],enemies =[]):
        for i in platforms:
            if self.dy>0:
                
                if self.x+5 <= i.x+i.width:
                    
                    if self.x+self.width-5 >= i.x:
                        
                        if i.y <= self.y+self.height <= i.y+i.height:
                            if i.jump_factor!=0:
                                self.jump(i.jump_factor)
                                return i.jump_factor
                            else:
                                platforms.remove(i)
                                return False
        for i in enemies:
            if self.x +5 <= i.x+i.width:
                if self.x+self.width-5 >= i.x:
                    if i.y <= self.y+self.height-5 <= i.y+i.height:
                        if not self.kill_mode:
                            self.loose = True
                        else:
                            print("Killed enemy")
                            enemies.remove(i)
        return False
                                
        
        