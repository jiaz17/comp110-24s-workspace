"""File to define Bear class"""
__author__ = 730679888

class Bear:
    def __init__(self, age):

        """Initialize a new Bear instance."""
        self.age = age
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """Simulate one day for the bear."""
        self.age += 1
        return None
    def eat(self, num_fish):
        """Increases the bear's hunger_score."""
        self.hunger_score += num_fish
