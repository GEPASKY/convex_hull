#!/usr/bin/env -S python3 -B
from tk_drawer import TkDrawer
from r2point import R2Point
from convex import Void, Point, Segment, Polygon, Figure


def void_draw(self, tk):
    pass


def point_draw(self, tk):
    tk.draw_point(self.p,
                      flag=self.p.is_near_p1(self.p1, self.p2))


def segment_draw(self, tk):
    tk.draw_line(self.p, self.q)
    tk.draw_point(self.p,
                      flag=self.p.is_near_p1(self.p1, self.p2))
    tk.draw_point(self.q,
                      flag=self.q.is_near_p1(self.p1, self.p2))


def polygon_draw(self, tk):
    for n in range(self.points.size()):
        tk.draw_line(self.points.last(), self.points.first())
        tk.draw_point(self.points.first(),
                      flag=self.points.first().is_near_p1(self.p1, self.p2))
        self.points.push_last(self.points.pop_first())


setattr(Void, 'draw', void_draw)
setattr(Point, 'draw', point_draw)
setattr(Segment, 'draw', segment_draw)
setattr(Polygon, 'draw', polygon_draw)


tk = TkDrawer()
f = Void()
tk.clean()

print('Задание фиксированных точек:')
Figure.p1 = R2Point()
Figure.p2 = R2Point()
print('Точки плоскости:')

try:
    while True:
        f = f.add(R2Point())
        tk.clean()
        f.draw(tk)
        print(f"S = {f.area()}, P = {f.perimeter()}\n, G = {f.g()}")
except(EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()
