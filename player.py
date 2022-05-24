import pygame
from pygame.sprite import Sprite


class Player(Sprite):
    def __init__(self,JA,plat_group):
        super().__init__()
        # IDK what to call these tf
        self.settings = JA.settings
        self.screen = JA.screen
        self.screen_rect = JA.screen_rect

        # player rect and positioning
        self.rect = pygame.rect.Rect((0, 0), (self.settings.player_width, self.settings.player_height))
        #self.rect.bottom = self.screen_rect.bottom
        self.rect.center = (155,self.settings.screen_height-150)

        #group to detect collisions
        self.plat_group = plat_group


        # player movement tags
        self.moving_right, self.moving_left, self.jumping, self.falling = False, False, False,True
        self.current_jump_vel = self.settings.player_jumpVel
        self.scroll_threshold = 400
        self.scroll = 0

    def draw_player(self):
        # creating the player surface
        self.screen.fill((255, 0, 0), self.rect)

    def move(self):
        if self.moving_right and self.rect.topright[0] < self.settings.screen_width:
            self.rect.centerx += self.settings.player_speed
        if self.moving_left and self.rect.topleft[0] > 0:
            self.rect.centerx -= self.settings.player_speed
        if self.jumping and self.rect.bottom < self.scroll_threshold:
            self.scroll = - self.current_jump_vel * 1.25
        else:
            self.scroll = 0

    def jump(self):
        """ Jump mechanism of player: the player moves upwards until the upward velocity reaches zero. After reaching
        the peak of the jump, acceleration due to gravity takes over """
        if self.jumping and round(self.current_jump_vel,1) >= -self.settings.player_jumpVel:
            self.settings.grav_flag = False
            self.rect.centery -= self.current_jump_vel
            self.current_jump_vel += self.settings.gravity_val
        if round(self.current_jump_vel, 1) == 0:
            # stops the upward motion once the object reaches the peak of the jump
            self.end_jump()
            self.settings.grav_flag = True

    def end_jump(self):
        """Abruptly ends jump and resets ability to jump"""
        self.jumping = False
        self.current_jump_vel = self.settings.player_jumpVel

    def apply_gravity(self):
        if self.settings.grav_flag:
            self.falling = True
            self.rect.centery -= self.settings.falling_vel
            self.settings.falling_vel += self.settings.gravity_val
        else:
            self.settings.falling_vel = self.settings.gravity_val
            self.falling = False

    def check_player_plat_collision(self):
        """Checks if the bottom of the player rect collides with the top of the platform. If collison takes place, the
        player is not subjected to gravity. If the player, is no longer colliding with the rect, the player begins to
        fall"""
        plat = pygame.sprite.spritecollideany(self, self.plat_group)
        if plat:
            if self.jumping and round (self.rect.bottom - plat.rect.top) <= 3:
                # checks if the object jumps onto a platform or falls onto a platform
                self.rect.bottom = plat.rect.top
                self.end_jump()
                self.settings.grav_flag = False
            elif self.falling and round(self.rect.bottom - plat.rect.top) <= 3:
                # checks if the object jumps onto a platform or falls onto a platform
                self.rect.bottom = plat.rect.top
                self.end_jump()
                self.settings.grav_flag = False
            if self.jumping and round(self.rect.top - plat.rect.bottom) <= 3:
                # checks if the jumping object collides with the base of the platform
                self.rect.top = plat.rect.bottom
                self.end_jump()
                self.settings.grav_flag = True
            if self.moving_right and round(self.rect.right - plat.rect.left) <= 3:
                # checks if the object collides into the right hand side of the platform
                self.rect.right = plat.rect.left
                self.end_jump() #ending the jump prevents the jerky up adjustment
            if self.moving_left and round(self.rect.left - plat.rect.right) <= 3:
                #checks if the object collides into the left hand side of the platform
                self.rect.left = plat.rect.right
                self.end_jump() #ending the jump prevents the jerky up adjustment

