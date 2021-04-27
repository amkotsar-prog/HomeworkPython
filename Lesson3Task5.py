def my_sum():
    sum = 0
    while True:
        my_list = input('Введите числа через пробел, либо символ “Q” для выхода:').split()
        for num in my_list:
            if num == "Q":
                return sum
            else:
                sum += int(num)
        print(f'Сумма чисел = {sum}')


print(my_sum())