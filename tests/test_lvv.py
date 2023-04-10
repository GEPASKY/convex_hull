from pytest import approx
from math import sqrt
from r2point import R2Point
from convex import Figure, Void, Point, Segment, Polygon


def test_000():
    Figure.p1 = R2Point(0, 3)
    Figure.p2 = R2Point(3, 2)
    t = Polygon(R2Point(5, 0), R2Point(2, -1), R2Point(-2, -1))
    t = t.add(R2Point(-5, 0))
    t = t.add(R2Point(0, -6))
    assert t.g() == 1

def test_001():
    Figure.p1 = R2Point(0, 0)
    Figure.p2 = R2Point(10, 10)
    t = Polygon(R2Point(0, 0), R2Point(10, 10), R2Point(-2, -1))
    t = t.add(R2Point(-5, 0))
    t = t.add(R2Point(0, -6))
    assert t.g() == 2

def test_010():
    Figure.p1 = R2Point(0, 3)
    Figure.p2 = R2Point(3, 2)
    t = Polygon(R2Point(-5, 0), R2Point(5, 0), R2Point(2, 3))
    t = t.add(R2Point(-2, -3))
    t = t.add(R2Point(0, -6))
    assert t.g() == 1


def test_100():
    Figure.p1 = R2Point(0, 3)
    Figure.p2 = R2Point(3, 2)
    t = Point(R2Point(3, 2))
    assert t.g() == 0
