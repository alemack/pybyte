print('Простое присваивание')
shoplist = ['яблоко', 'манго', 'морковь', 'бананы']
mylist = shoplist # mylist - лиш ещё одно имя, указывающее на тот же объект!

del shoplist[0] # Я сделал первую покупку, поэтому удаляю её из списка

print('shoplist:', shoplist)
print('mylist:', mylist)
# Обратите внимание, что и shoplist, и mylist выводят один и тот же список
# без пункта "яблоко", подтверждая тем самым, что они указывают на один
# объект.

print('Копирование при помощи поолной вырезки')
mylist = shoplist[:]
del mylist[0]

print('shoplist:', shoplist)
print('mylist:', mylist)
# Обратите внимание, что теперь списки разные