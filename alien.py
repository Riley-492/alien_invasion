import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """shows a single alien"""

    def __init__(self, ai_game):
        """start the alien up"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load('images/aliens.bmp')
        self.rect = self.image.get_rect()
        #self.rect.topleft = self.rect.topleft

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or screen_rect.left <= 0:
            return True

    def update(self):
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x



