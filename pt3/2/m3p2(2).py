from random import randint

n = 5
m = [[randint(0, 100) for i in range(n)] for j in range(n)]
list_end = []
for row in m:
    for elem in row:
        list_end.append(elem)
print(list_end)
list_end = sorted(list_end)
print(list_end[-1])


