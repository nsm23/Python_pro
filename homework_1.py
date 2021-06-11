"""Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате
и проверить тип и содержание соответствующих переменных. Затем с помощью онлайн-конвертера
преобразовать строковые представление в формат Unicode и также проверить тип и содержимое переменных."""
print('--------------task_1----------------------')
list = ['разработка', 'сокет', 'декоратор']
for i in list:
    print(f'{i} - {type(i)} - {len(i)}')  # (f'содержание - {i}, тип - {type(i)}, длинна - {len(i)}\n')
print('***********************************')
# https://calcsbox.com/post/konverter-teksta-v-unikod.html
list_2 = ['\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
          '\u0441\u043e\u043a\u0435\u0442', '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440']
for i in list_2:
    print(f'{i} - {type(i)} - {len(i)}')
print('***********************************')
print(list == list_2)

print('---------------task_2-----------------------')
"""Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов
(не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных."""

list_b = [b'class', b'function', b'method']
for i in list_b:
    print(f'{i} - {type(i)} - {len(i)}')

print('---------------task_3-----------------------')
"""Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе."""
# list = [b'attribute', b'класс', b'функция', b'type']
# for i in list:
#    print(i)
# нельзя записать "класс" и "функция"т.к. поддерживается только латиница
# SyntaxError: bytes can only contain ASCII literal characters.

print('---------------task_4-----------------------')
"""Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления
в байтовое и выполнить обратное преобразование (используя методы encode и decode)."""
list = ['разработка', 'администрирование', 'protocol', 'standart']
for i in list:
    i_enc = i.encode('utf-8')
    i_dec = bytes.decode(i_enc, 'utf-8')
    print(f'{i_enc} - {i_dec}\n')
# b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0' - разработка
# b'\xd0\xb0\xd0\xb4\xd0\xbc\xd0\xb8\xd0\xbd\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0\xb8\xd1\
# x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5' - администрирование
# b'protocol' - protocol
# b'standart' - standart

print('---------------task_5-----------------------')
"""Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип
на кириллице."""
import subprocess

ping_saits = [['ping', 'yandex.ru'], ['ping', 'youtube.com']]
for i in ping_saits:
    ping_process = subprocess.Popen(i, stdout=subprocess.PIPE)
    for line in ping_process.stdout:
        print(line)
        line = line.decode('cp866').encode('utf-8')
        print(line.decode('utf-8'))

print('---------------task_6-----------------------')
"""Создать текстовый файл test_file.txt, заполнить его тремя строками:
«сетевое программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию. 
Принудительно открыть файл в формате Unicode и вывести его содержимое."""
import locale

print(f'кодировка - {locale.getpreferredencoding()}')

list = ['python', 'базы данных', 'linux', 'django']
with open('test_file.txt', 'w+') as f_n:
    for i in list:
        f_n.write(i + '\n')
    f_n.seek(0)

# Чтение из файла
with open('test_file.txt', 'r', encoding='cp1251') as f_n:
    for i in f_n:
        print(i)
    f_n.seek(0)
