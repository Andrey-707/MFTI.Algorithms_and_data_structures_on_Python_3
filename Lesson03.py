# Алгоритмы на Python 3. Лекция №3.
# лектор: Хирьянов Тимофей Фёдорович
'''
Темы, рассмотренные на лекции №3:
- Позиционные системы счисления
- Литералы чисел в Python
- Разложение числа на цифры.
- Однопроходные алгоритмы без реализации.
'''

# Системы счисления.
# 1. Унарная система
# ПЛЮС- удобна для сложения
# МИНУС - работа с длинными числами
x = 4 = |||| (четыре палочки)

# Цифра - это символ, который играет свою роль в записи числа (для кодирование числа)
# Число - это термин, используемый для количественной характеристики, сравнения,
# нумерации объектов и их частей.
'''
1234  #  в десятичной (1234) |  в пятеричной (194)
1000  =     1 * 10**3        =     1 * 5**3
 200  =     2 * 10**2        =     2 * 5**2
  30  =     3 * 10**1        =     3 * 5**1
   4  =     4 * 10**0        =     4 * 5**0
'''

'''
Двоичная  |  4-ная  |  8-ная  |  10-ная  |  16-ная  |
0 0 0 0   |    0    |    0    |     0    |     0    |
0 0 0 1   |    1    |    1    |     1    |     1    |
0 0 1 0   |    2    |    2    |     2    |     2    |
0 0 1 1   |    3    |    3    |     3    |     3    |
0 1 0 0   |    10   |    4    |     4    |     4    |
0 1 0 1   |    11   |    5    |     5    |     5    |
0 1 1 0   |    12   |    6    |     6    |     6    |
0 1 1 1   |    13   |    7    |     7    |     7    |
1 0 0 0   |    20   |    10   |     8    |     8    |
1 0 0 1   |    21   |    11   |     9    |     9    |
1 0 1 0   |    22   |    12   |     10   |     A    |
1 0 1 1   |    23   |    13   |     11   |     B    |
1 1 0 0   |    30   |    14   |     12   |     C    |
1 1 0 1   |    31   |    15   |     13   |     D    |
1 1 1 0   |    32   |    16   |     14   |     E    |
1 1 1 1   |    33   |    17   |     15   |     F    |
1 00000   |   100   |    20   |     16   |     J    |
'''

# Перевод числа 73652 в другие системы счисления

# index 43210
#       73652(в 16-ную) = 7 * 10**5 + 3 * 10**4 + 6 * 10**3 + 5 * 10**2 + 2 * 10**1  = 11fb4
#       73652(в 10-ную) = 7 * 10**5 + 3 * 10**4 + 6 * 10**3 + 5 * 10**2 + 2 * 10**1  = 73652
#       73652(в 8-ную)  = 7 * 8**4  + 3 * 8**3  + 6 * 8**2  + 5 * 8**1  + 2 * 8**0   = 30634
#       73652(в 4-ную)  =    (13)   +     (3)   +    (12)   +   (11)    +    (2)     = 101332310
#       73652(в 2-ную)  = (0 1 1 1) + (0 0 1 1) + (0 1 1 0) + (0 1 0 1) + (0 0 1 0)  = 10001111110110100

# Схема Горнера
# Перевести 1234 из 10-ой в 5-ую
'''
1(5)   = 1
12(5)  = 10(5) + 2  =   1 * 5 + 2
123(5) = 120(5) + 3 =  (1 * 5 + 2) * 5 + 3 
1234(в 5-ную)       = ((1 * 5 + 2) * 5 + 3) * 5 + 4 = 
'''

# Число 127 в различных системах счисления и вывод
x = 127
# Двоичная система счисления 0b1111111
print(bin(x), 0b1111111) # OUT: 0b1111111 127

# Восьмеричная система счисления 0o177
print(oct(x), 0o177) # OUT: 0o177 127

# Шeснадцатеричная система счисления 0x7f
print(hex(x), 0x7f) # OUT: 0x7f 127


# Однопроходные алгоритмы
'''                []      переход
Подсчет      | n |  0  |     n += 1     |
Сумма        | s |  0  |     s += x     |
Произведение | p |  1  |     p *= x     |
Максимум     | m |     |  m = max(m, x) |
Поиск числа  | f |False|f = f or (x==x0)| # x0 - искомое число
'''


# Задача: Разложить число х (123 например) в base системе счисления на цифры. Ответ 4 3 2
base = 7
x = int(input())
while x > 0:
	digit = x % base
	print(digit, end = " ")
	x //= base
# Разложим число 123 в 10-ричной системе счиления на цифры. Ответ 3 2 1
base = 10
x = int(input())
while x > 0:
	digit = x % base
	print(digit, end = " ")
	x //= base
