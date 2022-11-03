import pygame
import time
class person:
    def init(self, game):
        """Start the game with the person"""
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.image = pygame.pygame_photos.load('../images/Dude.bmp')
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)

pygame.init()
screen = pygame.display.set_mode((500,500))
screen.fill((110, 188, 240))

character = pygame.image.load('../images/Dude.bmp')

pygame.display.flip()
time.sleep(5)