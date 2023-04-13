"""
Задание 5.
Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.
"""
import subprocess
from chardet import detect

sites = [['ping', 'yandex.ru'], ['ping', 'youtube.com']]
for site in sites:
    p = subprocess.Popen(site, stdout=subprocess.PIPE)
    for line in p.stdout:
        print(line.decode(detect(line)['encoding']))