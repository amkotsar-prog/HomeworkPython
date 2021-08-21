def my_func(x, y):
    x, y = float(x), int(y)
    power_res = 1
    for el in range (abs(y)):
        power_res /= x
    return f'Результат возведения x в степень y : {power_res}'


x = input('Введите положительное действительное число: ')
y = input('Введите целое отрицательное число: ')

print(my_func(x, y))

