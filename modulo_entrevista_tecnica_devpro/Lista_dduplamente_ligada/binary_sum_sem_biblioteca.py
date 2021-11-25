"""
Soma de dois numeros não negativos binarios com tamanho aleatório com formato de string
"""
from collections import deque


def less_to_great_siginiicant_digit(n):
    result = []
    s = list(n)
    while s:
        result.append(int(s.pop()))

    return result


def zip_longest(n, n2, fillvalue):
    n = list(n)
    n2 = list(n2)
    small, greater = sorted([n, n2], key=len)
    missing = len(greater) - len(small)
    small.extend([fillvalue]*missing)

    result = []
    for i, d in enumerate(greater):
        result.append((d, small[i]))

    return zip(greater, small)


def binary_sum(n, n2):
    """
    return string with the sum of two stings of positive binary numbers

    :param n: str, positive binary number if aleatory len
    :param n2: str, positive binary number if aleatory len
    :return: str, positive binary number if aleatory len

    O(n)
    """
    n = less_to_great_siginiicant_digit(n)
    n2 = less_to_great_siginiicant_digit(n2)
    last_sum = 0
    result = deque()
    for d, d2 in zip_longest(n, n2, fillvalue=0):
        d_sum = last_sum + d + d2
        last_sum = 0 if d_sum < 2 else 1
        result.appendleft(str(d_sum % 2))
    if last_sum == 1:
        result.appendleft('1')

    return ''.join(result)


print(binary_sum('111110', '1100'))  # 1001010
