import csv
import re


def get_data():
    main_list = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    file_list = ['info_1.txt', 'info_2.txt', 'info_3.txt']
    for i in file_list:
            with open(i, encoding='cp1251') as file:
                string = file.read()
                sistem_production = re.findall(main_list[0] + r".{1,}", string)[0].split('  ')[-1].strip()
                os_name = re.findall(main_list[1] + r".{1,}", string)[0].split('  ')[-1].strip()
                product_code = re.findall(main_list[2] + r".{1,}", string)[0].split('  ')[-1].strip()
                sistem_type = re.findall(main_list[3] + r".{1,}", string)[0].split('  ')[-1].strip()

                main_list.append(sistem_production)
                main_list.append(os_name)
                main_list.append(product_code)
                main_list.append(sistem_type)

    return main_list


def write_to_csv(new_file):
    list_to_write = get_data()
    with open(new_file, 'w') as n_f:
        n_f_writer = csv.writer(n_f)
        for row in list_to_write:
            n_f_writer.writerow(row)

write_to_csv('new_file.csv')