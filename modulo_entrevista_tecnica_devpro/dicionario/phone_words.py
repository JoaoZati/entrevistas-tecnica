from collections import deque


def phoneword(phonenumber):
    """
    Return all possible phonewords
    :param phonenumber: str
    :return: list, list with strgins of all phonewords

    Complexidade tempo e memoria: O(a**n)
    """

    dict_convert = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz',
    }

    if not isinstance(phonenumber, str):
        raise ValueError('Not a string')

    list_first = ['']
    list_actual = []
    for number in phonenumber:
        for lst in list_first:
            list_actual.extend([lst + letter for letter in dict_convert[str(number)]])
        list_first = list_actual
        list_actual = []

    return list_first


print(phoneword(''))
print(phoneword('2'))
print(phoneword('23'))
print(phoneword('234'))
print(phoneword('736'))
