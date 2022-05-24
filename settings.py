class Settings:
    def __init__(self):
        # game settings
        self.screen_width = 300
        self.screen_height = 600
        self.bg_colour = (214, 217, 132)
        self.game_caption = "Jumpin' Away"

        # player settings:
        self.player_width = 30
        self.player_height = 75
        self.player_speed = 3
        self.jump_height = 75
        self.player_jumpVel = 5

        #platform settings
        self.platform_width = 60
        self.platform_height = 10
        self.platform_vel = 1
        self.start_platx = 250
        self.start_platy = 350

        # gravity settings
        self.gravity_val = -0.1
        self.falling_vel = self.gravity_val
        self.grav_flag = True
