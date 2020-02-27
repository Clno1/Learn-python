
class GameStats():

    def __init__(self,ai_settings):
        self.ai_settings=ai_settings
        self.reset_stats()

        self.game_active=False

    def reset_stats(self):
        self.ship_lives=self.ai_settings.ship_lives