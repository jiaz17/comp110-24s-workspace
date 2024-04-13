class Point:
    def __init__(self, x_init: float, y_init: float):
        self.x = x_init
        self.y = y_init
        
        
    def scale_by(self, factor: int):
        """ Mutating method"""
        self.x *= factor
        self.y *= factor
        

    def scale(self, factor: int) -> 'Point':
        """Non-mutating method that returns a new Point object."""
        return Point(self.x * factor, self.y * factor)
