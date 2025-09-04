x=int(input('Введите 1 число'))
y=int(input('Введите 2 число'))
z=int(input('Введите 3 число'))

if x == y or x == z:
    if y == z:
        print("3")
    else:
        print("2")
elif y == z:
    print("2")
else:
    print ('0')
