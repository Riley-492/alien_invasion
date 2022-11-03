class GameStats:
    # track statistics for alien invasion

    def __init__(self, ai_game):
        #initialize statistics
        self.settings = ai_game.settings
        self.reset_stats()

        # Start game in an inactive state
        self.game_active = False

        self.high_score = 0


    def reset_stats(self):
        # Initialize statistics that can change during the game
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1