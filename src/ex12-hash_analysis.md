# Exercício 12 - Análise de Funções Hash e Distribuição 

## Objetivo 

Avaliar a qualidade de três funções hash aplicadas a uma tabela de tamanho fixo. O objetivo é analisar como cada função distribui as chaves disponíveis e qual o impacto dessa distribuição na ocorrência de colisões. 

--- 

## Conceitos Fundamentais 

Uma tabela hash depende de uma função hash para transformar uma chave em um índice. 

Idealmente, a função hash deve: 
- Distribuir os elementos uniformemente. 
- Minimizar colisões. 
- Utilizar toda a capacidade disponível da tabela.

Quando muitas chaves são mapeadas para a mesma posição, ocorre uma colisão. 

O aumento da quantidade de colisões reduz a eficiência das operações de busca, inserção e remoção. 

--- 

## Configuração do Problema Tabela: 

**M = 10**

### Índices válidos:

```text 
0,1,2,3,4,5,6,7,8,9
```

### Funções analisadas:
- **h₁(k) = k mod 10**
- **h₂(k) = (k × 7) mod 10**
- **h₃(k) = k² mod 10**

---

## Análise da Função h₁

### Definição

**h₁(k) = k mod 10**

### Exemplo

| k | índice |
| - | ------ |
| 0 | 0      |
| 1 | 1      |
| 2 | 2      |
| 3 | 3      |
| 4 | 4      |
| 5 | 5      |
| 6 | 6      |
| 7 | 7      |
| 8 | 8      |
| 9 | 9      |

### Distribuição:

```text
0 1 2 3 4 5 6 7 8 9
```

Todos os buckets são utilizados.

### Avaliação

Para conjuntos de dados razoavelmente distribuídos, essa função apresenta excelente comportamento.

Seu principal problema ocorre quando as chaves possuem padrões específicos.

#### Exemplo:

```text
10,20,30,40,50
```

#### Resultado:

```text
0,0,0,0,0
```

Nesse cenário todas as chaves colidem.

---

## Análise da Função h₂

### Definição

**h₂(k) = (k × 7) mod 10**

### Exemplo

| k | índice |
| - | ------ |
| 0 | 0      |
| 1 | 7      |
| 2 | 4      |
| 3 | 1      |
| 4 | 8      |
| 5 | 5      |
| 6 | 2      |
| 7 | 9      |
| 8 | 6      |
| 9 | 3      |

### Distribuição:

```text
0 7 4 1 8 5 2 9 6 3
```

### Avaliação

O número 7 é coprimo de 10.

Consequentemente, a função percorre todas as posições da tabela antes de repetir padrões.

Isso produz uma distribuição bastante uniforme.

Na prática, h₂ apresenta comportamento semelhante a h₁, porém reduz certos padrões previsíveis de agrupamento.

---

## Análise da Função h₃

### Definição

**h₃(k) = k² mod 10**

### Exemplo

| k | índice |
| - | ------ |
| 0 | 0      |
| 1 | 1      |
| 2 | 4      |
| 3 | 9      |
| 4 | 6      |
| 5 | 5      |
| 6 | 6      |
| 7 | 9      |
| 8 | 4      |
| 9 | 1      |

### Distribuição Observada

```text
0,1,4,9,6,5,6,9,4,1
```

#### Buckets utilizados:

```text
0,1,4,5,6,9
```

#### Buckets nunca utilizados:

```text
1² mod 10 = 1
9² mod 10 = 1
```

### Colisões

Observa-se imediatamente que:

```text
1² mod 10 = 1
9² mod 10 = 1
```

```text
2² mod 10 = 4
8² mod 10 = 4
```

```text
3² mod 10 = 9
7² mod 10 = 9
```

```text
4² mod 10 = 6
6² mod 10 = 6
```

A função gera colisões sistemáticas.
Além disso, vários buckets jamais são utilizados.

---

## Comparação Geral

| Critério                     | h₁    | h₂    | h₃     |
| ---------------------------- | ----- | ----- | ------ |
| **Utiliza todos os buckets** | Sim   | Sim   | Não    | 
| **Distribuição uniforme**    | Boa   | Boa   | Ruim   | 
| **Risco de colisão**         | Médio | Baixo | Alto   | 
| **Escalabilidade**           | Boa   | Boa   | Ruim   | 

---

## Impacto das Colisões

Em uma tabela hash ideal:

| -  | -  |
| - | - |
| **Busca**    | O(1) |
| **Inserção** | O(1) |
| **Remoção**  | O(1) |

À medida que as colisões aumentam:

| -  | -  |
| - | - |
| **Busca**    | O(n) |
| **Inserção** | O(n) |
| **Remoção**  | O(n) |

Portanto, uma função hash mal distribuída compromete diretamente a eficiência da estrutura.

---

## Conclusão

Entre as funções analisadas, **h₂(k) = (k × 7) mod 10** apresenta a melhor distribuição para o conjunto estudado, utilizando todos os buckets da tabela e reduzindo padrões previsíveis de agrupamento.

A função h₁(k) = k mod 10 também apresenta bom desempenho, embora possa sofrer degradação quando as chaves seguem padrões múltiplos do tamanho da tabela.

A função h₃(k) = k² mod 10 apresenta a pior distribuição. Ela gera colisões sistemáticas, não utiliza todos os buckets disponíveis e produz forte concentração de chaves em poucas posições.

Portanto, para esta tabela de tamanho fixo, h₂ é a alternativa mais adequada, enquanto h₃ representa a escolha menos eficiente.
