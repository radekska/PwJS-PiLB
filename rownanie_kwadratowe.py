"""
Napisz skrypt obliczający pierwiastki równania kwadratowego w postaci : y = ax2 + bx + c. Wejściem skryptu są wartości: a, b, c
"""

import math

def calculate_quad_func(a, b, c):
    delta = math.pow(b, 2) - (4 * a * c)
    if delta < 0:
        raise Exception('Brak miejsc zerowych')
    elif delta == 0:
        return -b / 2 * a
    else:
        x1 = (-b - math.sqrt(delta)) / 2 * a
        x2 = (-b + math.sqrt(delta)) / 2 * a
        return x1, x2


if __name__ == '__main__':
    a, b, c = input('Podaj kolejno parametry a, b oraz c: ').split()

    print('Podane paramtery: a={a} b={b} c={c}'.format(a=a, b=b, c=c))
    print('Miejsca zerowe funkcji kwadratowej: {wynik}'.format(wynik=calculate_quad_func(int(a), int(b), int(c))))