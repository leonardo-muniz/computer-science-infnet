# Exercício 9 - Implementação do QuickSort

```python
def quicksort(v):
 
if len(v) <= 1: return v
 
pivot = v[-1]
 
menores = [x for x in v[:-1] if x <= pivot]
maiores = [x for x in v[:-1] if x > pivot]

return quicksort(menores) + [pivot] + quicksort(maiores)
```

## Testes

```python
print(quicksort([1,2,3,4,5]))
print(quicksort([5,4,3,2,1]))
print(quicksort([8,2,9,1,7,4]))
```

## Análise

Array ordenado:

```text
Pior caso: O(n²)
```

Array invertido:

```text
Pior caso: O(n²)
```

Array aleatório:

```text
Caso médio: O(n log n)
```