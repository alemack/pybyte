def reverse(text):
    return text[::-1]

def clean_text(text):
    forbidden = (' ', '!', '?', '.', ',', ':', ';', '-', '—', '(', ')', '"', "'", '«', '»')
    text = text.lower()
    cleaned = ''
    for char in text:
        if char not in forbidden:
            cleaned += char
    return cleaned

def is_palindrome(text):
    cleaned = clean_text(text)
    return cleaned == reverse(text)

something = input('Введите текст: ')

if is_palindrome(something):
    print('Да, это палиндром')
else:
    print('Нет, это не палиндром')