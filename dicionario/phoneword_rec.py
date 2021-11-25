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

    n = len(phonenumber)

    def phoneword_rec(previous_results, cursor):
        if cursor == n:
            return previous_results
        digit = phonenumber[cursor]
        results = []
        for char in dict_convert[digit]:
            results.extend(prev_result + char for prev_result in previous_results)
        return phoneword_rec(results, cursor + 1)

    return phoneword_rec([''], 0)


print(phoneword('234'))