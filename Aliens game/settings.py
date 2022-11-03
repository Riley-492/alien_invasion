class Settings:
    # A class to store all settings for Alien Invasion

    def __init__(self):
        # initialize the game's settings

        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (43, 255, 50)
        self.bullets_allowed = 3

        # Alien Settings
        self.alien_speed = 0.5
        self.fleet_drop_speed = 5
        # Fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        self.speedup_scale = 1.5
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 4
        self.bullet_speed = 3
        self.alien_speed = 1

        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
