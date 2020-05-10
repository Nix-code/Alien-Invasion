#create button
import pygame.font
class Button():
    def __init__(self,game_set,screen,msg):
        """initialize the buttion settings"""
        self.screen=screen
        self.screen_rect=screen.get_rect()
        """set dimension of button"""
        self.width,self.height=200,50
        self.button_color=(6,53,146)
        self.text_color=(255,255,255)
        self.font=pygame.font.SysFont(None,48)
        #none means to use default font and size 48
        #build button rect object and place it on the center
        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.center=self.screen_rect.center
        #button rect gets placed at the screen rect
        #button message
        self.prep_msg(msg)

    def prep_msg(self,msg):
        """turn msg into a rendered image ans center text on button"""
        self.msg_image=self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.center=self.rect.center
    def draw_button(self):
        #draw blank button and write msg
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)
