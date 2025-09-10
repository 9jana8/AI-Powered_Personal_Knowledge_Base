from .base import Shape2D
import math
from functools import lru_cache
from .logging_decorator import log_calls

class Circle(Shape2D):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return self._area_cached(self.radius)

    def corner_count(self) -> int:
        return 0
    
    @staticmethod
    @lru_cache(maxsize=None)
    @log_calls
    def _area_cached(radius):
        return math.pi * radius ** 2