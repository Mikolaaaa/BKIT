from operator import itemgetter

class Filedir:
    """Каталог файлов"""
    def __init__(self, id, name):
        self.id = id
        self.name = name


class File:
    """Файл"""
    def __init__(self, id, name, size, dir_id):
        self.id = id
        self.name = name
        self.size = size
        self.dir_id = dir_id


class FiledirFile:
    """
    'Файлы в каталоге' для реализации
    связи многие-ко-многим
    """
    def __init__(self, Filedir_id, File_id):
        self.Filedir_id = Filedir_id
        self.File_id = File_id


File_dirs = [
    Filedir(1, 'отдых'),
    Filedir(2, 'учёба'),
    Filedir(3, 'телефон'),

    Filedir(11, 'отдых (другой)'),
    Filedir(22, 'учёба (другая)'),
    Filedir(33, 'телефон (другой)'),
]

Files = [
    File(1, 'Крым', 4036, 1),
    File(2, 'Резерваная копия', 349803, 3),
    File(3, 'Турция', 12089, 1),
    File(4, 'конспект', 4036, 2),
    File(5, 'программы', 9836, 3),
    File(6, 'Демидович учебник', 59836, 2),
    File(7, 'Лаба3', 2638, 2),
]

File_dir_File = [
    FiledirFile(1, 1),
    FiledirFile(1, 3),
    FiledirFile(2, 4),
    FiledirFile(3, 2),
    FiledirFile(3, 5),

    FiledirFile(11, 1),
    FiledirFile(11, 3),
    FiledirFile(22, 4),
    FiledirFile(33, 2),
    FiledirFile(33, 5),
]


def main():
    """Основная функция"""
    # Соединение данных один-ко-многим
    one_to_many = [(f.name, f.size, d.name)
                   for d in File_dirs
                   for f in Files
                   if f.dir_id == d.id]
    many_to_many_temp = [(d.name, fd.Filedir_id, fd.File_id)
                         for d in File_dirs
                         for fd in File_dir_File
                         if d.id == fd.Filedir_id]

    many_to_many = [(f.name, f.size, dir_name)
                    for dir_name, dir_id, File_id in many_to_many_temp
                    for f in Files if f.id == File_id]
    print('Задание Б1')
    print(B1(one_to_many))
    print('Задание Б2')
    print(B2(one_to_many))
    print('Задание Б3')
    print(B3(many_to_many))


def B1(one_to_many):
    res_11 = sorted(one_to_many, key=lambda x: x[0].lower())
    return res_11


def B2(one_to_many):
    res_12_unsorted = []
    # Перебираем все отделы
    for d in File_dirs:
        # Список сотрудников отдела
        d_Files = list(filter(lambda i: i[2] == d.name, one_to_many))
        # Если отдел не пустой
        if len(d_Files) > 0:
            # Зарплаты сотрудников отдела
            res_12_unsorted.append((d.name, len(d_Files)))

    # Сортировка по суммарной зарплате
    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    return res_12

def B3(many_to_many):
    res_13 = {}
    # Перебираем все отделы
    for f in Files:
        if f.name.endswith('ия'):
            # Список сотрудников отдела
            f_dirs = list(filter(lambda i: i[0] == f.name, many_to_many))
            # Только ФИО сотрудников
            f_dirs_names = [x for _, _, x in f_dirs]
            # Добавляем результат в словарь
            # ключ - отдел, значение - список фамилий
            res_13[f.name] = f_dirs_names
    return res_13


if __name__ == '__main__':
    main()
