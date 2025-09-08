import random

a, b = map(int, input("Введите диапазон через пробел: ").split())
n = int(input('Количество чисел: '))
my_set = set()
while len(my_set) < n:
    my_set.add(random.randint(a, b))

my_list = list(my_set)
print(my_list)

def change (my_list):
    for i in range(1, len(my_list)):
        key = my_list[i]
        j = i - 1
        while j >= 0 and my_list[j] > key:
            my_list[j + 1] = my_list[j]
            j -= 1
        my_list[j + 1] = key
    return my_list

print(f'После сортировки: {change(my_list)}')
