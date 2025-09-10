from abc import ABC, abstractmethod

class Shape2D(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def corner_count(self):
        pass
