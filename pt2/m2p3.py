ans = 'пароль'
password = ''
i = 0
n = 3
while i<n:
    password = str(input('Введите пароль: '))
    if password == ans:
        print('Принят')
        break
    else:
        i += 1
        if i < n:
            print(f'Неверно, осталось попыток: {n - i}')

else:
    print('Повторите позже')
