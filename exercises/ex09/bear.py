"""File to define Bear class."""


class Bear:
    """Bear Class."""
    def __init__(self, age=0):
        """Initialize Bear instance."""
        self.age = age
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """Simulate one day for the bear."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish):
        """Increases the bear's hunger_score."""
        self.hunger_score += num_fish
