def fizz_buzz(n: int):
    """
    Imprimir Fizz Buzz conforme o numero informado

    >>> fizz_buzz(6)
    1
    fizz
    buzz
    fizz
    5
    fizzbuzz

    :param n: int
    :return:
    """

    for i in range(1, n + 1):
        string = ''
        if i % 2 == 0:
            string += 'fizz'
        if i % 3 == 0:
            string += 'buzz'

        print(string) if string else print(i)
