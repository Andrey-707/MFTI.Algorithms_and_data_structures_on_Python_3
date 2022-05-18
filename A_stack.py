# Используется в лекции №13 как импортируемый модуль

'''
Модуль, описывающий структуру данных - стек
>>> clear()
>>> is_empty()
True
>>> push(1)
>>> push(2)
>>> push(3)
>>> is_empty()
False
>>> pop()
3
>>> pop()
2
>>> pop()
1
>>> is_empty()
True
'''

_stack = [] # символ подчеркивания в названии указывает на то, что это внутренняя переменная

def push(x):
	"""
	Добавляет элемент x в конец стека
	
	>>> size = len(_stack)
	>>> push(5)
	>>> len(_stack) - size
	1
	>>> _stack[-1]
	5
	"""
	_stack.append(x)



def pop():
	'''
	Удаляет элемент из спска, при этом
	возвращает сам элемент
	'''
	x = _stack.pop()
	return x


def clear():
	'''
	Очищает стэк
	'''
	_stack.clear()


def is_empty():
	'''
	Проверяет стек пуст или нет.
	Возвращает логическое значение
	'''
	return len(_stack) == 0 # True/False


# run
if __name__ == "__main__":
	import doctest
	# doctest.testmod(verbose=True) # verbose=True - подробное описание тестирования
	doctest.testmod(verbose=False) # малчаливое тестирование (ни чего не выводит, если в коде не допущена ошибка)
