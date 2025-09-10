from .base import Shape2D
from functools import lru_cache
from .logging_decorator import log_calls

class Triangle(Shape2D):
    def __init__(self, a: float, b: float, c: float) -> None:
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        return self._area_cached(self.a, self.b, self.c)

    def corner_count(self) -> int:
        return 3
    
    @staticmethod
    @lru_cache(maxsize=None)
    @log_calls
    def _area_cached(a, b, c):
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5

    
