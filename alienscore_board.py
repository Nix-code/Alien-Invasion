import pygame.font
from pygame.sprite import Group
from rocket import Rocket
"""create score board class and initialize the attributes"""
class Scoreboard():
    #holds score information
    def __init__(self,game_set,screen,stat):
        """initialize the attributes"""
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.game_set=game_set
        self.stat=stat
        #font setting
        self.text_color=192,192,192
        self.font=pygame.font.SysFont(None,35)
        #prepare for initial score image
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_rockets()
    def prep_high_score(self):
        """turn high score into rendered image"""
        high_score=int(round(self.stat.high_score,-1))
        high_score_str="{:,}".format(high_score)
        self.high_score_image=self.font.render(high_score_str,True,self.text_color,
                                               self.game_set.bg_color)
        #center high score at the top of the screen
        self.high_score_rect=self.high_score_image.get_rect()
        self.high_score_rect.centerx=self.screen_rect.centerx
        self.high_score_rect.top=self.score_rect.top
        
    def prep_level(self):
        """set the level"""
        self.level_image=self.font.render(str(self.stat.level_up),True,self.text_color,self.game_set.bg_color)
        self.level_rect=self.level_image.get_rect()
        self.level_rect.right=self.score_rect.right
        self.level_rect.top=self.score_rect.bottom +10
    def prep_score(self):
        score_str=str(self.stat.score)
        self.score_image=self.font.render(score_str,True,self.text_color,
                                          self.game_set.bg_color)
        #display the score at the top left of the screen
        rounded_score=int(round(self.stat.score,-1))
        score_str="{:,}".format(rounded_score)
        self.score_rect=self.score_image.get_rect()
        self.score_rect.right=self.screen_rect.right-30
        self.score_rect.top=20
        #this three lines defines alot by placing the score top right
    
    def show_score(self):
        """to get displayed something on the screen
            use screen.blit method"""
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        #show the level which is being played
        self.screen.blit(self.level_image,self.level_rect)
        #draw rockets
        self.rockets.draw(self.screen)
    def prep_rockets(self):
        #show how many rockets are left
        self.rockets=Group()
        for rock_num in range(self.stat.rocket_left):
            rocket=Rocket(self.game_set,self.screen)
            rocket.rect.x=8+rock_num*rocket.rect.width
            rocket.rect.y=10
            self.rockets.add(rocket)
            
            
    
    
