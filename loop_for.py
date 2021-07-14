"""
Loop for

Loop> Estrutura de repetiçao.
For> E uma dessas estrutura.

Utilizamos loops para iterar sobre sequecias ou sobre iteraveis

exemplos de iteraveis:
- String
     nome = "Maike Moura"
- Lista
     lista = [1, 3, 5, 7, 9]
- Range
    numeros = range(1, 10)

# Exemplo de for 1 (Iterando em uma String)
for letras in nome:
    print(letras)

# Exemplo de for 2 (Iterando sobre um lista)
for numeros in lista:
    print(numeros)

# Exemplo de for 3 (Iterando sobre um range)
# range(valor_inicial, valor_final)
# OBS: O Valor final nao e inclusive.

for numeros in range(1, 10):
    print(numeros)

Enumerate:
((0, 'M',), (1, 'a') ....)

for undice, letra in enumerate(nome):
    print(nome(indic))

for undice, letra in enumerate(nome):
    print(nome(letra))

for valor in enumerate(nome):
    print(valor)

nome = 'Maike Moura'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) #Temos que transformar em uma lista


qtd = int(input('Quantas vezes que rode o loop ? '))

soma = 0
for n in range(1, qtd+1):
    num = int(input(f' informe o {n}/{qtd} valor :'))
    soma = soma + num
print(f'A soma é {soma}')

nome = 'Maike'

for letras in nome:
    print(letras, end='')
"""

# Orin:U+1F496

emoje = 'U0001F496'

for _ in range(3):

    for num in range(1, 11):
        print('\U0001F496' * num)
