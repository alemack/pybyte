shoplist = ['яблоки', 'манго', 'морковь', 'бананы']
name = 'alex'

# Операция индексирования
print('Операция индексирования')
print('Элемент 0 -', shoplist[0])
print('Элемент 1 -', shoplist[1])
print('Элемент 2 -', shoplist[2])
print('Элемент 3 -', shoplist[3])
print('Элемент -1 -', shoplist[-1])
print('Элемент -2 -', shoplist[-2])
print('Символ 0  -', name[0])

# Вырезка из списка
print('Вырезка из списка')
print('Элементы с 1 по 3:', shoplist[1:3])
print('Элементы с 2 до конца:', shoplist[2:])
print('Элементы с 1 по -1:', shoplist[1:-1])
print('Элементы от начала до конца:', shoplist[:])

# Вырезка из строки
print('Вырезка из строки')
print('Символы с 1с по 3:', name[1:3])
print('Символы с 2 до конца:', name[2:])
print('Символы с 1 до -1:', name[1:-1])
print('Символы от начала до конца:', name[:])

# Изменяем шаг вырезки
print('Изменяем шаг вырезки')
print('Шаг 1: ', shoplist[::1])
print('Шаг 2: ', shoplist[::2])
print('Шаг 3: ', shoplist[::3])
print('Шаг 1-: ', shoplist[::-1])


seq = ['a', 'b', 'c', 'd', 'e']

# Проверка вхождения
print('Проверка вхождения')
print('b' in seq) # True

# Итерация
print('Итерация')
for x in seq: print(x)