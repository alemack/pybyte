# 'ab' - сокращение от 'a'dress 'b'ook

ab = { 'Swaroop' : 'swaroop@swaroop.com',
       'Larry' : 'larry@larry.com',
       'Matsumoto' : 'matsumoto@matsumoto.com',
       'Spammer' : 'spammer@hostmail.com'
    }

print("Адрес Swaroop'a:", ab['Swaroop'])

# Удаление пары ключ-значение
del ab['Spammer']

print('\nВ адресной книге {0} контакта\n'.format(len(ab)))

for name, adresss in ab.items():
    print('Контакт {0} с адресом {1}'.format(name, adresss))

# Добавление пары ключ-значение
ab['Guido'] = 'guid@mail.com'

if 'Guido' in ab:
    print("\nАдрес Guido:", ab['Guido'])