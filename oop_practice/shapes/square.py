from .rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, a: float) -> None:
        super().__init__(a, a)
        self.a = a