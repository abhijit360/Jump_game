class Settings:
    def __init__(self):
        # game settings
        self.screen_width = 300
        self.screen_height = 500
        self.bg_colour = (214, 217, 132)
        self.game_caption = "Jumpin' Away"

        # player settings:
        self.player_width = 30
        self.player_height = 75
        self.player_speed = 3
        self.jump_height = 75

        #platform settings
        self.platform_width = 60
        self.platform_height = 5

        # misc settings
        self.gravity_val = 1
