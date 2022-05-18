# Алгоритмы на Python 3. Лекция №9.
# лектор: Хирьянов Тимофей Фёдорович
'''
Темы, рассмотренные на лекции №9:
- Быстрая сортировка Тони Хоара (реализация).
- Слияние двух упорядоченных массивов.
- Сортировка слиянием (реализация).
- Устойчивость сортировок.
- Проверка упорядоченности массива за O(N).
'''

# Рекурентные сортировки.
# !!! Сортировка называется устойчивой если она не меняет порядок равных элементов !!!

# Сортировка слиянием. Выполняется на обратном ходу рекурсии. O(N * log N)
# Сортировку слиянием можно оптимизировать по памяти, если улучшить интерфейс функции merge(), либо
# запихнуть её (функцию merge()) внуть функции merge_sort()
def merge_sort(A):
	'''Сортировка слиянием делит массив на две части (рекурсивно до крайноего случая),
	сортирует эти части, обьединяет их в отдельный вспомогательный массив, затем массив,
	полученный в качестве аргумента для сортировки заполняется элементами вспомогательного массива'''
	if len(A) <= 1: # крайний случай
		return # <=> return None
	middle = len(A)//2
	L = [A[i] for i in range(0, middle)]
	R = [A[i] for i in range(middle, len(A))]
	merge_sort(L)
	merge_sort(R)
	C = merge(L, R)
	for i in range(len(A)):
		A[i] = C[i]


# Cлияние отсортированных массивов в один. Выполняется линейно (за один проход). O(N)
def merge(A:list, B:list):
	'''Cлияние отсортированных массивов'''
	C = [0] * (len(A) + len(B))
	i = k = n = 0
	while i < len(A) and k < len (B):
		if A[i] <= B[k]:
			C[n] = A[i]
			i += 1
			n += 1
		else:
			C[n] = B[k]
			k += 1
			n += 1
	while i < len(A):
		C[n] = A[i]
		i += 1
		n += 1
	while k < len(B):
		C[n] = B[k]
		k += 1
		n += 1
	return C


# Сортировка Тони Хоара (быстрая сортировка).
# Сложность алгоритма определяется лишь количеством разделений, то есть глубиной рекурсии.
# ЛУЧШИЙ случай - O(N * log2N); В СРЕДНЕМ - O(N * log N); ХУДШИЙ случай - O(N**2)
# Сортировка выполняется на прямом ходу рекурсии.
def hoar_sort(A):
	'''Сортировка Хоара'''
	if len(A) <= 1: # крайний случай
		return # <=> return None
	barrier = A[0]
	L = []
	M = []
	R = []
	for x in A:
		if x < barrier:
			L.append(x)
		elif x == barrier:
			M.append(x)
		else: # x > barrier
			R.append(x)
	hoar_sort(L)
	hoar_sort(R)
	k = 0
	for x in L + M + R:
		A[k] = x
		k += 1


# Тестирование сортировок 'hoar_sort' и 'merge_sort'
def test_sort(sort_algorithm):
    # testcase #1
    print("Тестируем: ", sort_algorithm.__doc__)
    print("testcase #1: ", end="")
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(A)
    print("OK" if A == A_sorted else "Fail")


# run test
if __name__ == "__main__":
    test_sort(merge_sort)
    test_sort(hoar_sort)


# Проверть отсортирован массив или НЕ отортирован. Однопроходный алгоритм. O(N) или за О(len(A))
def check_sorted(A, ascending=True):
    '''Проверка отсортированности массив'''
    flag = True
    x = int(ascending) # int(True) == 1, int(False) == 0
    # переменная 's' получает значения либо +1 (если int(True)), либо -1 (если int(False))
    s = 2*x - 1
    for i in range(0, len(A)-1):
        if s * A[i] > s * A[i+1]:
            flag = False
            break
    return flag

A = [4, 2, 5, 1, 3] # not sorted
A_sorted = [1, 2, 3, 4, 5] # sorterd

# run
print(check_sorted(A))
print(check_sorted(A_sorted))
'''OUT:
False
True
'''