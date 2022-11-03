import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0, 0, 15, 3)
        self.rect.midright = ai_game.ship.rect.midright

        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet"""
        self.x += self.settings.bullet_speed

        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet"""
        pygame.draw.rect(self.screen, self.color, self.rect)
