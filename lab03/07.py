import math

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, x, y):
        self.x, self.y = x, y

    def dist(self, p):
        return math.sqrt((self.x - p.x)**2 + (self.y - p.y)**2)

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

p1 = Point(x1, y1)
p1.show()
p1.move(x2, y2)
p1.show()
print(f"{p1.dist(Point(x3, y3)):.2f}")
