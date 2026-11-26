# Exercício 10 - Instrumentação do QuickSort

```Python
comparacoes = 0
copias = 0
 
def quicksort_inst(v):
     
    global comparacoes
    global copias
     
    if len(v) <= 1:
        return v
     
    pivot = v[-1]
     
    menores = []
    maiores = []
     
    for x in v[:-1]:
         
        comparacoes += 1
         
        if x <= pivot:
            menores.append(x)
        else:
            maiores.append(x)
     
    resultado = (
        quicksort_inst(menores)
        + [pivot]
        + quicksort_inst(maiores)
    )
     
    copias += len(resultado)
     
    return resultado
```

## Exemplo

```python
dados = [8,2,9,1,7,4]
 
quicksort_inst(dados)
 
print("Comparações:", comparacoes)
print("Cópias:", copias)
```

## Cenários

| Entrada	| Comparações |
| --------- | ----------- |
| Ordenada	| Alta        |
| Invertida	| Alta        |
| Aleatória	| Menor       |
