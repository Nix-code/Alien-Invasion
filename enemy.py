#start a new class its same like rocket class
import pygame
from pygame.sprite import Sprite
class Enemy(Sprite):
    def __init__(self,game_set,screen):
        """initializing attributes """
        super(Enemy, self).__init__()
        self.game_set=game_set
        self.screen=screen
        self.image=pygame.image.load(r"C:\Users\Lenovo\Desktop\eni.png")
        self.rect=self.image.get_rect()

        """set the spaceship at top-left"""
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        self.x=float(self.rect.x)
    def blitme(self):
        """draw alien/enemy at the current location"""
        self.screen.blit(self.image,self.rect)
    
    def check_edge(self):
        """return true if alien is at edge"""
        screen_rect=self.screen.get_rect()
        if self.rect.right>=screen_rect.right:
            return True
        elif self.rect.left<=0:
            return True
    def update(self):
        self.x+=(self.game_set.alien_speed_factor*self.game_set.fleet_direction)
        self.rect.x=self.x

        
        
        
        
