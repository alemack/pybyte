import pickle

# имя файла, в котором мы сохраним объект
shoplistfile = 'shoplist.data'
# список покупок
shoplist = ['яблоки', 'манго', 'морковь']

# Запись в файл
f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f) # помещаем объект в файл
f.close()

del shoplist # уничтожаем переменную shoplist

f = open(shoplistfile, 'rb')
storedlist = pickle.load(f) # загружаем объект их файла
print(storedlist)
