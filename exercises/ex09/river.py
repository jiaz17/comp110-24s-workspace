"""File to define River class."""
__author__ = "730679888"

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """River Class establish."""
    day: int
    fish: list[Fish]
    bears: list[Bear]
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def eat(self, num_fish: int):
        """Increase the bear's hunger_score by fish eaten."""
        self.hunger_score += num_fish

    def check_ages(self):
        """Removes fish older than 3 and bears older than 5."""
        self.fish = [fish for fish in self.fish if fish.age <= 3]
        self.bears = [bear for bear in self.bears if bear.age <= 5]
        return None

    def bears_eating(self):
        """Each bear will eat 3 fish if available."""
        for bear in self.bears:
            if len(self.fish) < 5:
                break  
            self.remove_fish(3)
            bear.eat(3)
        return None
    
    def check_hunger(self):
        """Removes any bears with hunger_score less than 0."""
        self.bears = [bear for bear in self.bears if bear.hunger_score >= 0]
        return None

    def repopulate_fish(self):
        """Each pair of fish will produce 4 offspring."""
        num_new_fish = (len(self.fish) // 2) * 4
        for _ in range(num_new_fish):
            self.fish.append(Fish())
        return None
    
    def repopulate_bears(self):
        """Each pair of bears will produce 1 offspring."""
        num_new_bears = len(self.bears) // 2
        for _ in range(num_new_bears):
            self.bears.append(Bear(age=0))
        return None
    
    def remove_fish(self, amount: int):
        """Remove the specified number of frontmost fish from the river."""
        self.fish = self.fish[amount:]

    def view_river(self):
        """View river output."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
    
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
    
    def one_river_week(self):
        """Simulate one week in the river."""
        for _ in range(7):
            self.one_river_day()