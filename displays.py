import pygame

class Score:
    def __init__(self,JA):
        # load in screen and settings
        self.screen = JA.screen
        self.settings = JA.settings

        # Font and styling
        self.font = pygame.font.SysFont("Ariel", 24)
        self.font_colour = (148, 0, 0)

        #score pos
        self.pos_X = 30
        self.pos_Y = 50

        self.distance_travelled = 0

        self.highscore = 0

    def measure_score(self,scroll):
        # measures the distance moved
        self.distance_travelled -= scroll

        # reads the highscore
        file_object = "score.txt"
        with open(file_object,"r") as fo:
            self.highscore = fo.read()

    def draw_current_score(self):
        # use the font to create text object and draw it on the screen
        cur_score = self.font.render(str(round(self.distance_travelled)),False,self.font_colour)
        self.screen.blit(cur_score,(self.pos_X,self.pos_Y))

    def display_highscore(self):
    # store previous high score in a file and use it to draw a check point that shows the previous highscore distance
        pygame.draw.line(self.screen,self.font_colour,start_pos=(0,int(self.highscore)),end_pos=(self.settings.screen_width,int(self.highscore)),width=1)




