def quickselect(v, k):

    pivot = v[-1]

    menores = [x for x in v[:-1] if x <= pivot]
    maiores = [x for x in v[:-1] if x > pivot]

    pos = len(menores)

    if k == pos: return pivot
    if k < pos: return quickselect(menores, k)

    return quickselect(
        maiores,
        k - pos - 1
    )