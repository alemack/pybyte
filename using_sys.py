import sys
import os

print('Аргументы командной строки:')
for i in sys.argv:
    print(i)

print('\n\Переменная PYTHONPATH содержит', sys.path, '\n')

print('--')
print(os.getcwd())