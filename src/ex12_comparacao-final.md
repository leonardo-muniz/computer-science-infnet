# Exercício 12 - Comparação entre QuickSort e QuickSelect

## Teste

```python
dados = [8,2,9,1,7,4,6,3,5]
```

Objetivo:
- Encontrar a mediana

### QuickSort

Executa ordenação completa:

```python
ordenado = quicksort(dados)
mediana = ordenado[len(dados)//2]
```

Complexidade média:
- O(n log n)

### QuickSelect

Executa somente as partições necessárias.

Complexidade média:
- O(n)

## Comparação

| Critério           | QuickSort          | QuickSelect |
| ------------------ | ------------------ | ----------- |
| Ordena todo vetor  | Sim                | Não         |
| Mediana            | Sim                | Sim         |
| Complexidade média | O(n log n)         | O(n)        |
| Trabalho realizado | Maior              | Menor       |
| Melhor uso         | Ordenação completa | Seleção     |

## Conclusão Técnica

Quando se deseja obter apenas um elemento específico (mediana, percentil, k-ésimo menor ou maior elemento), o **QuickSelect** é **mais eficiente** porque evita ordenar partes do vetor que não influenciam o resultado. Já o **QuickSort** continua sendo a melhor escolha quando o objetivo final é **obter todos os elementos ordenados**.
