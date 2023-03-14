"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!"""


import subprocess
import chardet
import os


servers = ['yandex.ru', 'youtube.com']
for i in servers:
    ping = subprocess.Popen(['ping', i], stdout=subprocess.PIPE)
    for line in ping.stdout:
        result = chardet.detect(line)
        print(line.decode(result['encoding']))

print(os.name)
print(result)