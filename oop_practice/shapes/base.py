from abc import ABC, abstractmethod

class Shape2D(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def corner_count(self) -> int:
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}"

    def __str__(self):
        return f"This shape has {self.corner_count()} corners and area of {self.area():.2f}"