""""
Desenvolva uma função chamada max_min que calcula os valores máximo e mínimo de uma lista
Retornando uma Tupla.

Perguntas:
1. E se a lista for vazia?
2. A lista já vem ordenada? (crescente ou decrescente?)
3. Pode usar a função embutida max e min?

>>> max_min_ordered([0,1,2,3,4,5,6])
(6, 0)
>>> max_min_ordered(list(range(100)))
(99, 0)
>>> max_min_ordered([])
Traceback (most recent call last):
 ...
ValueError: Empty List
>>> max_min([1,2,5,2,3,0,2])
(5, 0)
>>> from random import shuffle
>>> random_list = list(range(100))
>>> shuffle(random_list)
>>> max_min(random_list)
(99, 0)
>>> max_min([])
Traceback (most recent call last):
 ...
ValueError: Empty List
>>> max_min_hardcoded([1,2,5,2,3,0,2])
(5, 0)
>>> from random import shuffle
>>> random_list = list(range(100))
>>> shuffle(random_list)
>>> max_min_hardcoded(random_list)
(99, 0)
>>> max_min_hardcoded([])
Traceback (most recent call last):
 ...
ValueError: Empty List
"""


def max_min_ordered(lst):
    """
    Calculate the maximum and minimum values of a list
    :param lst: list
    :return: tuple (max, min)
    """

    if len(lst) == 0:
        raise ValueError('Empty List')

    return lst[-1], lst[0]


def max_min(lst):
    """
    Calculate the maximum and minimum values of a list
    :param lst: list
    :return: tuple (max, min)
    """

    if len(lst) == 0:
        raise ValueError('Empty List')

    return max(lst), min(lst)  # O(n + n) = O(2n) = O(n)


def max_min_hardcoded(lst):
    """
    Calculate the maximum and minimum values of a list
    :param lst: list
    :return: tuple (max, min)
    """

    if len(lst) == 0:
        raise ValueError('Empty List')

    max_value = min_value = lst[0]

    for value in lst:
        if value > max_value:
            max_value = value
        if value < min_value:
            min_value = value

    return max_value, min_value  # O(n) e não O(n+n)
