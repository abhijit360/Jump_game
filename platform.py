import pygame
from pygame.sprite import Sprite

class Platform(Sprite):
    def __init__(self, JA):
        super().__init__()
        self.settings = JA.settings
        self.screen = JA.screen
        self.player = JA.player

        #platform
        self.image = pygame.Surface((self.settings.platform_width,self.settings.platform_height))
        self.rect = self.image.get_rect()
        self.rect.center = (150,self.settings.screen_height - 60)

