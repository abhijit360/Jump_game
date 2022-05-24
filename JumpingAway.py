import pygame , sys , random
from settings import Settings
from player import Player
from platform import Platform
from enemy import Enemy
from displays import Score


class Jumper:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        #main surface
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        #clock to manage frames of the game
        self.clock = pygame.time.Clock()

        self.platform_group = pygame.sprite.Group()
        self.player = Player(self,self.platform_group)

        self.score = Score(self)
        self.enemy_group = pygame.sprite.Group()


    def spawn_enemy(self):
        """Spawns enemy and removes any platforms in its path"""
        if len(self.enemy_group) < 1:
            global path_block, path_surf
            enemy_x = random.randint(0, self.settings.screen_width)
            enemy_y = random.randint(0, self.settings.screen_height)
            path_block = pygame.Rect((enemy_x, enemy_y), (32,self.settings.screen_width))
            # create a rectangle that represents the path taken by the enemy.
            enemy = Enemy(enemy_x,enemy_y,self)
            self.enemy_group.add(enemy)

        for plat in self.platform_group.sprites():
            # checks if any platforms collide with the path of the enemy and removes them
            if path_block.colliderect(plat):
                self.platform_group.remove(plat)

    def generate_platform(self, offset_x=155,offset_y=500):
        """ produces a fixed number of platform sprites and adds it to the group"""
        for i in range(10):
            P_width = random.randint(30,60)
            P_x = random.randint(0,self.settings.screen_width - P_width)
            P_y = random.randint(100,150)
            if i == 0:
                plat = Platform(self,offset_x,offset_y,P_width)
                self.platform_group.add(plat)
            plat = Platform(self,P_x,(offset_y - (P_y *i)),P_width)
            self.platform_group.add(plat)

    def manage_sprites(self):
        """ manages the all sprite groups"""

        # Kills platforms that reach the bottom of the screen
        for plat in self.platform_group:
            if plat.rect.y > self.settings.screen_height:
                self.platform_group.remove(plat)

        # kills enemies that reach the bottom of the screen
        for enemy in self.enemy_group:
            if enemy.rect.y > self.settings.screen_height:
                self.enemy_group.remove(enemy)

        if len(self.platform_group) < 8:
            self.generate_platform(offset_y=-25)

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
        #draw enemy and moving sprites
        self.enemy_group.draw(self.screen)
        # draw score and displahy highscore
        self.score.draw_current_score()
        self.score.display_highscore()
        pygame.display.flip()

    def end_game(self):
        ''' checks if situations to end game are met'''
        if self.player.rect.y > self.settings.screen_height:
            self.save_score()
            pygame.quit()
            sys.exit()
        for enemy in self.enemy_group:
            if self.player.rect.colliderect(enemy.rect):
                self.save_score()
                pygame.quit()
                sys.exit()


    def save_score(self):
        file_object = "score.txt"
        with open(file_object,"w+") as fo:
            fo.write(str(round(self.score.distance_travelled)))

    def run_game(self):
        " manages the main loop that keeps the game running"

        # produces the platform
        self.generate_platform()

        while True:
            # keep game at 60 fps
            self.clock.tick(60)

            self.update_mainsurface()

            #functions for player
            self.player.move()
            self.player.jump()
            self.player.apply_gravity()

            #checking collision
            self.player.check_player_plat_collision()

            #update platforms
            self.platform_group.update(self.player.scroll)
            self.manage_sprites()

            # create enemy and update enemy group
            self.spawn_enemy( )
            self.enemy_group.update(self.player.scroll)

            # measure and displays current score
            self.score.measure_score(self.player.scroll)
            self.end_game()
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