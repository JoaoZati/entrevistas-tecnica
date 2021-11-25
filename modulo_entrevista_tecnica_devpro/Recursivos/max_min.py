"""
>>> max_min([1,2,3,4,5])
(5, 1)
>>> max_min([1,2,5,2,3,0,2])
(5, 0)
>>> from random import shuffle
>>> random_list = list(range(100))
>>> shuffle(random_list)
>>> max_min(random_list)
(99, 0)
>>> max_min ([])
Traceback (most recent call last):
 ...
ValueError: Empty List
"""


def max_min(lst):
    """
    Calculate the maximum and minimum values of a list
    :param lst: list
    :return: tuple (max, min)
    """

    n = len(lst)
    if n == 0:
        raise ValueError('Empty List')

    max_value = min_value = lst[-1]

    def max_min_rec(cursor):
        """
        t(n) = 1 + t(n-1)
        t(n) = 1 + 1 + t(n-2)
        t(n) = 1 + 1 + 1 + t(n-3)
        t(n) = 1 + 1 + 1 + .... + t(-1)
        t(n) = n + t(-1)

        m(m) = 1 + m(n-1) => O(n)


        :param cursor:
        :return:
        """
        nonlocal max_value, min_value

        if cursor < 0:
            return max_value, min_value
        current = lst[cursor]
        if current > max_value:
            max_value = current
        if current < min_value:
            min_value = current
        return max_min_rec(cursor - 1)

    return max_min_rec(n-1)
