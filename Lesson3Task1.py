def div(s1, s2):
    try:
        print(round(s1 / s2, 4))
    except ZeroDivisionError:
        print('Деление на ноль запрещено!')


s1 = int(input('Введите первое число: '))
s2 = int(input('Введите второе число: '))
div(s1, s2)



