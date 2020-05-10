
"""Starting the Alien Invasion"""
import sys#to exit program
import pygame
from settings import Settings
from rocket import Rocket
from enemy import Enemy
from game_collides import Game_stat
from alienscore_board import Scoreboard
from button import Button
import game_function as gf
from pygame.sprite import Group

#starting game
def run_game():
    pygame.init()  #It sets screen display
    game_set=Settings()
    screen=pygame.display.set_mode((game_set.screen_height,game_set.screen_width))
    background=pygame.image.load(r'C:\Users\NISHANT\Desktop\UDACITY STUDENT MANAGEMENT\ALIEN INVASION (PYGAME-OCT - 16. (6-27)\nisss.jpg')
    pygame.display.set_caption("ALIEN INVASION :NISHANT")
    #rocket=Rocket(screen)
    """setting screen display and name of the game"""
    play_button=Button(game_set,screen,"Play")
    stat=Game_stat(game_set)
    sb=Scoreboard(game_set,screen,stat)
    rocket=Rocket(game_set,screen)
    bullets=Group()
    aliens=Group()
    gf.alien_sum_flet(game_set,screen,rocket,aliens)
    
    while True:
        bullets.update()
        #game controller
        gf.check_events(game_set,screen,stat,sb,play_button,rocket,aliens,bullets)
        
        if stat.game_active:
            rocket.update()
            gf.update_my_bullets(game_set,screen,stat,sb,rocket,aliens,bullets)
            gf.update_alien(game_set,screen,stat,sb,rocket,aliens,bullets)
            """for loop controls the event of mouse and keyboards"""
        gf.update_screen(game_set,screen,stat,sb,rocket,aliens,bullets,play_button)
        screen.blit(background,(0,0))
run_game()

                
