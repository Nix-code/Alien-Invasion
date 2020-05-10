import pygame
""" Create rocket class , load image of rocket,set it rect because it is easier
to use"""
from pygame.sprite import Sprite
class Rocket(Sprite):
    def __init__(self,game_set,screen):
        """ initialize the rocket and set it to the starting position"""
        super(Rocket,self).__init__()
        self.screen=screen
        #load the rocket image and get it rect
        self.game_set=game_set
        self.image=pygame.image.load(r'C:\Users\Lenovo\Desktop\rockt.png')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        #assigning rocket in bottom and in center
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        self.center=float(self.rect.centerx)
        """flag method is imp,
            if we press right arrow continuously it only stops if we release the key"""
        #movement flag
        self.moving_right=False
        self.moving_left=False
    def update(self):
        '''false means release of button say,
        so it acts as true, it goes on until it is realeased'''
        if self.moving_right and self.rect.right<self.screen_rect.right:#updating center value not rect
            self.center+=self.game_set.rocket_speed_factor
        if self.moving_left and self.rect.left>0:
            self.center-=self.game_set.rocket_speed_factor
            #update rect value from center
        self.rect.centerx=self.center
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    def rocket_center(self):
        #center the rocket to the screen
        self.center=self.screen_rect.centerx

