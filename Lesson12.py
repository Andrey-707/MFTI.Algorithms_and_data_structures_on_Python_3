# Алгоритмы на Python 3. Лекция №№12.
# лектор: Хирьянов Тимофей Фёдорович
'''
Темы, рассмотренные на лекции №12:
- Расстояние Левенштейна
- Проверка равенства строк
- Наивный поиск подстроки в строке
- Алгоритм Кнута-Морриса-Пратта
'''

# Редакционное расстояние между строками (расстояние Левинштейна). O(M*N)
A = "колокол"
B = "молоко"
'''Допустимые типографические ошибки:
1) Перепутали символ
2) Вставили лишний символ
3) Потеряли нужный символ
'''
"колокол"
 123...N # элементы строки
"молоко"
 123..M # элементы строки
'''Fij - минимальное редакционное расстояние между срезами A[:i] и B[:j]
FNM - ответ

Рекурентные случаи:

1) Если последний символ один и тот же
A[:i] = "a1, a2, ..., ai-1, x"
B[:j] = "b1, b2, ..., bi-1, x"
Fij = F(i-1)(j-1), если Ai == Bj

2) Если последние символы отличаюся
A[:i] = "a1, a2, ..., ai-1, x"
B[:j] = "b1, b2, ..., bi-1, y"
Fij = 1 + min(F(i-1)j, Fi(j-1), F(i-1)(j-1))

крайний случай:
F0j = j, F0i = i
F00 = 0
'''
def get_levenshtein_length(A, B):
    '''Редакционное расстояние между строками'''
    F = [[(i+j) if i*j == 0 else 0 for j in range(len(B)+1)]
         for i in range(len(A)+1)]
    for i in range(1, len(A)+1):
        for j in range(1, len(B)+1):
            if A[i-1] == B[j-1]:
                F[i][j] = F[i-1][j-1]
            else:
                F[i][j] = 1 + min(F[i-1][j], F[i][j-1], F[i-1][j-1])
    return F[len(A)][len(B)]


# Тестирование алгоритма Левенштейна
def test_levenshtein_algorithm(algorithm):
    
    # testcase #1 (одна ошибка в слове "Привт")
    print("Тестируем: ", algorithm.__doc__)
    print("testcase #1: ", end="")
    A = "Привет"
    B = "Привт"
    edit = algorithm(A, B)
    print("OK" if edit == 1 else "Fail")
    
    # testcase #2 (две ошибки в слове "молоко")
    print("Тестируем: ", algorithm.__doc__)
    print("testcase #2: ", end="")
    A = "колокол"
    B = "молоко"
    edit = algorithm(A, B)
    print("OK" if edit == 2 else "Fail")

    # testcase #3 (три ошибки в слове "привты")
    print("Тестируем: ", algorithm.__doc__)
    print("testcase #3: ", end="")
    A = "Привет"
    B = "привты"
    edit = algorithm(A, B)
    print("OK" if edit == 3 else "Fail")

    # testcase #4 (семь ошибок в слове "а_л_г_о_р_и_т_м")
    print("Тестируем: ", algorithm.__doc__)
    print("testcase #4: ", end="")
    A = "алгоритм"
    B = "а_л_г_о_р_и_т_м"
    edit = algorithm(A, B)
    print("OK" if edit == 7 else "Fail")


# run test
if __name__ == "__main__":
    test_levenshtein_algorithm(get_levenshtein_length)
'''OUT:
Тестируем:  Редакционное расстояние между строками
testcase #1: OK
Тестируем:  Редакционное расстояние между строками
testcase #2: OK
Тестируем:  Редакционное расстояние между строками
testcase #3: OK
Тестируем:  Редакционное расстояние между строками
testcase #4: OK
'''


# Проверка равенства строк. O(N)
def equal(A, B):
    '''Проверка равенства строк'''
    if len(A) != len(B): # проверка равенства длин строк
        return False
    for i in range(len(A)): # переход к проверке символов строк
        if A[i] != B[i]:
            return False
    return True # A == B
    

