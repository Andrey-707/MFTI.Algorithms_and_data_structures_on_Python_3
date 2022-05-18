# Проверка корректности скобочной последовательности. Используется в лекции №13.
import A_stack


def is_braces_sequence_correct(s: str):
    '''
    Проверяет корректность скобочной последовательности
    из круглых и кадратных [] скобок ()
    >>> is_braces_sequence_correct("(([()]))[]")
    True
    >>> is_braces_sequence_correct("([)]")
    False
    >>> is_braces_sequence_correct("(")
    False
    >>> is_braces_sequence_correct("]")
    False
    '''
    for brace in s:
        if brace not in "()[]": # является ли скобкой
            continue
        if brace in "([":
            A_stack.push(brace)
        else:
            assert brace in ")]", "Ожидалась закрывающая скобка: " + str(brace)
            if A_stack.is_empty():
                return False
            left = A_stack.pop()
            assert left in "([", "Ожидалась открывающая скобка: " + str(brace)
            if left == "(":
                right = ")"
            elif left == "[":
                right = "]"
            if right != brace:
                return False

    # часть кода:

    # if A_stack.is_empty():
    #     return True
    # else:
    #     False
    
    # можно сократить и записать в одну строчку:

    return A_stack.is_empty()


# run
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True) # verbose=True - подробное описание тестирования
    # doctest.testmod(verbose=False) # малчаливое тестирование (ни чего не выводит, если в коде не допущена ошибка)
