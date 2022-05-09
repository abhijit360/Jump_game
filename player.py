import pygame
from pygame.sprite import Sprite


class Player(Sprite):
    def __init__(self,JA):
        super().__init__()
        # IDK what to call these tf
        self.settings = JA.settings
        self.screen = JA.screen
        self.screen_rect = JA.screen_rect

        # player rect and positioning
        self.rect = pygame.rect.Rect((0, 0), (self.settings.player_width, self.settings.player_height))
        self.rect.bottom = self.screen_rect.bottom

        # player movement tags
        self.moving_right, self.moving_left, self.jumping = False, False, False
        self.current_jump_vel = self.settings.player_jumpVel

        self.vel_list = []
    def draw_player(self):
        # creating the player surface
        self.screen.fill((255, 0, 0), self.rect)

    def move(self):
        if self.moving_right and self.rect.topright[0] < self.settings.screen_width:
            self.rect.centerx += self.settings.player_speed
        if self.moving_left and self.rect.topleft[0] > 0:
            self.rect.centerx -= self.settings.player_speed

    def jump(self):
        """ Jump mechanism of player"""
        if self.jumping and round(self.current_jump_vel,1) >= -self.settings.player_jumpVel:
            self.settings.grav_flag = False
            self.rect.centery -= self.current_jump_vel
            self.current_jump_vel += self.settings.gravity_val
        if round(self.current_jump_vel,1) == -self.settings.player_jumpVel:
            # set jump flag back to false
            self.current_jump_vel = self.settings.player_jumpVel
            self.settings.grav_flag = True
            self.jumping = False


    def apply_gravity(self):
        if self.settings.grav_flag:
            self.rect.centery -= self.settings.falling_vel
            self.settings.falling_vel += self.settings.gravity_val
        else:
            self.settings.falling_vel = self.settings.gravity_val

