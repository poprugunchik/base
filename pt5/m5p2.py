class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set(self, x, y):
        self.x = x
        self.y = y

    def get(self):
        return self.x, self.y


p = Point(1,2)

print("Стартовая точка:", p.get())

p.set(5,12)
print("Промежуточная точка:", p.get())

p.set(15,15)
print("Конечная точка:", p.get())

