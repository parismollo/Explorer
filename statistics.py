from typing import List
from linear_algebra import sum_of_squares

def mean(xs: List[float]) -> float:
    return sum(xs)/ len(xs)

assert mean([1, 2, 3]) == 2


def de_mean(xs: List[float]) -> List[float]:
    x_bar = mean(xs)
    return [x_i - x_bar for x_i in xs]

def variance(xs: List[float]) -> float:
    assert len(xs) >= 2, "at least 2 values"
    n = len(xs)

    deviations = de_mean(xs)
    return sum_of_squares(deviations)/ (n - 1)


import math

def standard_deviation(xs: List[float]) -> float:
    return math.sqrt(variance(xs))
