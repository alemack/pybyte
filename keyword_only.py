# Только ключевые параметры

def total(initial=5, *numbers, extra_number):
    count = initial
    for number in numbers:
        count += number
    count += extra_number
    print(count)

total(10, 1,2,3, extra_number=50)

# Вызовет ошибку, поскольку мы не указали значение
# аргумента по умолчанию для 'extra_number'
# total(10, 1,2,3)

# МОЖНО ВОТ ТАК ЕЩЕ, ЕСЛИ НАМ НЕ НУЖЕН ПАРАМЕТР СО ЗВЁЗДОЧКОЙ
# Если вам нужны аргументы, передаваемые только по ключу, но не нужен па-
# раметр со звёздочкой, то можно просто указать одну звёздочку без указания
# имени: def total(initial=5, *, extra_number).
