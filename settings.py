#creating seperate class for height,width , color for screen

class Settings():
    def __init__(self):
        """initialize the game setting"""
        self.screen_width=600
        self.screen_height=1000
        self.bg_color=(0,0,0)
        self.rocket_speed_factor=15
        #bullet setting
        self.bullet_speed_factor=4
        self.bullet_height=6
        self.bullet_width=4
        self.bullet_color=192,192,192
        self.bullet_allowed=14
        #alien speed setting
        self.alien_speed_factor=4
        #setting speed factor to let flet of alien slide down
        self.fleet_down_speed=10
        """fleet 1 says to move Right and-1 left"""
        #alien new settinf for speed up
        self.speed_up=1.2
        self.score_scale=1.5
        self.newer_setting()
        
        self.fleet_direction=1
        #assign the rocket limit
        self.rocket_limit=3

    def newer_setting(self):
        self.rocket_speed_factor=14
        self.bullet_speed_factor=14
        self.alien_speed_factor=2
        self.fleet_direction=1
        #scoring
        self.score_point=1
        """we add flet direction so that alien always moves right(1)"""
    #increse the speed
    def increase_speed(self):
        #increase speed setting and scoring on level difficulties
        self.rocket_speed_factor*=self.speed_up
        self.bullet_speed_factor*=self.speed_up
        self.alien_speed_factor*=self.speed_up
        self.alien_points=int(self.score_point*self.score_scale)
        print(self.alien_points)
        
        

        
   
        
