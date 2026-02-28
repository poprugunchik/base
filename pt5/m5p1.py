class StringVar:
    def __init__(self, value=""):
        self._value = str(value)

    def set(self, value):
        self._value = str(value)

    def get(self):
        return self._value


my_string = StringVar()
print("Начальное значение:", my_string.get())

my_string.set("Новое значение")
print("Первая итерация:", my_string.get())

my_string.set("Забавное задание")
print("Конечное значение:", my_string.get())
