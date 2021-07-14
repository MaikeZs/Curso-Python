"""
Ranges

- Precisamos conhecer o loop for para usar os ranges.
- Precisamas conhecer o range para trabalhar melhor com loops for.

Ranges sao utilizados para gerar sequecias numericas, nao de forma aleatoria
mas sim de maneira especificada.

Fromas gerais:

# Forma 01

range(valor_de_parada)
OBs: Valor-de_parada nao incluive(inicio padrao 0, e passo de 1 em 1)

# Forma 01

for num in range(11):
    print(num)

# Forma 02
for num in range(1,11):
    print(num)

range(valor_de_inicio, valor_de_parada)

OBs; valor de parada nao inclusive(inicio especificado pelo usuario, e passo de 1 em 1)

# Forma 03

for num in range(1, 10, 2):
    print(num)

Range(valor de inicio, valor de parada, passo)

OBs; valor de parada nao inclusive(inicio especificado pelo usuario,
e passo espeficicado pelo usuario)

# Forma 04(inversa)

for num in range(10, 0, -1):
    print(num)

Range(valor de inicio, valor de parada, passo)

OBs; valor de parada nao inclusive(inicio especificado pelo usuario,
e passo espeficicado pelo usuario)
"""

for num in range(10, 0, -1):
    print(num)
