import pygame , sys , random
from settings import Settings
from player import Player
from platform import Platform



class Jumper:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        #main surface
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        #clock to manage frames of the game
        self.clock = pygame.time.Clock()

        self.player = Player(self)

        self.platform_group = pygame.sprite.Group()

    # def generate_platform(self):
    #     for i in range(1,25):
    #         plat = Platform(self)
    #         plat.rect.centerx = random.randint(self.settings.platform_width/2 , self.settings.screen_width
    #                                            - self.settings.platform_width)
    #         plat.rect.centery = random.randint(0 + self.settings.platform_height , self.settings.screen_height
    #                                            - self.settings.platform_height)
    #         self.platform_group.add(plat)

    def check_player_plat_collision(self):
        for plat in self.platform_group:
            if pygame.sprite.collide_rect(self.player, plat):
                if self.player.rect.bottom - plat.rect.top < 2 :
                    self.player.rect.bottom = plat.rect.top
                    self.settings.grav_flag = False


    def check_keydown(self,event):
        "checks for key events regarding the player movement"
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = True

        if event.key == pygame.K_LEFT:
            self.player.moving_left = True
        if event.key == pygame.K_SPACE:
            self.player.jumping = True

    def check_keyup(self,event):
        "checks for key events regarding the player movement"
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = False
        if event.key == pygame.K_LEFT:
            self.player.moving_left = False


    def update_mainsurface(self):
        " Method to encapsulate all the drawing on the main surface"
        # produce main surface
        self.screen.fill(self.settings.bg_colour)
        pygame.display.set_caption(self.settings.game_caption)

        # draw player
        self.player.draw_player()
        # draw the platforms
        self.platform_group.draw(self.screen)

        pygame.display.flip()


    def run_game(self):
        " manages the main loop that keeps the game running"
        #self.generate_platform()
        plat = Platform(self)
        self.platform_group.add(plat)
        while True:
            # keep game at 60 fps
            self.clock.tick(60)

            self.update_mainsurface()

            #functions for player
            self.player.move()
            self.player.jump()
            self.player.apply_gravity()

            #checking collision
            self.check_player_plat_collision()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    self.check_keydown(event)
                if event.type == pygame.KEYUP:
                    self.check_keyup(event)





if __name__ == "__main__":
    JA = Jumper()
    JA.run_game()