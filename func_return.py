# Оператор return

def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'Числа равны.'
    else:
        return y

print(maximum(3,7))

# Оператор pass используется в Python для обозначения пустого блока команд.

def someFunction():
    pass

print(someFunction())
# print(help(None))