# Тестирование алгоритма проверки равенства строк
def test_equal(algorithm):
    
    # testcase #1 (строки НЕ равны)
    print("Тестируем: ", algorithm.__doc__)
    print("testcase #1: ", end="")
    A = "строки"
    B = "равны"
    result = algorithm(A, B)
    print("OK" if result else "Fail")

    # testcase #2 (строки всё ещё НЕ равны)
    print("Тестируем: ", algorithm.__doc__)
    print("testcase #2: ", end="")
    A = "строки"
    B = "Строки"
    result = algorithm(A, B)
    print("OK" if result else "Fail")

    # testcase #3 (теперь строки равны)
    print("Тестируем: ", algorithm.__doc__)
    print("testcase #3: ", end="")
    A = "строки"
    B = "строки"
    result = algorithm(A, B)
    print("OK" if result else "Fail")
    

# run test
if __name__ == "__main__":
    test_equal(equal)
'''OUT:
Тестируем:  Проверка равенства строк
testcase #1: Fail
Тестируем:  Проверка равенства строк
testcase #2: Fail
Тестируем:  Проверка равенства строк
testcase #3: OK
'''


# Поиск подстроки в строке. O(N*M)
s = "abacabadabacabafabacabadabacabadabacabadaba"
#           7               23      31          # индексы, где обнаружена подстрока
sub = "dabac"

# воспользуемся вспомогательным алгоритмом сравнения строк
def equal(s, sub):
    '''Проверка равенства строк'''
    if len(s) != len(sub):
        return False
    for i in range(len(s)):
        if s[i] != sub[i]:
            return False
    return True


def search_substring(s, sub):
    '''Поиск подстроки в строке'''
    for i in range (0, len(s) - len(sub) + 1):
        if equal(s[i:i+len(sub)], sub): # применяется проверка равенства строк
            print(i)


# run
if __name__ == "__main__":
    search_substring(s, sub)
'''OUT:
7
23
31
'''

# Сколько раз подстрока встречается с строке.
# В строке 's' подстрока 'sub' встречается три раза.
s = "abacabadabacabafabacabadabacabadabacabadaba"
#           7               23      31
sub = "dabac"

# воспользуемся вспомогательным алгоритмом сравнения строк
def equal(s, sub):
    '''Проверка равенства строк'''
    if len(s) != len(sub):
        return False
    for i in range(len(s)):
        if s[i] != sub[i]:
            return False
    return True


def count_substring(s, sub):
    '''Количество вхождений подстроки в строку'''
    count = 0
    for i in range (0, len(s) - len(sub) + 1):
        if equal(s[i:i+len(sub)], sub): # если обнаружено равенство строк
            count += 1
    return count


# Результат аналогичен методу строки .count()
if __name__ == "__main__":
    print(count_substring(s, sub))
    print(s.count(sub))
'''OUT:
3
3
'''


# Префикс-фунция пи от строки. O(N)

'''
s = "abacabadabacabafabacabadabacabadabacabadaba"
                                            |   | # суффикс
Например, в стороке 's' суффиксом является 'aba' (на который строка заканчивается)
Собственный суффикс - это суффикс, не равный самой строке.
П_s - длина максимального собственного суффикса, который является префиксом.
т.е. найденный в пи функции префикс будет ОБЯЗАТЕЛЬНО равен суффиксу.
П_si - префикc функция среза стоки s[:i]

П_ = [0 для всех i]
для всех i строки s:
    k = П_[s][i-1]
    пока k > 0 и s[i] != s[k+1]:
        k = П_[s][k]
    если s[i] == s[k+1], то
        k += 1
    П_[i] = k
'''
# Возьмем строку 's'
s = "abacabadabacabafabacabadabacabadabacabadaba"

# Разобьем строку 's' на части, используя суффикс 'aba'
s = "aba c aba d aba c aba f aba c aba d aba c aba d aba c aba d aba"

# Разобьем строку 's' на части по алгоритку 'префикс-функции' (максимальная длина собственного суффикса)
s = "abacabadaba c aba f abacabadaba c aba d abacabadaba "
#    11 символов         11 символов         11 символов

# Алгоритм:
def pi_f(s):
    '''Вычисление префикса строки'''
    if len(s) < 2:
        return 0
    p = [0]*len(s)
    for i in range(1, len(s)):
        k = p[i-1]
        while k > 0 and s[i] != s[k]:
            k = pi_f(s[:k])
        if s[i] == s[k]:
            k += 1
        p[i] = k
    return p[len(s) - 1]


# run
s = "abacabadabacabafabacabadabacabadabacabadaba"
print(pi_f(s)) # OUT: 11

# собственно, вот и префикс строки 's':
print(s[:pi_f(s)]) # OUT: abacabadaba

