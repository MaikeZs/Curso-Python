"""
listas

listas em python fucional como vetores/matrizes (arrays) em outra linguagens. como a diferença de serem
DINAMICO e tambem de podermos colocar QUALQUER tipo de dado.

linguagens c/java: Arrays
    - possuem tamanho e tipo de dado fixo:
    ou seja, nestas linguagens se voce criar um array de tipo int e como tamanho 5, este array
    sera SEMPRE do tipo inteiro e podera ter SEMPRE no 5 valores.
Ja em Python:
- Dinamico: nao possuem tamanho fixo; ou seja, podemos criar a lista e simplesmente ir adicionando
elementos:

- Qualquer tipo de dado: nao possuem tipo de dado fixo; ou seja, podemos colocar qualquer tipo de
doda:

As lista em python são representadas por colchetes: []

#  Podemos facilmente checar se determinado valor esta contido na lista
type([])

lista1 = [1, 33, 44, 22, 43, 55, 11, 52, 96]

lista2 = ['M', 'a', 'i', 'k', 'e']

lista3 = []

lista4 = list(range(11))

lista5 = list('Maike Moura')

if 18 in lista4:
    print('Encontrei o numero 8')
else:
    print('Nao encontrado')

#  Podemos facilmente ordenar  uma lista
lista1.sort()
print(lista1)

#  Podemos facilmente contar o numero  de ocorrencias de um valor em uma lista
print(lista1.count(1))
print(lista5.count('a'))

#  Adicionar elementos em lista


Para adicionar elementos em lista, utilizamos a função append

Obs> com append, nós só conseguimos adicionar 1 elemento por vez
#lista1.append(12, 33, 44) #erro


print(lista1)
lista1.append(98)
print(lista1)

lista1.append([2, 1, 52]) # coloca a lista como elemnto unico (sublista)
print(lista1)

if [2, 1, 52] in lista1:
    print('encntrei a lista')
else:
    print('nao encontrei a lista')

lista1.extend([123, 22, 141] # coloca cada elemento da lista como valor adicional á lista
print(lista1)
#  Podemos inserir um novo elemento no lista informando a posição dp indice
#  isso nao substitui o valor inicial. o mesmo sera deslocado para a direnta da lista
lista1.insert(2, 'novo')
print(lista1)

#  Podemos facimente junta as duas listas

#  lista6 = lista1 + lista2

#  lista1.extend(lista2)
print(lista1)
# Podemos facilmente inverter uma lista

#Forma 1
lista1.reverse()
lista2.reverse()

print(lista1)
print(lista2)

#Forma 2

print(lista1[:: -1])
print(lista2[:: -1])

# copiar uma lista

lista6 = lista2.copy()
print(lista6)

# Podemos contar quantos elementos existem dentro da lista
print(len(lista4))

# Podemos remover facilmente o ultimo elementos de uma lista
# Obs: o pop nao somente remove o ultimo elemento mas tambem o retorna
# obs: se nao houver elementos no indice informado, teremos o erro IndexError.

print(lista5)
lista5.pop()
print(lista5)

# Podemos remover um elemento pelo indice
# Obs: Os elementos a direita deste indice serao deslocados para a esquerda

lista5.pop(2)
print(lista5)

# Podemos remover todos os elementos (zera a lista)
print(lista1)
lista1.clear()
print(lista1)

# Podemos facilmente repetir elementos em uma lista

nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

# Podemos facilmente converte uma string para uma lista

# Exemplo 1

curso = 'Programação em Python'
print(curso)
curso = curso.split()
print(curso)

# Convertendo  uma lista em uma string
lista6 = ['Pragrama', 'em', 'Python']
print(lista6)
# Abaixo estamos falando: pega a lista6,  coloca espaço entre cada elemento e transforma em uma string
curso = ' '.join(lista6)
print(curso)

curso = '$'.join(lista6)
print(curso)

# Podemos realmente  coloca qualquer tipo de dado em uma lista, inclusive misturando esses dados

lista6 = [1, 2.33, True, 'Maike', 'd', 31232212, [2, 3, 5]]
print(lista6)
print(type(lista6))

# Iterando sobre lista

# exemplo 1 - utilizando for

soma =0
for elementos in lista1:
    print(elementos)
    soma = soma + elementos
print(soma)

# exemplo 2 - utilizando while

carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' parar sair:")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)
    # Fazemos acesso aos elementos de forma indexada

#         0         1         2         3
cores = ['azul', 'verde', 'amarelo', 'branco']

print(cores[0])
print(cores[1])
print(cores[2])
print(cores[3])

# Fazer acesso aos elementos de forma indexada inversa
# Para entender melhor o indice negativo, pense na lista como um circulo, onde o final do elemeto
# esta ligado ao inicio da lista


print(cores[-0])
print(cores[-1])
print(cores[-2])
print(cores[-3])

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

    cores = ['azul', 'verde', 'amarelo', 'branco']

# Gerar indice em um for
for indide, cor in enumerate(cores):
    print(indide, cor)

# Lista aceitam valores repetidos
lista = []
lista.append(22)
lista.append(22)
lista.append(44)
lista.append(45)
lista.append(45)
lista.append(44)

print(lista)
# outros metados nao tao importantes mas tambem uteis

# encontrar o indice de uma elemento na lista

numeros = [4, 5, 3, 8, 5, 111, 555]

# Em qual indice esta o valor 6?

print(numeros.index(5)) # Retorna o indice do primeiro elemnto encontrado
print(numeros.index(4))
# Obs: caso nao tem este elemento na lista, sera apresentado erro ValueError
# Podemos fazer busca dentro de um range, ou seja, qual indice começar a buscar
print(numeros.index(8))
print(numeros.index(5, 1)) # buscado a partir do indice 1
print(numeros.index(5, 2)) # buscado a partir do indice 2
print(numeros.index(5, 3)) # buscado a partir do indice 3
#print(numeros.index(5, 4)) # buscado a partir do indice

# Podemos fazer busca dentro de um range, inicio/fim

print(numeros.index(8, 3, 555))

# Revisao de slicing
#Lista[inicio:Fim:Passo]
#Range[inicio:Fim:Passo]
#Trabalhando com slice de lista como  o paramento 'inicio'

lista = [1, 2, 3, 4]
print(lista[1:]) # iniciando no indice 1 e pegando todos os elementos restante

#Trabalhando com slice de lista com o parametro 'fim'

print(lista[:2]) # começa em 0, pega ate o indice 2 -1

print(lista[1:3])

#Trabalhando com slice de lista com o parametro 'passo'

print(lista[1::2])
print(lista[::2])
print(lista[1::-1])

# invertendo valores em uma lista

nomes = ['maike', 'Moura']

nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)

nomes = ['mike', 'moura']
nomes.reverse()
print(nomes)

#Soma, valor maximo*, valor minimo*, tamanho
#* se os valores forem todos inteiros ou reais.

lista = [1, 2, 3, 4, 5, 6]

print(sum(lista)) #soma
print(max(lista)) #maximo valor
print(min(lista)) #minimo valor
print(len(lista)) #Tamanho da lista

# transforma uma lista em tupla
lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

# desempacotamento de lista

lista = [1, 2, 3]

num1, num2, num3, = lista
#OBs: se tivermos um numero diferente de elementos na lista ou variaveis para recever os dados, teremos Valueerro

print(num1)
print(num2)
print(num3)
# copiando uma lista para outra (shallow copy e deep copy)

# Forma 1

lista = [1, 2, 3]
print(lista)

nova = lista.copy()
print(nova)

nova.append(7)
print(lista)
print(nova)
# veja que ao utilizarmos lista.copy() copiamos os dados da lista para uma nova lista, mas elas
# ficaram totalmente independentes, ou seja, modificando uma lista, nao afeta a outra. Isso em Python
# e chamado de deep copy (copia profunda)
"""


# Forma 2
lista = [1, 2, 3]
print(lista)

nova = lista # copia
print(nova)

nova.append(4)

print(nova)
print(lista)

# Veja que utilizamos a copia via atribuiçao e copiamos os dados da lista para a nova lista, mas
# apos realizar modificação em uma das listas, essa modificação se refletiu em ambas as lista.
# Isso em Python e chamado de Shallow Copy.
