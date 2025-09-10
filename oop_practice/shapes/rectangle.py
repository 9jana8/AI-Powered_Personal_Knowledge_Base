from .base import Shape2D

class Rectangle(Shape2D):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def corner_count(self):
        return 4