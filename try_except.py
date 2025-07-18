try:
    text = input('Введите что-нибудь --> ')
except EOFError:
    print('Ну зачем вы сделали мне EOF?')
except KeyboardInterrupt:
    print('Вы отменили операцию.')
else:
    print('Вы ввели {0}'.format(text))




# try:
#     # опасный код
# except ValueError:
#     # обработка конкретной ошибки
# except Exception:
#     # обработка других ошибок
# else:
#     # выполнится, если не было исключений!
# finally:
#     # выполнится всегда, даже если была ошибка или break/return
