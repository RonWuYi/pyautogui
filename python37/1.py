# @dataclass
from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float
    z: float = 0.9

p = Point(1.5, 2.5)
print(p)
print(p.x)