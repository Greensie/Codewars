# https://www.codewars.com/kata/58dceee2c9613aacb40000b9/train/python
from math import sqrt


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


def distance_between_points(a: Point, b: Point) -> float:
    return sqrt(pow((a.x - b.x), 2) + pow((a.y - b.y), 2) + pow((a.z - b.z), 2))
