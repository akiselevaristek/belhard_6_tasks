"""
Написать функцию to_set, которая принимает список, а возвращает множество,
созданное из этого списка и длину этого множества
"""
spisok = [1, 2, 2, 4, 5, 6, 7, 7]


def to_set(list_exp: list):
    mn = set(list_exp)
    return mn, len(mn)


if __name__ == "__main__":
    print(to_set(spisok))
