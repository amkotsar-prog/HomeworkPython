arg1 = int(input('Введите первый аргумент: '))
arg2 = int(input('Введите второй аргумент: '))
arg3 = int(input('Введите третий аргумент: '))


def my_func(arg1, arg2, arg3):
    my_list = [arg1, arg2, arg3]
    my_list.remove(min(my_list))
    print(sum(my_list ))


my_func(arg1, arg2, arg3)