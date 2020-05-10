import sys
from time import sleep
import pygame
from bullet import Bullet
from enemy import Enemy

"""this function will allow rocket to move left and right
"""
def check_keydown_events(event,game_set,screen,rocket,bullets):
    if event.key == pygame.K_RIGHT:
        rocket.moving_right=True
    elif event.key == pygame.K_LEFT:
        rocket.moving_left=True#can click both left and right
    elif event.key == pygame.K_SPACE:
        fire_gun(game_set,screen,rocket,bullets)
    #elif event.key==K_q:
        #sys.exit()
        #it allows to exit the game by pressing key
#separating new function makes code easier to understand
def fire_gun(game_set,screen,rocket,bullets):
    if len(bullets)<game_set.bullet_allowed:
        #it allows only 3 bullets get active at a time
        new_bullet=Bullet(game_set,screen,rocket)
        bullets.add(new_bullet)
        #create a new bullet and add it 
"""key down allows to move left and right
but if user presses both key rocket should stop so R and L should be false"""
def check_keyup_events(event,rocket):
    if event.key==pygame.K_RIGHT:
        rocket.moving_right=False
    elif event.key==pygame.K_LEFT:
        rocket.moving_left=False
def check_events(game_set,screen,stat,sb,play_button,rocket,aliens,bullets):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event,game_set,screen,rocket,bullets)
        elif event.type==pygame.KEYUP:
            check_keyup_events(event,rocket)
        elif event.type==pygame.MOUSEBUTTONDOWN:
            """Mousebuttondown begins game whenever clicked to screen
                but we need restriction """
            #mouse responses x and y coordinate of play button
            mouse_x,mouse_y=pygame.mouse.get_pos()
            check_play_button(game_set,screen,stat,sb,play_button,rocket,aliens,bullets,mouse_x,mouse_y)

def check_play_button(game_set,screen,stat,sb,play_button,rocket,aliens,bullets,mouse_x,mouse_y):
    """start new game when player click play button"""
    button_clicked=play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stat.game_active:
        game_set.newer_setting()
        #hide mouse cursor
        pygame.mouse.set_visible(False)
        stat.reset_stat()
        stat.game_active=True
        #after each new click to play, old alien and bullets should be emptied
        #after the new game , each and everything must be emptied
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_rockets()
        aliens.empty()
        bullets.empty()
        #create new fleet of aliens
        alien_sum_flet(game_set,screen,rocket,aliens)
        rocket.rocket_center()
"""let's update screen, it redraw the screen again and again into new event"""
def update_screen(game_set,screen,stat,sb,rocket,aliens,bullets,play_button):
    #redraw screen into each for loop  a      
    #screen.fill(game_set.background)
    #redraw bullet behind rocket and alien
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    rocket.blitme()
    aliens.draw(screen)
    #draw play button if game is inactive
    sb.show_score()
    
    if not stat.game_active:
        play_button.draw_button()
    pygame.display.flip()

def update_my_bullets(game_set,screen,stat,sb,rocket,aliens,bullets):
    """updating the bullet and getting rid of old bullets"""
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)
    bullet_alien_collision(game_set,screen,stat,sb,rocket,aliens,bullets)
        
def bullet_alien_collision(game_set,screen,stat,sb,rocket,aliens,bullets):
    """check if any bullet hit enemy and make bullet and alien disappear"""
    collisions=pygame.sprite.groupcollide(bullets,aliens,True,True)
    if collisions:
        for aliens in collisions.values():
            stat.score+=game_set.score_point*len(aliens)
            sb.prep_score()
            check_high_score(stat,sb)
    if len(aliens)==0:
        #destroy exciting bullets and creat new one
        #if all the exsisting aliens are destroyed than start the new level
        stat.level_up+=1
        sb.prep_level()
        bullets.empty()
        game_set.increase_speed()
        alien_sum_flet(game_set,screen,rocket,aliens)
        

"""creating the flet of aliens on the top of the screen """
#lets refactor the code
def number_alien(game_set,alien_width):
    available_space=game_set.screen_width
    number_of_enemies=int(available_space//(5*alien_width))
    return number_of_enemies
    #simple mathematics where total screen space is divided by one alien width
#now know how much space is available in vertical row
def number_of_rows(game_set,rocket_height,alien_height):
    available_s_y=(game_set.screen_height-alien_height-2*rocket_height)
    number_row=int(available_s_y/(2*alien_height))
    return number_row
def create_enemy(game_set,screen,aliens,row_number,enemy_number):
    alien=Enemy(game_set,screen)
    alien_width=alien.rect.width
    alien.x=alien_width+2*alien_width*enemy_number
    alien.rect.x=alien.x
    alien.rect.y=alien.rect.height+2*alien.rect.height*row_number
    aliens.add(alien)
    #understand this line
    #we have added total number of alien to the group enemies
        
def alien_sum_flet(game_set,screen,rocket,aliens):
    """create flet of enemies"""
    alien=Enemy(game_set,screen)
    number_of_enemies=number_alien(game_set,alien.rect.width)
    number_row=number_of_rows(game_set,rocket.rect.height,alien.rect.height)
    for row_number in range(number_row):
        for enemy_number in range(number_of_enemies):
            create_enemy(game_set,screen,aliens,enemy_number,row_number)
def check_fleet_edges(game_set,aliens,rocket):
    """respond properly if alien reach to the edge of the screen"""
    for alien in aliens.sprites():
        if alien.check_edge():
            change_fleet_direction(game_set,aliens)
            break
def change_fleet_direction(game_set,aliens):
    """drop the entire alien down and change the direction of it"""
    for alien in aliens.sprites():
        alien.rect.y+=game_set.fleet_down_speed
    game_set.fleet_direction*=-1
def ship_hit(game_set,screen,stat,sb,rocket,aliens,bullets):
    #decrease the rocket by 1 after getting hit
    if stat.rocket_left>0:
        stat.rocket_left-=1
        """empty bullet and aliens list"""
        #update score board
        sb.prep_rockets()
        aliens.empty()
        bullets.empty()
        alien_sum_flet(game_set,screen,rocket,aliens)
        rocket.rocket_center()
        #pause
        sleep(0.5)
    else:
        stat.game_active=False
        pygame.mouse.set_visible(True)

def check_bottom_alien(game_set,screen,stat,sb,rocket,aliens,bullets):
    """respond same as the rocket gets hit by alien,after the flet reaches the bottom"""
    screen_rect=screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom>screen_rect.bottom:
            ship_hit(game_set,screen,stat,sb,rocket,aliens,bullets)
            break
    
def update_alien(game_set,screen,stat,sb,rocket,aliens,bullets):
    """update positions of all the aliens in a flet"""
    check_fleet_edges(game_set,aliens,rocket)
    aliens.update()
    #now create method that stops the loop after the collision of rocket with alien being collided
    if pygame.sprite.spritecollideany(rocket,aliens):
        ship_hit(game_set,screen,stat,sb,rocket,aliens,bullets)
        #look for the alien hitting the bottom
    check_bottom_alien(game_set,screen,stat,sb,rocket,aliens,bullets)

def check_high_score(stat,sb):
    if stat.score>stat.high_score:
        stat.high_score=stat.score
        sb.prep_high_score()
    
        
            


    
   
        
        
    
    
    
    
   
    
