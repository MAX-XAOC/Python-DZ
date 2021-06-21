def my_func(arg_1, arg_2, arg_3):
    spisok = [arg_1, arg_2, arg_3]
    try:
        spisok.remove(min(spisok))
        return sum(spisok)
    except TypeError:
        return "Введите только числа"

print(my_func(1, 2, 3))