# Exercício 8 - Otimização com Programação Dinâmica

Versão memoizada da mochila.

```python
def knapsack_dp(target, weights, index=0, memo=None):
    if memo is None:
        memo = {}
 
    chave = (target, index)
 
    if chave in memo: return memo[chave]
 
    if target == 0: return [[]]
 
    if target < 0 or index >= len(weights):
        return []
 
    incluir = knapsack_dp(
        target - weights[index],
        weights,
        index + 1,
        memo
    )
 
    incluir = [
        [weights[index]] + c
        for c in incluir
    ]
 
    excluir = knapsack_dp(
        target,
        weights,
        index + 1,
        memo
    )
     
    memo[chave] = incluir + excluir
     
    return memo[chave]
```

## Comparação

| Versão	| Complexidade  |
| --------- | ------------- |
| Recursiva | O(2ⁿ)         |
| Memoizada | O(n × target) |

## Evidência

Estados repetidos passam a ser calculados apenas uma vez.
