"""
Tuplas (tuple)

tuplas são  bastantes parecidas com listas.

Existem basicamente duas diferencias basicas:

1 - as  tuplas  são representadas por parenteses ()

2 -as tuplas sao imutaveis: isso significa que ao ser criar uma tupla ela nao muda.
toda operação em um tupla gera uma nova tupla.

#  Cuidado 1: as tuplas sao representadas por (), mas veja:

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)

print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)

print(type(tupla2))

#  Cuidado 2: Tuplas com 1 elemento

tupla3 = (4) # isso nao e uma tupla

print(tupla3)

print(type(tupla3))

#  CONVLUSÃO: Podemos concluir que tuplas sao definidas pela virgula e nao pelo uso do parenteses

(4) -> Nao e tupla
(4,) -> e tupla
4, -> e tupla

# Podemos gerar uma tupla dinamicamente com range(inicio, fim, passo)
tupla  = tuple(range(11))
print(tupla)

print(type(tupla))

# Desempacotamento de tupla

tupla = ('maike', 'moura')

nome, sobrenome = tupla

print(nome)
print(sobrenome)

# Obs> gera erro (ValueErro) se colocarmos um numero diferente de elementos para desempacotar.

# Metodos para adição e remoção de elementos nas tuplas nao existem, dados o fatos das tuplas serem imutaveis.

# Soma*, valor maximo*, valor minim*, e tamanho
# * se os valores forem todos inteiros ou reais

tupla = (1, 2, 3, 4, 5, 6)

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Concatenação de tuplas

tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2) # tupla sao imutaveis

print(tupla1)
print(tupla2)

tupla1 = tupla1 + tupla2 # Tuplas sao imutaveis, mas podemos sobrescrever seus valores
print(tupla1)

# veficar se determinado elemento esta contido na tupla

tupla = (1, 2, 3)

print(3 in tupla)

# O acesso a elementos de uma tupla tambem e semelhante a de uma lista

print(meses[5])

# Iterar com while

i = 0

while i < len(meses):
    print(meses[i])
    i = i + 1
# verificamos em qual indice um elemento esta na tupla

print(meses.index('Abril'))

# Obv> Caso o elemento nao exista, sera gerado erro.

#  dicas na utilização de tuplas

#  devemos utilizar tuplas sempre que nao precisamos modificar os dados contidos em uma coleção

# Exmplo 1

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', ' Maio', 'Junho', 'julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

# slicing

# tulpa(inicio:fim:passo)

print(meses[5:6])


"""


