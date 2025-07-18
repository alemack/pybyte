listone = [2, 3, 4]

# эквивалент "традиционного" цикла
result = []
for i in listone:
    if i > 2:
        result.append(2*i)

# то же самое через list comprehension
result = [2*i for i in listone if i > 2]