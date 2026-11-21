# Exercício 8 - Escolha entre Pilha e Fila

## Problema

Considere um sistema responsável por processar solicitações recebidas de usuários.

O requisito principal estabelece que as solicitações devem ser atendidas estritamente na ordem em que foram recebidas.

O objetivo deste exercício é determinar qual estrutura de dados é mais adequada para implementar esse comportamento e justificar tecnicamente a decisão.

---

## Análise do Cenário

A característica fundamental do sistema é a preservação da ordem cronológica de chegada.

Suponha a seguinte sequência de requisições:

### Ordem de chegada

1. Requisição A
2. Requisição B
3. Requisição C
4. Requisição D

O comportamento esperado do sistema é:

```text
A → B → C → D
```

Ou seja, a primeira requisição recebida deve ser a primeira processada.

Esse requisito elimina imediatamente qualquer estrutura que permita inversão da ordem original.

---

## Avaliação das Alternativas

### Pilha (Stack)

Uma pilha segue o princípio:
- LIFO
- Last In, First Out

O último elemento inserido é o primeiro a ser removido.

#### Exemplo

```text
Push(A)
Push(B)
Push(C)
Push(D)

Pop() → D
Pop() → C
Pop() → B
Pop() → A
```

#### Resultado

```text
D → C → B → A
```

Esse comportamento contradiz diretamente o requisito do sistema.

Portanto, uma pilha não é adequada para este cenário.

### Fila (Queue)

Uma fila segue o princípio:
- FIFO
- First In, First Out

O primeiro elemento inserido é o primeiro removido.

#### Exemplo

```text
Enqueue(A)
Enqueue(B)
Enqueue(C)
Enqueue(D)
 
Dequeue() → A
Dequeue() → B
Dequeue() → C
Dequeue() → D
```

#### Resultado

```text
A → B → C → D
```

O comportamento coincide exatamente com o requisito especificado.

---

## Operações Envolvidas

### Inserção

```python
enqueue(element)
```

Insere um novo elemento no final da fila.

Complexidade:
- O(1)

### Remoção

```python
dequeue()
```

Remove o elemento localizado no início da fila.

Complexidade:
- O(1)

### Consulta do Primeiro Elemento

```python
front()
```

Retorna o próximo elemento a ser processado.

Complexidade:
- O(1)

| Complexidade | Computacional |
| ------------ | ------------  |
| Operação     | Complexidade  |
| Enqueue      | O(1)          |
| Dequeue      | O(1)          |
| Front        | O(1)          |

O custo constante dessas operações torna a fila adequada mesmo para sistemas com grande volume de solicitações.

### Aplicações Reais

O padrão FIFO é amplamente utilizado em:
- Sistemas de impressão.
- Escalonadores de tarefas.
- Processamento de mensagens.
- Filas de atendimento.
- Buffers de rede.
- Sistemas distribuídos.

Em todos esses casos, preservar a ordem de chegada é um requisito funcional importante.

---

## Conclusão

A estrutura mais adequada para o problema é a **Fila (Queue)**.

A justificativa não se limita à sua eficiência computacional. O principal motivo é que seu comportamento FIFO preserva naturalmente a ordem de chegada das solicitações, atendendo integralmente ao requisito do sistema.

Além disso, suas operações fundamentais possuem custo O(1), permitindo escalabilidade e previsibilidade de desempenho mesmo sob alta carga.