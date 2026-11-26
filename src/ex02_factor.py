from math import sqrt

def factor(x, lowest=2):

    if x == 0: return ["0 possui infinitos divisores"]
    if x == 1: return [1]
    if x < 0: return [-1] + factor(-x)

    limite = int(sqrt(x))

    for d in range(lowest, limite + 1):
        if x % d == 0:
            return [d] + factor(x // d, d)

    return [x]