# более простой пример. Массив префикс-функции будет выглядеть следующим образом: [0, 0, 1, 0, 1]
s = "олово"
print(pi_f(s)) # OUT: 1

# А в этом случае ответ будет ноль. Массив префикс-функции будет выглядеть следующим образом: [0, 0, 0, 0, 0]
s = "Олово"
print(pi_f(s)) # OUT: 0


# реализация алгоритма префикс-функции из Вики (возвращает массив):
def prefix(s):
    '''Вычисление префикса строки'''
    p = [0] * len(s)
    for i in range(1, len(s)):
        k = p[i - 1]
        while k > 0 and s[k] != s[i]:
            k = p[k - 1]
        if s[k] == s[i]:
            k += 1
        p[i] = k
    return p


# подробное решение для предыдущей строки 's' = "abacabadabacabafabacabadabacabadabacabadaba"
# для строки 's' всего три случая

# s = "abacabadabacabafabacabadab acabadabacabadaba" <- стоп на 26 символе
#                      abacabadaba 

# s = "abacabadabacabafabacabadabacabadaba cabadaba" <- стоп на 35 символе
#                              abacabadaba

# s = "abacabadabacabafabacabadabacabadabacabadaba"  <- стоп на 43 символе
#                                      abacabadaba

# run
s = "abacabadabacabafabacabadabacabadabacabadaba"
print(*prefix(s))
# ниже приведены развернутый массив префикс функции для строки 's' и под ним номера букв (НЕ ИНДЕКСЫ)
# 0 0 1 0 1 2 3 0 1 2 3 4 5 6 7 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 8 9 10 11 12 13 14 15 8 9 10 11  <- prefif
# 1 2 3 4 5 6 7 8 910111213141516171819202122232425 26 27 28 29 30 313233 34 35 36 37 38 394041 42 43  <- num of symb
print(len(s)) # OUT: 43


# строка
s = "ababcaba"
'''
префикс      префикс         p
a            a          ->   0
ab           ab         ->   0
aba          aba        ->   1
abab         abab       ->   2
ababc        ababc      ->   0
ababca       ababca     ->   1
ababcab      ababcab    ->   2
ababcaba     ababcaba   ->   3
'''
def prefix(s):
    '''Вычисление префикса строки'''
    p = [0] * len(s)
    for i in range(1, len(s)):
        k = p[i - 1]
        while k > 0 and s[k] != s[i]:
            k = p[k - 1]
        if s[k] == s[i]:
            k += 1
        p[i] = k
    return p

# подробное решение для строки 's' = "ababcaba"
# для строки 's' максимальный случай при значении 'зед-функции' 8

# s = "ababcaba" <- стоп на 8 символе
#           aba

# run
s = "ababcaba"
print(*prefix(s))
# ниже приведены развернутый массив префикс функции для строки 's' и под ним номера букв (НЕ ИНДЕКСЫ)
# 0 0 1 2 0 1 2 3 <- prefif
# 1 2 3 4 5 6 7 8 <- num of symb
print(len(s)) # OUT: 8


# "Z-функция". O(N+M)

# "Z-функция" — это вектор длин наибольшего общего префикса строки с ее суффиксом.
# "Z-функция" от строкиs 'string' и позиции 'x' — это длина максимального префикса подстроки, начинающейся с
# позиции 'x' в строке 'string', который одновременно является и префиксом всей строки 'string'.
# "Z-функция" тесно связана с префикс-функцией, и их область применения в основном совпадает. Для примера
# можно заменить в решении задачи на поиск подстроки в строке префикс-функцию "Z-функцией":

# строка
s = "ababcaba"
'''
суффикс      строка         Z
ababcaba    ababcaba   ->   8
babcaba     ababcaba   ->   0
abcaba      ababcaba   ->   2
bcaba       ababcaba   ->   0
caba        ababcaba   ->   0
aba         ababcaba   ->   3
ba          ababcaba   ->   0
a           ababcaba   ->   1
'''
def z_f(s):
    '''Z функция'''
    arr = []
    if not s: return arr
    i, slen = 1, len(s)
    arr.append(slen)
    while i < slen:
        left, right = 0, i
        while right < slen and s[left] == s[right]:
            left += 1
            right += 1
        arr.append(left)
        i += 1
    return arr


# run
s = "ababcaba"
print(z_f(s)) # OUT: [8, 0, 2, 0, 0, 3, 0, 1]


