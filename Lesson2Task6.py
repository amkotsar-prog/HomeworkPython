goods = []
character = {'название': '', 'цена': '', 'количество': '', 'единица измерения': ''}
analytics = {'название': [], 'цена': [], 'количество': [], 'единица измерения': []}
num = 0

while True:
    if input('Для выхода из программы нажмите "Q", для продолжения "Enter": ') .upper() == 'Q':
        break
    num += 1
    character = character.copy()
    for el in character:
        inf = input(f'Введите значение свойства "{el}": ')
        character[el] = int(inf) if inf == 'цена' or inf == 'количество' else inf
        analytics[el].append(character[el])
    goods.append((num, character))
    print(f"\nСтруктура товаров\n{goods}")
    print(f'\nСтруктура аналитики по товарам:\n')
    for key, value in analytics.items():
        print(f'{key},{value}')
