month = int(input('Введите месяц в виде целого числа: '))

my_list = ["winter", "spring", "summer", "autumn", "winter"]
my_dict = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn', 5: 'winter'}

print(f'This month is {my_list [month // 3]} (from the list)!')
print(f'This month is {my_dict [month // 3 + 1]} (from the dictionary)!')



