# Алгоритмы на Python 3. Лекция №10.
# лектор: Хирьянов Тимофей Фёдорович
'''
Темы, рассмотренные на лекции №10:
- Вычисление чисел Фибоначчи и проблема перевычислений.
- Одномерное динамическое программирование на примере чисел Фибоначчи.
- Задачи о кузнечике (количество траекторий, траектория наименьшей стоимости).
- Двумерные массивы (списки списков).
- Оператор is.
'''

# Реализация бинарного поиска в массиве.
# Скорость бинарного поиска очень высока, она равна O(log2 N)

# !!! Двоичный (бинарный) поиск работает ТОЛЬКО ЕСЛИ МАССИВ ОТСОРТИРОВАН !!!

'''В массиве [1, 3, 3, 5, 7, 9] ищем 15. Позиция 1 имеет индекс 0, позиция левее 1
имеет индект -1, позиция 9 имеет индекс N-1, а позиция вне (правее 9) имеет индекс,
равный количесву элементов в массиве.'''
#   	[1, 3, 3, 5, 7, 9]
#    -1  0  1  2  3     N-1  N

key = 15

# Поиск левой границы
def left_bound(A, key): # A - ОТСОРТИРОВАННЫЙ массив, key - искомое значение
	'''Поиск левой границы'''
	left = -1
	right = len(A)
	while right - left > 1:
		middle = (left + right) // 2
		if A[middle] < key:
			left = middle
		else:
			right = middle
	return left

# Поиск правой границы
def right_bound(A, key): # A - ОТСОРТИРОВАННЫЙ массив, key - искомое значение
	'''Поиск правой границы'''
	left = -1
	right = len(A)
	while right - left > 1:
		middle = (left + right) // 2
		if A[middle] <= key:
			left = middle
		else:
			right = middle
	return right


# ДИНАМИЧЕСКОЕ ПРОГРАММИРОВАНИЕ.

# Число Фибоначчи (рекурентный алгоритм).
# Асимптотика вычисления числа Фибоначи (рекурсиво) ОЧЕНЬ медленная, она равна O(Fib n)
def fib(n):
	'''Число Фибоначчи'''
	if n <= 1: # крайний случай
		return n
	else:
		return fib(n-1) + fib(n-2)

# Число Фибоначчи от 30
fib(30) # OUT: 832040


# Число Фибоначчи.
# Такой алгоритм работает ОЧЕНЬ быстро. Линейная асимптотика O(N)
def fib(n):
	'''Число Фибоначчи'''
    fib = [0, 1] + [0] * (n-1)
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]

# Число Фибоначчи от 30
print(fib(30)) # OUT: 832040


# Задача. Кузнечик находится на старте (цифра 1). Он может прыгать по траекории только
# вперед двумя способами:
# 1) либо на +1 шаг
# 2) либо на +2 шага
# Вычислить количество способов дорыгать до клетки N (т.е. до конца).

# Решение.
# В клетку N можно попасть двумя способами:
# 1) из клети N-1
# 2) из клетки N-2
# Количество траекторий, ведущих в клеку N равно: K(N) = K(N-2) + K(N-1)
def traj_num(n):
	'''Число таекторий'''
	K = [0, 1] + [0] * (n-1)
	for i in range(2, n+1):
		K[i] = K[i-2] + K[i-1]
	return K[n] # <=> K[i]

# Количество способов дорыгать до клетки 30
# !!! Число таректорий равно числу Фибоначи !!!
print(traj_num(30)) # OUT: 832040


# Добавим дополнительное условие.

