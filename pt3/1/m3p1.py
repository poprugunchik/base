x=float(input('Ваш вклад: '))
y=float(input('Итоговая сумма: '))
p=float(input('Процент: '))
cash = x
year = 0

while cash<y:
    percent = (cash * p) / 100
    cash += int(percent)
    year += 1
    print(int(cash))
if year == 11:
    print(f'Для достижении цели потребуется {year} лет')
elif year % 10 in (2,3,4):
    print(f'Для достижении цели потребуется {year} года')
elif year % 10 == 1:
    print(f'Для достижении цели потребуется {year} год')
else:
    print(f'Для достижении цели потребуется {year} лет')

