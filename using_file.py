poem = """\
Программировать весело.
Если работа скучна, 
Чтобы придать её весёлый тон - 
    используй Python!
"""

f = open('poem.txt', 'w', encoding='utf-8') # открываем для записи (writing)
f.write(poem) # записываем текст в файл
f.close() # закрываем файл

f = open('poem.txt', encoding='utf-8') # если не указан режим, по умолчанию подразумевается
                   # режим чтения ('r'eading)
while True:
    line = f.readline()
    if len(line) == 0: # Нулевая длина обозначает конец файла (EOF - End Of File)
        break
    print(line, end='')

f.close() # закрываем файл

# СЕЙЧАС АКТУАЛЬНО ИСПОЛЬЗОВАТЬ КОНТЕКСТНЫЙ МЕНЕДЖЕР WITH AS
poem = """\
Программировать весело.
Если работа скучна, 
Чтобы придать её весёлый тон - 
    используй Python!
"""

with open('poem.txt', 'w', encoding='utf-8') as f:
    f.write(poem)  # файл открыт только внутри этого блока

with open('poem.txt', encoding='utf-8') as f:
    for line in f:
        print(line, end='')  # файл автоматически закроется после блока
