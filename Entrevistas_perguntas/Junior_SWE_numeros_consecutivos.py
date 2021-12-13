"""
Crie uma função que receba um número qualquer e encontre o maior número formado
por digitos consecutivos naquele número

>>> find_two_bigger(53590)
90
>>> find_two_bigger(674030098567819)
5678
>>> find_two_bigger(9012364509789)
90123
"""


def find_two_bigger(num: int):
    resp = ''
    bigger_resp = '0'
    for i, number in enumerate(str(num)):
        if resp == '':
            resp += str(number)
            if int(resp) >= int(bigger_resp):
                bigger_resp = resp
            continue

        last_caracter = int(resp[-1])

        if int(number) == last_caracter + 1 or int(number) == 0 and last_caracter == 9:
            resp += str(number)
        elif len(resp) == 1 and int(number) >= last_caracter:
            resp = number
        else:
            resp = ''

        try:
            if int(resp) >= int(bigger_resp):
                bigger_resp = resp
        except ValueError:
            pass

    return int(bigger_resp)


if __name__ == '__main__':
    numero = int(input('Entrada: '))
    resposta = find_two_bigger(numero)
    print(f'Saída: {resposta}')
