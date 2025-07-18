# VarArgs - Variable number of Arguments - переменное число аргументов

def total(a=5, *numbers, **phonebook):
    print('a', a)

    # проход по всем элементам кортежа
    for single_item in numbers:
        print('single_item', single_item)

    # проход по всем элементам словаря
    for first_part, second_part in phonebook.items():
        print(first_part, second_part)

# total(10, 1, 2,3, Jack=2231, John=2321, Inge=1560)
print(total(10, 1, 2,3, Jack=2231, John=2321, Inge=1560))