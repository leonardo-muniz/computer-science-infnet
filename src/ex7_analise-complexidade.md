# Exercício 7 - Análise de Complexidade

## Função escolhida: Knapsack Recursivo

### Chamadas Redundantes

O mesmo estado pode ser calculado diversas vezes:

```python
knapsack(10, index=2)
knapsack(10, index=2)
knapsack(10, index=2)
```

### Crescimento

Cada elemento gera duas escolhas:
- incluir
- excluir

Árvore de decisão:
- 2ⁿ

### Complexidade

```text
Tempo: O(2ⁿ)
Espaço: O(n)
```

A explosão combinatória ocorre porque todas as combinações possíveis precisam ser avaliadas.