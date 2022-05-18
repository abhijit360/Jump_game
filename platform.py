import pygame
from pygame.sprite import Sprite

class Platform(Sprite):
    def __init__(self, JA,x,y,width):
        super().__init__()
        self.settings = JA.settings
        self.screen = JA.screen
        self.player = JA.player

        #platform
        self.image = pygame.Surface((width,self.settings.platform_height))
        self.rect = self.image.get_rect()
        self.rect.x,self.rect.y = (x,y)

    def update(self,scroll):
        self.rect.y -= scroll


