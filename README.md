# Calculadora de Estequiometria

Este é um script simples em Python que calcula as massas estequiométricas de um composto químico a partir dos elementos, suas proporções (x) e a massa total desejada da amostra.

---

## Como utilizar

### 1. Google Colab (recomendado)

A forma mais fácil de usar este código é através do Google Colab, onde você não precisa instalar nada.

- Acesse o site [https://colab.research.google.com](https://colab.research.google.com)
- Copie e cole o código
- Execute célula por célula

### 2. No seu computador (uso local)

Você também pode rodar o código localmente. Para isso, é necessário ter o Python instalado, junto com a biblioteca NumPy.

---

## Entradas esperadas

Ao rodar o código, ele irá solicitar:

1. Quantos elementos fazem parte do composto.
2. Para cada elemento:
   - O símbolo químico (ex: Ti, O, Fe, etc.)
   - O valor de x (proporção estequiométrica).
3. A massa total da amostra (em gramas).

---

## Regras de entrada

- Os símbolos químicos devem estar corretamente formatados:
  - A primeira letra deve ser maiúscula.
  - Se houver uma segunda letra, ela deve ser minúscula.

  Exemplo:
  - Correto: Ti, Fe, O
  - Incorreto: ti, FE, o

- Use ponto (.) ao invés de vírgula para números com casas decimais.

  Exemplo:
  - Correto: 1.5
  - Incorreto: 1,5

---

## Saída

O programa retorna a massa de cada elemento que deve ser usada para atingir a proporção correta na massa total fornecida.

Exemplo de saída:

Massas estequiométricas:
1.0 x Ti: 0.0362875 g
2.0 x Te: 0.1637125 g


---

## Exemplo de uso

Para o composto TiTe2, com massa total de 200 g:

- Símbolos: Ti, Te
- Proporções x: 1, 2
- Massa total: 0.2

Saída esperada:

Massas estequiométricas:
1.0 x Ti: 0.0362875 g
2.0 x Te: 0.1637125 g

