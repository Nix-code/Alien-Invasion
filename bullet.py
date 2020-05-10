import pygame
#sprite allows the elements to group and work at once
from pygame.sprite import Sprite
class Bullet(Sprite):
    def __init__(self,game_set,screen,rocket):
        super(Bullet,self).__init__()
        self.screen=screen
        #create bullet rect into correct position
        self.rect=pygame.Rect(0,0,game_set.bullet_width,game_set.bullet_height)
        #bullet rect is same as rocket because it should look like bullet comes from rocket
        self.rect.centerx=rocket.rect.centerx
        self.rect.top=rocket.rect.top
        #store bullet position as decimal
        self.y=float(self.rect.y)
        self.color=game_set.bullet_color
        self.speed_factor=game_set.bullet_speed_factor

#update the value of bullet
    def update(self):
        """make bullet move up to the screen"""
        #as bullet moves up , y-coordinates get decreased
        #x-coordinate never changes because it is fixed
        self.y-=self.speed_factor
        self.rect.y=self.y
    def draw_bullet(self):
        """draw the bullet to the screen"""
        pygame.draw.rect(self.screen,self.color,self.rect)
        
        
        
