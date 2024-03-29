# Алгоритмы на Python 3. Лекция №4.
# лектор: Хирьянов Тимофей Фёдорович
'''
Темы, рассмотренные на лекции №4:
- Описание простых функций с параметрами.
- Декомпозиция задачи.
- Структурное программирование. Проектирование «сверху-вниз».
- Стек вызовов.
- Полиморфизм в Python. Duck typing.
- Значения параметров по умолчанию.
- Именованные параметры функций
- Мастер-класс по структурному программированию на проекторе
- Метод грубой силы.
- Тест простоты числа.
- Разложение числа на множители.
'''

# Функции
# элементарная функция
def hello():
    print("Hello, World!")

# вызов функции. В стандартных случаях мы испльзуем !!! СИНХРОННЫЙ ВЫЗОВ ФУНКЦИЙ !!!
# ЭТО ОЗНАЧАЕТ, ЧТО ОСНОВНАЯ ПРОГРАММА ОСТОНАВЛИВАЕТСЯ ПОКА ВЫЗЫВАЕТСЯ ФУНКЦИЯ И ПРОДОЛЖАЕТ РАБОТАТЬ,
# ПОСЛЕ ТОГО, КАК СРАБОТАЛ ВЫЗОВ ФУНКЦИИ (return).
hello() # OUT: Hello, World!

# вызов функции методом присваивания
f = hello
f() # OUT: Hello, World!

# функция с параметрами
def hello(name): # parametr (ФАКТИЧЕСКИЙ ПАРАМЕТР)
    print(f"Hello, {name}!")

# вызов функции с передачей аргумента функции
hello("Andrey") # OUT: Hello, Andrey!

# без передачи аргумента функция вызывает исключение
# hello() # OUT: TypeError: hello() missing 1 required positional argument: 'name'

# функция с параметрами по умолчанию
def hello(name="Name"): # parametr (ИМЕНОВАННЫЙ ПАРАМЕТР)
    print(f"Hello, {name}!")

# вызов функции с передачей аргумента функции
hello("Andrey") # OUT: Hello, Andrey!

# без передачи аргумента функция уже НЕ вызывает исключение
hello() # OUT: Hello, Name!


# return (возврат)
# предыдущие функции ни чего не возвращали, напишем функцию с возвратом значения
def max2(x, y):
    '''Функция возвращает большее из двух'''
    if x > y:
        return x
    else:
        return y

max_of_two = max2(3, 5)
print(max_of_two) # OUT: 5

# предыдущую функцию можно создавать без else
def max2(x, y):
    '''Функция возвращает большее из двух'''
    if x > y:
        return x
    return y

max_of_two = max2(3, 5)
print(max_of_two) # OUT: 5

# Вызов функции внутри функции. Функция с тремя параметрами
# Функции max2 и max3 используют утиный полиморфизм (утиную типизацию данных) и подходят для
# сравнения любого нечто.
def max3(x, y, z): # <<Duck typing>>
    '''Функция возвращает большее из трех'''
    return max2(x, max2(y, z))

max_of_three = max3(3, 5, 22)
print(max_of_three) # OUT: 22

# Работает со строками (лексикографический порядок сравнения)
max_of_three = max3("test", "tesa", "tesq") # слово 'test' имеет больший вес
print(max_of_three) # OUT: test

# separator
def hello_separated(name="Name", separator="-"): # символ разделитель передается в параметр функции
    '''Функция использует в тексте символ разделитель'''
    print("Hello", name + "!", sep=separator)

# вызов функции с передачей имени
hello_separated("Andrey") # OUT: Hello-Andrey!

# вызов функции с передачей имени и символа разделителя
hello_separated("Andrey", "_=_") # OUT: Hello_=_Andrey!

# вызов функции с ЯВНОЙ ссылкой на параметры
hello_separated(separator="***", name="Andrey") # OUT: Hello***Andrey!


# Структурное программирование.
# Проектирование "сверху вниз".

# ШАГ_1. Макет
import graphics as gr

def build_house():
    '''Функция, которая рисует дом'''
    pass

window = gr.GraphWin("Build house", 300, 300)
build_house()

print("Дом нарисован!")

input()

# ШАГ_2. Параметры
import graphics as gr

# передаем в параметры 
# window - где нарисовать дом (на каком холсте) 
# upper_left_corner - в какой точке холста нарисовать дом (координаты)
# width - гараритные размеры дома (ширина)

def build_house(window, upper_left_corner, width):
    '''Функция, которая рисует дом'''
    pass

window = gr.GraphWin("Build house", 300, 300)
build_house(window, gr.Point(100, 100), 100)

print("Дом нарисован!")

input()

# ШАГ_3. Работа в теле функции (там, где было pass)
# В теле функции используем функцию calculate_height(), которой ещё не существует. Чтобы программа
# не валилась, прописываем её ниже как функцию-заглушку (в теле функции просто 'pass').
import graphics as gr

# передаем в параметры 
# window - где нарисовать дом (на каком холсте) 
# upper_left_corner - в какой точке холста нарисовать дом (координаты)
# width - гараритные размеры дома (ширина)


def build_house(window, upper_left_corner, width):
    '''Функция, которая рисует дом'''
    height = calculate_height(width)


def calculate_height(width):
    '''Функция рассчитывает высоту строения по его ширине'''
    pass


window = gr.GraphWin("Build house", 300, 300)
build_house(window, gr.Point(100, 100), 100)

print("Дом нарисован!")

input()

# Приведенное выше называется <<ИТЕРАТИВНАЯ РАЗРАБОТКА>>.
# Программа должна оставаться рабочей в каждый момент времени, т.е. по завершении каждого
# шага программа не должна рушиться. Можно поставить заглушки, а дальше расширять функционал.


# Метод грубой силы (Brute_Force).
def is_simple_num(x):
    '''Функция определяет является ли число простым.
    "x" - целое положительное число.
    Если простое, то возвращает True, а иначе - False'''
    devisor = 2
    while devisor < x:
        if x % devisor == 0:
            return False
        devisor += 1
    return True

# Вывод на экран документ проки функции
# для отображения кирилицы нужно натроить кодировку (прописать chcp 1251)
'''
chcp +
1251 - Windows-кодировка. (Кириллица);
866 - DOS-кодировка;
65001 - Кодировка UTF-8;
'''
help(is_simple_num)
# число 19 является простым
print(is_simple_num(19)) # OUT: True


# Алгоритм факторизации. Разложение числа на множители.
def factirize_num(x):
    '''Функция раскладывает число на множители.
    Печатает их на экран.
    "x" - целое положительное число.'''
    devisor = 2
    while x > 1:
        if x % devisor == 0:
            print(devisor)
            x //= devisor
        else:
            devisor += 1

# Вывод на экран документ проки функции
help(factirize_num)
# получаем десять двоечек в столбик
factirize_num(1024)
# получаем три троечки и чило 37 в столбик
factirize_num(999)
