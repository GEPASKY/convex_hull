#!/usr/bin/env -S python3 -B
from r2point import R2Point
from r2point import R2Point
from convex import Void, Figure

f = Void()

Figure.p1 = R2Point()
Figure.p2 = R2Point()
try:
    while True:
        f = f.add(R2Point())
        print(f"S = {f.area()}, P = {f.perimeter()}\n, G = {f.g()}")
        print()
except(EOFError, KeyboardInterrupt):
    print("\nStop")