# Кузнечик может прыгать по траекории только вперед тремя способами:
# 1) либо на +1 шаг
# 2) либо на +2 шага
# 2) либо на +3 шага
# 4) Кузнечик не может попадать в некоторые клетки.
# Клетки передаются в 'allowed' в виде массива булевых значений [True]*3 + [False, True, True, False, True, True]
# Решение для случая, когда кузнечик прыгает из точки с индексом 1ю
def count_trajectories(n, allowed:list):
    K = [0, 1, int(allowed[2])] + [0]*(n-2) # массив траекторий
    for i in range(3, n+1):
        if allowed[i]:
            K[i] = K[i-1] + K[i-2] + K[i-3]
    # print(K) # кузнечик прыгает из точки с индексом 1, то [0, 1, 1, 0, 2, 3, 0, 5, 8]
    return K[i]   

# run
'''Возможные траектории:
[0 1 1 0 2 3 5]
   x 1   2 3 4    trajectory_№1
   x 1   2   3    trajectory_№2
   x 1     2 3    trajectory_№3
   x     1 2 3    trajectory_№4
   x     1   2    trajectory_№5
'''
print(count_trajectories(6, [True]*3 + [False, True, True, False, True, True])) # OUT: 8

# Другой вариант (старт из точки с индексом 0).
def count_trajectory(n, allowed: list):
    K = [0, 1, int(allowed[2])*2] + [0]*(n-2)
    for i in range(3, n+1):
        if allowed[i-1]:
            K[i] = K[i-1] + K[i-2] + K[i-3]
    # print(K) # кузнечик прыгает из точки с индексом 0, то [0, 1, 2, 3, 0, 5, 8, 0, 13]
    return K[i]

# run
'''Возможные траектории:
[0 1 2 3 0 5 8]
 x 1 2 3   4 5    trajectory_№1
 x 1 2 3     4    trajectory_№2
 x 1 2     3 4    trajectory_№3
 x   1 2   3 4    trajectory_№4
 x   1     2 3    trajectory_№5
 x     1   2 3    trajectory_№6
 x     1     2    trajectory_№7
 x 1   2   3 4    trajectory_№8
'''
print(count_trajectory(6, [True]*3 + [False, True, True, True])) # OUT: 8


# Миниальная стоимость достижения клетки N. Без запрещенных клеток. Прыжки на +1 и +2.
# price[i] - цена за посещение клетки i
# C[i] - суммарная минимальная стоимось достижения клетки i
def count_min_cost1(n, price:list):
    '''Calculate the lowest cost to reach a destination
    Allowed steps: +1 and +2'''
    # float("-inf") обозначает минус бесконечность
    C = [float("-inf"), price[1], price[1] + price[2]] + [0]*(n-2) # крайний случай
    for i in range(3, n+1):
        C[i] = price[i] + min(C[i-1], C[i-2])
    return C[n]

# run
print(count_min_cost1(7, [1]*8)) # OUT: 4

# Тут программа считает не правильно, ведь доступен шаг на +2. И ответ 5 будет неправильным.
'''
[0 1 2 3 4 5 6 7]    # points
 1 2 1 1 1 1 1 1     # cost
 x   1   2   3 4     # min cost
'''
print(count_min_cost1(7, [1, 2] + [1]*6)) # OUT: 5

# Исправлена ошибка при создании 'C'
def count_min_cost2(n, price:list):
    C = [float("-inf"), price[1], price[2]] + [0]*(n-2) # крайний случай
    for i in range(3, n+1):
        C[i] = price[i] + min(C[i-1], C[i-2])
    return C[n]

# run
print(count_min_cost2(7, [1]*8)) # OUT: 4

# Теперь программа учитывает, что можно со старта сделать шаг +2.
'''
[0 1 2 3 4 5 6 7]    # points
 1 2 1 1 1 1 1 1     # cost
 x   1   2   3 4     # min cost
'''
print(count_min_cost2(7, [1, 2] + [1]*6)) # OUT: 4


# ДВУМЕРНЫЕ МАССИВЫ.

# Создание двумерного массива.
# 1) Линеаризация двумерного массива.
# В массиве N строк и M элементов в строке (столбцов). Элемент A[i][j] хранится в позиции A[i*M + j]
# 2) Создание списка списков (матрица, заполненная нулями)
A = [[0]*M for i in range(N)]