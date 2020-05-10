class Game_stat():
    """we record the statistics for the collision """
    def __init__(self,game_set):
        """initialize the setting """
        self.game_set=game_set
        self.game_active=False
        self.reset_stat()
        #high score should not get reset
        self.high_score=0
       
        
        
    def reset_stat(self):
        """we should have the statistics to determine how many ship is left which
         continuously changes throughout the game"""
        self.rocket_left=self.game_set.rocket_limit
        self.score=0
        self.level_up=0
        
        
    
  
    
        
        
