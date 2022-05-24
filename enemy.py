import pygame
from pygame.sprite import Sprite

class Enemy(Sprite):
    def __init__(self,posx,posy,JA):
        Sprite.__init__(self)
        #game window and settings
        self.settings = JA.settings


        # player image and rect
        self.image = pygame.Surface((32,32))
        self.rect = self.image.get_rect()

        self.vel = 1



    def update(self,scroll):
        #moves the enemy object horizontally and changes direction once the enemy collides with the edge
        self.rect.x += self.vel
        if self.rect.right >= self.settings.screen_width or self.rect.left <= 0:
            self.vel *= -1
        # adjust the enemy with scroll
        self.rect.y -= scroll
