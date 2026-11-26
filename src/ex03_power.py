def power(x, y):

    if y == 0: return 1
    if y == 1: return x
    if y < 0: return 1 / power(x, -y)

    return x * power(x, y - 1)
