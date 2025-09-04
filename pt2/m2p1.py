ans=0
b=5
while ans!=b:
    ans=int(input())
    if ans>b:
        print('Число меньше!')
    elif ans<b:
        print('Число больше')
    else:
        print('Ты выиграл!')

