# Алгоритмы на Python 3. Лекция №8.
# лектор: Хирьянов Тимофей Фёдорович
'''
Темы, рассмотренные на лекции №8:
- Генерация комбинаторных объектов.
- Рекурсивная генерация всех чисел длины M.
- Генерация всех перестановок (рекурсивная).
- Быстрые сортировки: Тони Хоара и слиянием (без реализации).
'''

# Генерация всех перестановок (рекурсивная).
# Реализуем.
def generate_number(N:int, M:int, prefix=None): # N - основание системы счисления, M - кол-во чисел
	prefix = prefix or []
	print(prefix)

# Получаем пустой список []
generate_number(4, 3)

# Подолжаем
def generate_number(N:int, M:int, prefix=None): # N - основание системы счисления, M - кол-во чисел
	'''Функция генерирует все числа (с лидирующими незнчащими нулями)
	в N-ричной системе счисления (N <= 10) длины M'''
	prefix = prefix or []
	if M == 0: # крайний случай
		print(prefix)
		return
	for digit in range(N):
		prefix.append(digit)
		generate_number(N, M-1, prefix)
		prefix.pop()

# Получаем генерацию списков от [0, 0, 0] до [3, 3, 3]
generate_number(4, 3)


# Генерация всех перестановок упрощенный вариант.
# Подходит ТОЛЬКО для двоичной сисемы счисления.
def gen_bin(M, prefix=""): # M - кол-во чисел
	if M == 0: # крайний случай
		print(prefix)
		return
	# gen_bin(M-1, prefix + "0")
	# gen_bin(M-1, prefix + "1")
	# предыдущие два вызова функции можно записать в цикла
	for digit in "0", "1":
		gen_bin(M-1, prefix + digit)
# Получаем все двоичные числа от 00000 до 11111
gen_bin(5)


# Генерация ВСЕХ перестановок чисел.
def generate_permutations(N:int, M:int=-1, prefix=None): # N - кол-во чисел, M - кол-во позиций
    '''Генерирация всех перестановки N чисел в M позициях,
    начиная с префикса prefix'''
    M = N if M == -1 else M # по умолчанию N чисел в M позициях
    prefix = prefix or []
    if M == 0: # крайний случай
        print(prefix)
        return
    for number in range(1, N+1):
        if find_number(number, prefix):
            continue
        prefix.append(number)
        generate_permutations(N, M-1, prefix)
        prefix.pop()

# поиск числа в массиве
def find_number(number, A):
    '''Поиск "number" в массиве "A". Возвращает True, если "number" есть,
    иначе False'''
    for x in A:
        if number == x:
            return True
    return False

# тот же вариант с флагом
def find_number(number, A):
    '''Поиск "number" в массиве "A". Возвращает True, если "number" есть,
    иначе False'''
    flag = False
    for x in A:
        if number == x:
            flag = True
            break
    return flag

# run
generate_permutations(3)
'''OUT:
[1, 2, 3]
[1, 3, 2]
[2, 1, 3]
[2, 3, 1]
[3, 1, 2]
[3, 2, 1]
'''

# Генерация ВСЕХ перестановок чисел (с разворачиванием списков *list).
def generate_permutations_r(N:int, M:int=-1, prefix=None): # N - кол-во чисел, M - кол-во позиций
    '''Генерирация всех перестановки N чисел в M позициях,
    начиная с префикса prefix'''
    M = N if M == -1 else M # по умолчанию N чисел в M позициях
    prefix = prefix or []
    if M == 0: # крайний случай
        # списки можно развернуть вручную, если задать для длины ТРИ (N = 3):
        # refix[0], prefix[1], prefix[2]
        # print(prefix[0], prefix[1], prefix[2])
        # либо с помощью сивола звездочка *
        print(*prefix)
        return
    for number in range(1, N+1):
        if find_number(number, prefix):
            continue
        prefix.append(number)
        generate_permutations_r(N, M-1, prefix)
        prefix.pop()

# run
generate_permutations_r(3)
'''OUT:
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
'''