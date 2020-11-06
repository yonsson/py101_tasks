"""Задания по ветвлениям, итерациям и вводу данных."""

# напиши функцию, которая принимает на вход любое
# количество чисел и сообщает, есть ли среди них чётное
def check_even(entered_numbers):
    is_even = False
    for number in entered_numbers:
        if number % 2 == 0:
            is_even = True
            break
    if is_even:
        print('Чётное число есть!')
    else:
        print('Чётных чисел нет!')
check_even([1, 2, 3, 5, 4])


# используй тернарный оператор, чтобы вызвать функцию
# если возраст больше 21 года, в противном случае верни
# сообщение "Мы не продаём алкоголь несовершеннолетним."
def sell_alcohol():
    pass
age = 16
sell_alcohol() if age > 21 else print('Мы не продаём алкоголь несовершеннолетним!')


# напиши функцию, которая проверит, является ли строка ключевым словом в Питоне
# тебе понадобится модуль keyword, импортируй его и изучи с помощью dir()
def is_keyword(word):
    import keyword
    if keyword.iskeyword(word):
        print('Слово является ключевым в Питоне.')
    else:
        print('Слово не ключевое в Питоне.')
is_keyword('False')


# напиши функцию, которая возвращает тип данных на русском языке:
# число, строка, булевый, None, список, кортеж, множество, словарь
# пример: get_type("что-то") возвращает "Это строка."
# пример2: get_type(42) возвращает "Это словарь."
def type_russian(entered):
    type_dict = {
        "int":"целое число",
        "float":"число с плавающей точкой",
        "str":"строка",
        "bool":"число с плавающей точкой",
        "NoneType":"ничто",
        "list":"список",
        "tuple":"кортеж",
        "set":"множество",
        "dict":"словарь",
    }
     print("Это " + type_dict[type(entered).__name__])
    
type_russian(123)
type_russian("Строка")
type_russian(["клещ", "паук", "жук"])
type_russian(("клещ", "паук", 1))
type_russian({"абыр": "рыба"})
type_russian(None)
type_russian(False)
