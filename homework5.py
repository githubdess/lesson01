tuple_ = immutable_var = 15, 3.14, 'Aloha', False  # - задание 2
print('Immutable var:', tuple_)
# - tuple_[2] = 'Hawaii'    # - задание 3
print('Immutable var:', tuple_)
# "в отличие от списка (list) значение элемента в коллекции кортежа (tuple) изменить не получится,"
# "так как он относится к неизменяемым типам данных и не поддерживает обращение по элементам"
mutable_list = [91, 'A Broken Silence', 261, False, 'K']   # - задание 4
print('Mutable list:', mutable_list)
mutable_list[0] = 91 - 19.19
mutable_list[1] = 'Impending Doom'
print('Mutable list:', mutable_list)
