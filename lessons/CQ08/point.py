"""CQ08 - Intro to Object Oriented Programming."""
from __future__ import annotations
__author__ = "730679888"


class Point:
    """Class Point has x,y attribute."""
    x: float
    y: float


    def __init__(self, x_init: float, y_init: float) -> None:
        """Point Class."""
        self.x = x_init
        self.y = y_init


    def scale_by(self, factor: int) -> None:
        """Mutating method."""
        self.x *= factor
        self.y *= factor
        
        
    def scale(self, factor: int) -> Point:
        """Non-mutating method that returns a new Point object."""
        return Point(self.x * factor, self.y * factor)