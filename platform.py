import pygame
from pygame.sprite import Sprite

class Platform(Sprite):
    def __init__(self, JA,x,y,width):
        super().__init__()
        self.settings = JA.settings
        self.screen = JA.screen
        self.player = JA.player

        #platform rect, image, and position
        self.image = pygame.Surface((width,self.settings.platform_height))
        self.rect = self.image.get_rect()
        self.rect.x,self.rect.y = (x,y)

    def update(self,scroll):
        self.rect.y -= scroll

class Moving_plats(Sprite):
    def __init__(self, JA, x, y, width):
        super().__init__()
        self.settings = JA.settings
        self.screen = JA.screen
        self.player = JA.player

        # platform rect, image, and position
        self.image = pygame.Surface((width, self.settings.platform_height))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = (x, y)

        # movement of Moving_plats
        self.vel = self.settings.platform_vel

    def update(self, scroll):
        self.rect.x += self.vel
        if self.rect.right >= self.settings.screen_width or self.rect.left <= 0:
            self.vel *= -1
        self.rect.y -= scroll