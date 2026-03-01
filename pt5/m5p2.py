import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set(self, x, y):
        self.x = x
        self.y = y

    def get(self):
        return self.x, self.y

    def get_distance(self, p2):
        dx = p2.x - self.x
        dy = p2.y - self.y
        return math.sqrt(dx ** 2 + dy ** 2)

    def get_angle(self, p2):
        dx = p2.x - self.x
        dy = p2.y - self.y
        return math.degrees(math.atan2(dy, dx))

    def move(self, length, angle):
        rad = math.radians(angle)
        self.x += length * math.cos(rad)
        self.y += length * math.sin(rad)


p1 = Point(1,0)
p2 = Point(5, 12)

print("Стартовая точка:", p1.get())

print("Расстояние:", p1.get_distance(p2))
print("Угол:", p1.get_angle(p2))

p1.move(10, 0)
print("Новая позиция:", p1.get())

