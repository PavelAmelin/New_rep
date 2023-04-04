import csv
import re
lst = ['info_1.txt', 'info_2.txt', 'info_3.txt']

def get_data(file_lst):
    main_d = []
    for f in file_lst:
        with open(f, 'r') as obj:
            a = obj.read()
            start1 = a.find('Изготовитель системы')
            end1 = a[start1: a.find('Модель системы')].strip().split('  ')
            main_d.append(end1[-1][1:])
            start2 = a.find('Название ОС')
            end2 = a[start2: a.find('Версия ОС')].strip().split('  ')
            main_d.append(' '.join(end2[-1].split()[1:3]))
            start3 = a.find('Код продукта')
            end3 = a[start3: a.find('Дата установки')].strip().split('   ')
            main_d.append(end3[-1])
            start4 = a.find('Тип системы')
            end4 = a[start4: a.find('Процессор(ы)')].strip().split('  ')
            main_d.append(end4[-1])
    return [main_d[i:i + 4] for i in range(0, len(main_d), 4)]

# def get_data(file_lst):
#     main_d = []
#     for f in file_lst:
#         with open(f, 'r') as obj:
#             a = obj.read()
#             d1 = re.compile(r'Изготовитель системы:\s*\S*')
#             d2 = re.compile(r'Название ОС:\s*\S*\s*\S*\s*\S*')
#             d3 = re.compile(r'Код продукта:\s*\S*')
#             d4 = re.compile(r'Тип системы:\s*\S*')
#             main_d.append(d1.findall(a)[0].split()[2])
#             main_d.append(' '.join(d2.findall(a)[0].split()[-2:]))
#             main_d.append(d3.findall(a)[0].split()[2])
#             main_d.append(d4.findall(a)[0].split()[2])
#     return [main_d[i:i + 4] for i in range(0, len(main_d), 4)]

def write_to_csv():
    with open('data_report.csv', 'w', encoding='utf-8', newline='') as out:
        d = get_data(lst)
        wr = csv.writer(out)
        wr.writerow(['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы'])
        for i, row in enumerate(d, 1):
            wr.writerow((i, *row))

write_to_csv()

