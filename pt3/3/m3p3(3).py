import random
from functools import cmp_to_key  #Вот это честно загуглил)

n = int(input())
arr = [random.randint(0, 100) for _ in range(n)]
arr_str = []
def compare(x, y):
    return int(y + x) - int(x + y) #Да и это загуглил как произвести сравнение
for num in arr:
    arr_str.append(str(num))
print(arr_str) #оставил для наглядности, но в целом, чисто отладочное решение
arr_str.sort(key=cmp_to_key(compare)) #ну и аналогично, что не сам придумал
big_number = ''.join(arr_str)
print(big_number)

#официально заявляю, что в модуле не хватало  разборов каких-то доп.функций)
#гпт предлагал делать через map, но в целом, вообще не в курсе что это