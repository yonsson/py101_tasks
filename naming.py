"""Задания по стилю кода и именованию переменных."""

# напиши команду, которая проверяет, ссылаются ли
# переменные spam и eggs на один и тот же объект в пямяти
spam = None
eggs = None
if id(spam) == id(eggs):
    print('Переменные ссылаются на один и тот же объект в памяти')
else:
    print('Переменные ссылаются на разные объекты в памяти')

# придумай название для переменной, которая хранит список
# активных студентов, оставь этот список пустым
students_active = []

# назови переменную, которая хранит текущее количество студентов в потоке
students_count = 101

# придумай две переменных для обозначения самого маленького и самого большого
# числа в диапазоне и запиши в них числа 1 и 45
number_less = 1
number_more = 45

# создай константу для хранения числа Пи и запиши в неё первые 10 знаков
PI = 3.1415926535