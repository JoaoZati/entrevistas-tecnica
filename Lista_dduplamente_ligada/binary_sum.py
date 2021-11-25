"""
Soma de dois numeros não negativos binarios com tamanho aleatório com formato de string
"""


def binary_sum(n, n2):
    """
    return string with the sum of two stings of positive binary numbers

    :param n: str, positive binary number if aleatory len
    :param n2: str, positive binary number if aleatory len
    :return: str, positive binary number if aleatory len
    """
    n = int(n, base=2)
    n2 = int(n2, base=2)

    return format(n + n2, 'b')


print(binary_sum('111110', '1100'))  # 1001010
