import random

a, b = map(int, input("Введите диапазон через пробел: ").split())
n=int(input('Количество чисел: '))
x=int(input('Искомое число: '))


my_set = set()
while len(my_set) < n:
    my_set.add(random.randint(a, b))

list_numbers=sorted(list(my_set))

print("Наш список:", list_numbers)
print("Ищем число:", x)

left = 0
right = len(list_numbers)-1
def search (left, right):
    if left > right:
        return -1
    mid = (left + right) // 2

    if list_numbers[mid] == x:
        return mid
    elif list_numbers[mid] < x:
        return search  (mid+1, right)
    else:
        return search (left, mid-1)
index = search(0, len(list_numbers)-1)
if index != -1:
    print(f"Число {x} найдено, индекс {index}")
else:
    print(f"Число {x} не найдено")



