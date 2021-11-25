from collections import deque


def phoneword(phonenumber):
    """
    Return all possible phonewords
    :param phonenumber: str
    :return: list, list with strgins of all phonewords
    """

    dict_convert = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz',
    }

    n = len(phonenumber)
    if n == 0 or not isinstance(phonenumber, str):
        raise ValueError('Not a string or empty string')

    list_first = [[letter] for letter in dict_convert[phonenumber[0]]]
    list_actual = []

    for number in phonenumber[1:]:
        for lst in list_first:
            for letter in dict_convert[str(number)]:
                list_append = lst + [letter]
                list_actual.append(list_append)

        list_first = list_actual
        list_actual = []

    return list_first


print(phoneword('23'))
