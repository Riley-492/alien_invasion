class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings."""
        #Screen Settings
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230,230,230)

        #Ship settings
        self.ship_speed = 1.5

        #Bullet settings
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        #Alien speed
        self.alien_speed = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1


