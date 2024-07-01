my_dict = {'Denis': 1981, 'Pavel': 1936, 'Andrey': 1966}
print('Dict:', my_dict)
print('Existing value:', my_dict['Denis'])
print('Not existing value:', my_dict.get('Kseniya'))
my_dict.update({'Luka': 2017, 'Liza': 2021})
d = my_dict.pop('Pavel')
print(f'Deleted value: {d}')
print('Modified dictionary:', my_dict)
my_set = {'A', 1, 1, 4, 'B', (3, 2), 'A', 4, False}
print('Set:', my_set)
my_set.add('C')
my_set.add(8.615)
my_set.remove((3, 2))
print('Modified set:', my_set)
