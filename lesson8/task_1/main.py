"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.

Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список
для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;

Пример того, что должно получиться:

Изготовитель системы,Название ОС,Код продукта,Тип системы

1,LENOVO,Windows 7,00971-OEM-1982661-00231,x64-based

2,ACER,Windows 10,00971-OEM-1982661-00231,x64-based

3,DELL,Windows 8.1,00971-OEM-1982661-00231,x86-based

Обязательно проверьте, что у вас получается примерно то же самое.

ПРОШУ ВАС НЕ УДАЛЯТЬ СЛУЖЕБНЫЕ ФАЙЛЫ TXT И ИТОГОВЫЙ ФАЙЛ CSV!!!
"""
import os
import re
import csv

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


def collect_data():
    data_dir = os.path.join(CURRENT_DIR)
    result = []
    source_files = [i for i in os.listdir(data_dir) if i.split('.')[1] == 'txt']

    for filename in source_files:
        filepath = os.path.join(data_dir, filename)

        with open(filepath) as fl:
            for line in fl.readlines():
                result += re.findall(r'^(\w[^:]+).*:\s+([^:\n]+)\s*$', line)

    return result


def get_data():
    data = collect_data()
    os_prod, os_name, os_code, os_type = [], [], [], []
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]

    for item in data:
        os_prod.append(item[1]) if item[0] == main_data[0][0] else None
        os_name.append(item[1]) if item[0] == main_data[0][1] else None
        os_code.append(item[1]) if item[0] == main_data[0][2] else None
        os_type.append(item[1]) if item[0] == main_data[0][3] else None

    for i in range(len(os_prod)):
        main_data.append([os_prod[i], os_name[i], os_code[i], os_type[i]])

    return main_data


def write_to_csv(filepath):
    data = get_data()

    dir_, filename = os.path.split(filepath)

    os.makedirs(dir_, exist_ok=True)

    filepath = os.path.join(CURRENT_DIR, dir_, filename)

    with open(filepath, 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)

        for line in data:
            writer.writerow(line)

    print(f'Данные сохранены в {filepath}')



write_to_csv('task_1/source/report.csv')

#os_prod_reg = re.compile(r'Изготовитель системы:\s*\S*')
#os_prod_list.append(os_prod_reg.findall(data)[0].split()[2])