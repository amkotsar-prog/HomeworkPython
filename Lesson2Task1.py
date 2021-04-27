my_list = [True, 233, 35.35, 'dfghj', None, [5, 4, 7, 90], (56, 78, 94, 23), complex(8, 9),
           {1: 'one', 2: 'two', 3: 'three', 4: 'four'}, TypeError, {89, 96, 56, 23}, range(16), b'57']

for ind, el in enumerate(my_list):
    print(ind, el, type(el))