# подробное решение для строки 's' = "abacabadabacabafabacabadabacabadabacabadaba"
# для строки 's' максимальный случай при значении 'зед-функции' 43

# s = "abacabadabacabafabacabadabacabadabacabadaba"  <- 43 символа префикса с 1 символа
#      abacabadabacabafabacabadabacabadabacabadaba 


# для этой же строки ещё два случая при значении 'зед-функции' 15

# s = "abacabadabacabaf abacabadabacabadabacabadaba"  <- 15 символов префикса с 17 символа
#                       abacabadabacaba

# s = "abacabadabacabafabacabad abacabadabacabadaba"  <- 15 символов префикса с 25 символа
#                               abacabadabacaba


# и ещё один пример для этой же строки при значении 'зед-функции' 11

# s = "abacabadabacabafabacabadabacabad abacabadaba"  <- 11 символов префикса с 33 символа
#                                       abacabadaba

# run
s = "abacabadabacabafabacabadabacabadabacabadaba"
print(*z_f(s))
# ниже приведены развернутый массив префикс функции для строки 's' и под ним номера букв (НЕ ИНДЕКСЫ)
# 43 0 1 0 3 0 1 0 7 0 1 0 3 0 1 0 15 0 1 0 3 0 1 0 15 0 1 0 3 0 1 0 11 0 1 0 3 0 1 0 3 0 1  <- z
# 1  2 3 4 5 6 7 8 910111213141516 1718192021222324 2526272829303132 3334353637383940414243  <- num of symb
print(len(s)) # OUT: 43



# Алгоритм Кнута-Морриса-Пратта (КМП). Время работы алгоритма линейно O(N+M)
# Это эффективный алгоритм, осуществляющий поиск подстроки в строке.

# s = substring + "#" + string

# Даны подстрока 'sub' и строка 's'. Требуется определить индекс, начиная с которого подстрока 'sub'
# содержится в строке 's'. Если 'sub' не содержится в 's' — вернуть индекс, который не может быть
# интерпретирован как позиция в строке (например, отрицательное число).

# КМП функция с использованием pi функции
def find1(substring, string):
    '''КМП функция поиска подстроки в строке'''
    if substring == "":
        return 0
    if string == "":
        return -1
    s = substring + "#" + string
    arr = [0]*len(s)
    for i in range(1, len(s)):
        p = arr[i-1]
        while p > 0 and s[i] != s[p]:
            p = pi_f(s[:p])
        if s[i] == s[p]:
            p += 1
        if p == len(substring):
            return i-2*p
        arr[i] = p
    return -1


# для первого случая find1() воспользуемся алгоритмом pi функции
def pi_f(s):
    '''Вычисление префикса строки'''
    if len(s) < 2:
        return 0
    arr = [0]*len(s)
    for i in range(1, len(s)):
        p = arr[i-1]
        while p > 0 and s[i] != s[p]:
            p = pi_f(s[:p])
        if s[i] == s[p]:
            p += 1
        arr[i] = p
    return arr[len(s) - 1]


# КМП функция с использованием z функции
def find2(substring, string):
    '''КМП функция поиска подстроки в строке'''
    if substring == "":
        return 0
    if string == "":
        return -1
    s = substring + "#" + string
    arr = [0]*len(s)
    for i in range(1, len(s)):
        p = arr[i-1]
        while p > 0 and s[i] != s[p]:
            p = z_f(s[:p])
        if s[i] == s[p]:
            p += 1
        if p == len(substring):
            return i-2*p
        arr[i] = p
    return -1


# для второго случая find2() воспользуемся алгоритмом z функции
def z_f(s):
    '''Z функция'''
    arr = []
    if not s: return arr
    i, slen = 1, len(s)
    arr.append(slen)
    while i < slen:
        left, right = 0, i
        while right < slen and s[left] == s[right]:
            left += 1
            right += 1
        arr.append(left)
        i += 1
    # return arr
    return arr[len(s) - 1]


# строка
s = "abacabadabacabafabacabadabacabadabacabadaba"
#           7               23      31          # индексы, где обнаружена подстрока
# подстрока
sub = "dabac"

# Результат аналогичен методу строки .index()
# для функции КМП, первый момент нахождения подстроки в строке - BINGO !!
if __name__ == "__main__":
    print(find1(sub, s)) # OUT: 7
    print(find2(sub, s)) # OUT: 7
    print(s.index(sub)) # OUT: 7
'''OUT:
7
7
7
'''
