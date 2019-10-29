from typing import List


Vector = List[float]

def subtract(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w)
    return [v_i - w_i for v_i, w_i in zip(v, w)]
assert subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]


def dot(v: Vector, w: Vector) -> float:
    assert len(v) == len(w)," vectors musth have the same length"
    return sum([v_i * w_i for v_i, w_i in zip(v, w)])

assert dot([1, 2, 3], [4, 5, 6]) == 32

def sum_of_squares(v: Vector) -> float:
    return dot(v, v)

assert sum_of_squares([1, 2, 3]) == 14


def squared_distance(v: Vector, w: Vector) -> float:
    return sum_of_squares(subtract(v, w))


import math

def distance(v: Vector, w: Vector) -> float:
    return math.sqrt(squared_distance(v, w))
