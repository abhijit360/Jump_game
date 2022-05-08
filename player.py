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
        self.moving_right, self.moving_left, self.jumping, self.gravity_flag = False, False, False, True
        self.current_jump_vel = self.settings.player_jumpVel

        self.current_time = 0
    def draw_player(self):
        # creating the player surface
        self.screen.fill((255, 0, 0), self.rect)

    def move(self):
        if self.moving_right and self.rect.topright[0] < self.settings.screen_width:
            self.rect.centerx += self.settings.player_speed
        if self.moving_left and self.rect.topleft[0] > 0:
            self.rect.centerx -= self.settings.player_speed


    def apply_gravity(self):
        "To add an effect of gravity that can be toggled on and off using a gravity flag"
        if self.gravity_flag:
            self.rect.y += self.settings.gravity_val

    def jump(self):
        """ Jump mechanism of player"""
        if self.jumping and self.current_jump_vel >= -self.settings.player_jumpVel:
            self.rect.centery -= self.current_jump_vel * (pygame.time.get_ticks() - self.current_time)
            self.current_jump_vel += self.settings.gravity_val * (pygame.time.get_ticks() - self.current_time)
            print(self.rect.centery)
        else:
            # set jump flag back to false
            self.jumping = False
            self.current_jump_vel = self.settings.player_jumpVel



        # if self.jumping and self.rect.bottom < self.current_height - self.settings.jump_height:
        #     # stop moving once peak height is reached and resume gravity
        #     self.jumping, self.gravity_flag = False, True


        # if not self.jumping and self.rect.bottom <= self.current_height:
        #     self.rect.y += self.settings.gravity_val
