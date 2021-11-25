def hanoi(n, orig='A', aux='B', dest='C'):
    """
    Recursive solution to hanoi tower

    t(n) = 1 + 2t(n-1)
    t(n) = 1 + 2(1 + 2t(n-2))
    t(n) = 1 + 2 + 4t(n-2)
    t(n) = 1 + 2 + 4(1+2t(n-3))
    t(n) = 1 + 2 + 4 + 8t(n-3)
    t(n) = 1 + 2 + 4 + 8 + 16 ... 2**n
    t(n) = 2**(n+1) - 1 => 2**n

    m(n) = 1 + m(n-1) => O(n)

    :param n:
    :param orig:
    :param aux:
    :param dest:
    :return:
    """
    if n >= 1:
        hanoi(n - 1, orig, dest, aux)
        print(f'{orig} -> {dest} : {n}')
        hanoi(n - 1, aux, orig, dest)


for i in range(1, 5):
    print(f'########## Hanoi {i}')
    hanoi(i)
