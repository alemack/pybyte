import time

try:
    f = open('poem.txt', 'r', encoding='utf-8')
    while True: # наш обычный способ читать файлы
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')
        time.sleep(2) # Пусть подождёт некоторое время
except KeyboardInterrupt:
    print('!! Вы отменили чтение файла.')
finally:
    f.close()
    print('(Очистка: Закрытие файла)')