"""
Задание 4.
Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).
"""

words = ['разработка', 'администрирование', 'protocol']
words_b = [word.encode('utf-8') for word in words]
print(*words_b, sep='\n')
for word in words_b:
    print(word.decode('utf-8'))
