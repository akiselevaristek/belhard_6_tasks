"""
Написать композицию из функций (не чистых функций)

Имеется словарь SCHOOL_DATA с данными школы класс-количество учеников

- Функция incr_students, которая принимает SCHOOL_DATA, название класса и
    увеличивает количество учеников на 1
- Функция decr_students, которая принимает SCHOOL_DATA, название класса и
    уменьшает количество учеников на 1, но не меньше 0
- Функция add_class, которая принимает SCHOOL_DATA, название класса и добавляет
    класс в словарь с количеством учеников 0
- Функция remove_class, которая принимает SCHOOL_DATA, название класса и удаляет
    класс из словаря
- Функция calc_students, которая принимает SCHOOL_DATA и возвращает кол-во
    учеников во всей школе
"""
school_data = {
    '1a': 15,
    '1b': 23,
    '2a': 13,
    '2b': 30
}


def incr_students(data, cls):
    data[cls] = data.get(cls) + 1


def decr_students(data, cls):
    if data[cls] >= 0:
        data[cls] = data.get(cls) - 1


def add_class(data, cls):
    data.update({cls: 0})


def remove_class(data, cls):
    del data[cls]


def calc_students(data):
    return sum(data.values())


if __name__ == '__main__':
    incr_students(school_data, '1a')
    decr_students(school_data, '1a')
    add_class(school_data, '7z')
    remove_class(school_data, '2b')
    print(calc_students(school_data))







#
#
# def incr_students(exp1: dict, exp2):
#     exp1[exp2] = exp1.get(exp2) + 1
#
#
# def decr_students(exp1: dict, exp2):
#     if exp1.get(exp2) > 0:
#         exp1[exp2] = exp1.get(exp2) - 1
#     else:
#         print("Количество учеников в классе должно быть больше 0")
#
#
# def add_class(exp1: dict, exp2):
#     exp1.update({exp2: 0})
#
#
# def remove_class(exp1: dict, exp2):
#     del exp1[exp2]
#
#
# def calc_students(exp1: dict):
#     return print(sum(exp1.values()))
#
#
# if __name__ == '__main__':
#     print(school_data)
#     incr_students(school_data, '1a')
#     decr_students(school_data, '1b')
#     add_class(school_data, '3a')
#     remove_class(school_data, '2a')
#     calc_students(school_data)
#     print(school_data)