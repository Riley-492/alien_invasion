import pygame
import sys


class Dude:

    def __init__(self, screen):
        """Start the game with the person"""
        self.dude_rect = screen.get_rect()
        self.screen = screen
        self.dude = pygame.image.load('../images/Dude.bmp')
        self.screen_rect = screen.get_rect()
        self.rect = self.dude.get_rect()
        self.screen_rect.center = self.dude_rect.center
        self.bullets = pygame.sprite.Group()
        self.y = float(self.rect.y)

        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update position based on movement"""
        # update ship value not the rectangle
        if self.moving_up and self.rect.top > 0:
            self.y -= 0.5
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += 0.5
        self.rect.y = self.y

    def draw(self):
        self.screen.blit(self.dude, self.rect)

class Bullet():

    """A class to manage bullets fired from the ship"""

    def __init__(self, ship):
        """Create a bullet object at the ship's current position"""
        super().__init__()
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        self.color = self.bullet_color

        self.rect = pygame.Rect(0, 0, self.bullet_width, self.bullet_height)
        self.rect.midright= ship.rect.midright

        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet"""
        self.x -= self.bullet_speed

        self.rect.y = self.x

    def draw_bullet(self):
        """Draw the bullet"""
        pygame.draw.rect(self.screen, self.color, self.rect)


pygame.init()
screen = pygame.display.set_mode((300, 300))
dude = Dude(screen)

# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                dude.moving_down = True
                print("Moving down")
            elif event.key == pygame.K_UP:
                dude.moving_up = True
                print("Moving up")
            elif event.key == pygame.K_SPACE:
                _fire_bullet()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                dude.moving_down = False
                dude.moving_up = False


    dude.update()

    screen.fill((110, 188, 240))
    dude.draw()
    pygame.display.flip()

