# Алгоритмы на Python 3. Лекция №q16.
# лектор: Хирьянов Тимофей Фёдорович


# Индуктивные функции. Однопроходные алгоритмы.
'''
число -> число
	x -> f(x) # или x,y -> f(x,y)

число -> последовательность чисел
1) генерирующие алгоитмы:
- все цифры чила
- разложить на множители
- арифметическая прогрессия
- геометрическая прогрессия
- и т.д.

последовательность чисел -> число
1) неоднопроходные алгоритмы
2) однопроходные алгоритмы. По оперативной памяти O(1)

последовательность чисел -> последовательность чисел
			x1,x2,...,xn -> f(x1),f(x2),...,f(xn)
	  A = [x1,x2,...,xn] -> [f(x) for x in A]

	      x1,x2,x3...,xn -> x2,x3...,xn-1
фильтрация       x for x in A if x >0

'''
# Однопроходные алгоритмы.
'''
f([x1,...,xn]) = fn
f([x1,...,xn,xn+1]) = fn+1
fn+1 = F(fn,x+1)
					ТАБЛИЧКА
Название          | Имя |  [] | x[1] |    F(fn,x)    |
Количество        |  n  |  0  |  1   |     n=n+1     |
Сумма             |  s  |     |  x1  |     s=s+x     |
Произведение      |  p  |     |  x1  |     p=p*x     |
Хотя бы один (any)| bs  |False|c(x1) | bs=bs or c(x) |    
Все (all)         | bp  |True |c(x1) | bp=bp and c(x)|
Максимум          |  m  |  *  |  x1  |  m=max(m,x)   |
Частотный анализ  |  f  |     |      |  f[x] += 1    |
* начальное состояние для максимума и минимума пустой последовательности не определено

Частотный анализ являеся однопроходным алгоритмом,
при этом числа должны быть ограниченного набора.
Часотный анализ используется в сортировке подсчетов.
'''
# Асимптотика алгоритов.
'''
Количество операций = Времени работы
Nопер = ([x1,x2,x3,...,xn])
Nоперmax = O(f(N))
Количество операций max зависит от функции f(N), при этом гарантирует наихудшее
время выполнения операций, домножденное на определенную константу (с точки зрения
асимптотики эта константа не так важна).

Классические асимптотики функций.
O(1) - фиксированное время, не зависящее от количества чисел.
O(log N) - поиск числа среди упорядоченных чисел. Метод деления пополам.
O(N) - однопроходные алгоритмы. Частотный анализ.
O(N+M) - сортировка подсчетом.
O(N*M) - поразрядная сортировка. Диджит-рэдит-сом.
O(N log N) - Сортировка слиянием. Также в реднестатистичеких случаях подходит
сортировка Хоара.
O(N**2) - квадратичные орировки. Сортировка пузырьком, вставками и выбором.Также
подходит сортировка Хоара.
O(N**3) - сортировка "дурака", сортировка на граммах.
O(2**N) - для комбинаторных ситуаций, когда алгоритм сводится к полному перебору.

# Тест простоты Ферма.
Теорема Ферма.
Для любого простого числа p и для любого натурального чиcла a (при этом a не кратно p)
а в степени (p-1) равно единице по модулю p :      a ** (p-1) = 1 mod p
На языке программирования:
y = (a ** (p-1)) % p
y = 1
Пимер теоремы Ферма:
a = 5
p = 3
y = (5 ** (3-1)) % 3
Y = (25 % 3)
y = 1 -> ч.т.д.

Если (a1 ** (p-1) ) % p = 1 , то число a1 вероятно простое
Если (a1 ** (p-1) ) % p != 1 , то число a1 составное
Сущесвуют числа Кармайкла, которые являются составными, при этом условие теоремы Ферма
для них выполняется.

Генерируе два простых числа, проверяем по теореме Ферма дейсвительно ли они простые,
перемножаем их и получаем число n для окрытого ключа РСА (RSA). p1 * p2 = n
На том, что произведение больших простых чисел нельзя разложить на ножители быстро
держится банковская система и система безопасностей WI-FI сетей, открытые/закрытые 
ключи, цифровые подписи, госуслуги. RSA - алгоритм шифрования.
'''