from .base import Shape2D
from functools import lru_cache
from .logging_decorator import log_calls

class Rectangle(Shape2D):
    def __init__(self, a: float, b: float) -> None:
        self.a = a
        self.b = b

    def area(self) -> float:
        return self._area_cached(self.a, self.b)

    def corner_count(self) -> int:
        return 4
    
    @staticmethod
    @lru_cache(maxsize=None)
    @log_calls
    def _area_cached(a, b):
        return a * b