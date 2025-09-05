l = [1, 4, 1, 6, "hello", "а", 5, "hello"]
l = sorted(l, key=str)
list_o = []
list_repeat = []
for i in range(len(l)):
    if i > 0 and l[i] == l[i - 1]:
        list_repeat.append(l[i])
    else:
        list_o.append(l[i])
print('Уникальные :',list_o)
print('Повтор:',list_repeat)