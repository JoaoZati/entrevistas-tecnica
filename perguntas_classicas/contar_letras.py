from collections import Counter


def contar_letras(s: str):
    """
    >>> contar_letras('joao')
    {'j': 1, 'o': 2, 'a': 1}
    >>> contar_letras('João')
    {'j': 1, 'o': 2, 'ã': 1}
    >>> contar_letras('banana')
    {'b': 1, 'a': 3, 'n': 2}

    :param s:
    :return:
    """

    dct = {}
    for letra in s.lower():
        dct[letra] = dct.get(letra, 0) + 1

    return dct


def contar_letras_with_counter(s: str):
    """
    >>> contar_letras_with_counter('joao')
    {'j': 1, 'o': 2, 'a': 1}
    >>> contar_letras_with_counter('João')
    {'j': 1, 'o': 2, 'ã': 1}
    >>> contar_letras_with_counter('banana')
    {'b': 1, 'a': 3, 'n': 2}

    :param s:
    :return:
    """

    return dict(Counter(s.lower()))


def contar_letras(s: str):
    """
    >>> contar_letras('joao')
    {'j': 1, 'o': 2, 'a': 1}
    >>> contar_letras('João')
    {'j': 1, 'o': 2, 'ã': 1}
    >>> contar_letras('banana')
    {'b': 1, 'a': 3, 'n': 2}

    :param s:
    :return:
    """

    dct = {}
    for letra in s.lower():
        try:
            dct[letra] = dct[letra] + 1
        except Exception as e:
            dct[letra] = 1

    return dct
