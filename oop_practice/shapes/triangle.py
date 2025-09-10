from .base import Shape2D

class Triangle(Shape2D):
    def __init__(self, base: float, height: float) -> None:
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def corner_count(self):
        return 3

    
