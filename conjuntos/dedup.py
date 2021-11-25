"""
Crie uma função que remove duplicatas de uma lista
>>> lst_fruits = ['banana', 'banana', 'caqui', 'caramelo']
>>> dedup(lst_fruits)
['banana', 'caqui', 'caramelo']
"""


def dedup(lst):
    """

    :param lst:
    :return: lst without duplicated elements

    Linear and space
    """
    result = []
    set_result = set()

    for e in lst:
        if e not in set_result:
            result.append(e)
            set_result.add(e)

    return result
