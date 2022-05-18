# Алгоритмы на Python 3. Лекция №6.
# лектор: Хирьянов Тимофей Фёдорович
'''
Темы, рассмотренные на лекции №6:
- Методы append(), pop() и функция len() для списка.
- Списковые включения.
- Мастер-класс по TDD.
- Сортировка вставками.
- Сортировка выбором.
- Сортировка методом пузырька.
- Сортировка подсчётом.
'''

# Добавление элемента в список. Список (состоит из N_max нулей) заполняется числами слева направо.
N_max = int(input("Размер массива: "))
A = [0] * N_max
print(A) # OUT: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

n = 0
for i in range(N_max):
    x = int(input("Число: "))
    A[n] = x
    n += 1 
print(A) # OUT: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Добавление элемента в список. Метод .append(). Список (пустой) заполняется слева направо.
A = []
print(A) # OUT: []

n = int(input("Размер массива: "))
for i in range(n):
    x = int(input("Число: "))
    A.append(x)

print(A) # OUT: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Удаление элементов из массива.
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

N_max = len(A)
n = N_max
for i in range(N_max):
    n -= 1
    x = A[n]
    print(x) # будут выводиться числа с последнего элемента списка "A" по первый

# при этом список не опустошается
print(A) # OUT: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Удаление элементов из массива. Метод .pop(). Список опустошается справа налево.
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

N_max = len(A)

for i in range(N_max):
    x = A.pop()
    print(x) # будут выводиться числа с последнего элемента списка "A" по первый

# при этом список станет пустым
print(A) # OUT: []


# list comprehensions (eng. - понимание списка). Упрощение создания списка.
A = [x**2 for x in range(10)]
print(A) # OUT: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# Эквивалентное решение
A = []
for x in range(10):
    A.append(x**2)
print(A) # OUT: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Задача_1
# Дан список "A". Создать список "B" из четных элементов списка "A".
A = [1, 2, 3, 4, 5, 9, 16, 25, 36, 10, 6, 8]
B = [x**2 for x in A if x % 2 == 0]

print(B) # OUT: [4, 16, 256, 1296, 100, 36, 64]

# Задача_2
# Дан список "A". Создать список "B" из четных элементов списка "A". Если элемент четный и отрицательный,
# то заменить его на ноль.
A = [1, 2, -3, 4, 5, 9, 16, 25, -36, 10, 6, 8]
B = [0 if x < 0 else x**2 for x in A if x % 2 == 0]

print(B) # OUT: [4, 16, 256, 0, 100, 36, 64]


# Сортировка массива.

# Квадратичные сортировки. O(N**2)

def insert_sort(A):
    '''Сортировка списка "А" ВСТАВКАМИ'''
    N = len(A)
    for top in range(1, N):
        k = top
        while k > 0 and A[k-1] > A[k]:
            A[k], A[k-1] = A[k-1], A[k]
            k -= 1


def selection_sort(A):
    '''Сортировка списка "А" методом ВЫБОРА'''
    N = len(A)
    for pos in range(0, N-1):
        for k in range(pos+1, N):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]


def bubble_sort(A):
    '''Сортировка списка "А" методом ПУЗЫРЬКА'''
    N = len(A)
    for bypass in range(1, N):
        for k in range(0, N-bypass):
            if A[k] > A[k+1]:
                A[k], A[k+1] = A[k+1], A[k]


# Тестирование
def test_sort(sort_algorithm):
    # testcase #1
    print("Тестируем: ", sort_algorithm.__doc__)
    print("testcase #1: ", end="")
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(A)
    print("OK" if A == A_sorted else "Fail")

    # testcase #2
    print("Тестируем: ", sort_algorithm.__doc__)
    print("testcase #2: ", end="")
    A = list(range(10,20)) + list(range(0,10))
    A_sorted = list(range(20))
    sort_algorithm(A)
    print("OK" if A == A_sorted else "Fail")

    # testcase #3
    print("Тестируем: ", sort_algorithm.__doc__)
    print("testcase #3: ", end="")
    A = [4, 2, 4, 2, 1]
    A_sorted = [1, 2, 2, 4, 4]
    sort_algorithm(A)
    print("OK" if A == A_sorted else "Fail")


# запуск тестирования
if __name__ == "__main__":
    test_sort(insert_sort)
    test_sort(selection_sort)
    test_sort(bubble_sort)

'''OUT:
Тестируем:  Сортировка списка "А" ВСТАВКАМИ
testcase #1: OK
Тестируем:  Сортировка списка "А" методом ВЫБОРА
testcase #1: OK
Тестируем:  Сортировка списка "А" методом ПУЗЫРЬКА
testcase #1: OK
Тестируем:  Сортировка списка "А" ВСТАВКАМИ
testcase #2: OK
Тестируем:  Сортировка списка "А" методом ВЫБОРА
testcase #2: OK
Тестируем:  Сортировка списка "А" методом ПУЗЫРЬКА
testcase #2: OK
Тестируем:  Сортировка списка "А" ВСТАВКАМИ
testcase #3: OK
Тестируем:  Сортировка списка "А" методом ВЫБОРА
testcase #3: OK
Тестируем:  Сортировка списка "А" методом ПУЗЫРЬКА
testcase #3: OK
'''

# Сортировка подсчетом. count_sort. O(N)
A = [8, 0, 1, 2, 5, 2, 6, 8, 3, 5, 7, 1, 9, 5, 7]
support = [0] * 10 # умножаем на 9 поскольку в массиве 10 различных цифр (от 0 до 9)

for i in A:
    support[i] += 1

# список 'support' будет содержать повторения всех чисел. Четверок - ноль.
print(support) # [1, 2, 2, 1, 0, 3, 1, 2, 2, 1]
# numbers         0  1  2  3  4  5  6  7  8  9

for i in range(10):
    if support[i] > 0:
        # print(i, support[i]) # выводит цифры в столбик
        print((str(i) + " ") * support[i], end="") # выводит цифры в строку


# Реализацция. Сортировка подсчетом. O(N)
def count_sort(A):
    '''Сортировка ПОДСЧЕТОМ'''
    min_value = min(A)
    max_value = max(A)
    support = [0 for i in range(max_value-min_value+1)]
    for element in A:
        support[element-min_value] += 1
    index = 0
    for i in range(len(support)):
        for element in range(support[i]):
            A[index] = i+min_value
            index += 1


# Тест
def test_c_sort(sort_algorithm):
    # testcase #1
    print("Тестируем: ", sort_algorithm.__doc__)
    print("testcase #1: ", end="")
    A = [8, 0, 1, 2, 5, 2, 6, 8, 3, 5, 7, 1, 9, 5, 7]
    A_sorted = [0, 1, 1, 2, 2, 3, 5, 5, 5, 6, 7, 7, 8, 8, 9]
    sort_algorithm(A)
    print("OK" if A == A_sorted else "Fail")


# запуск тестирования
if __name__ == "__main__":
    test_c_sort(count_sort)