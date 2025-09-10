from .base import Shape2D
import math

class Circle(Shape2D):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def corner_count(self):
        return 0