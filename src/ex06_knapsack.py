def knapsack(target, weights, index=0):

    if target == 0: return [[]]

    if target < 0 or index >= len(weights):
        return []

    incluir = knapsack(
        target - weights[index],
        weights,
        index + 1
    )

    incluir = [
        [weights[index]] + c
        for c in incluir
    ]

    excluir = knapsack(
        target,
        weights,
        index + 1
    )

    return incluir + excluir