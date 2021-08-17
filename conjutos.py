"""
Conjuntos

 - conjuntos em qualquer linguagem de programaçao, estamos fazendo referencia a teoria dos conjuntos
 da matematica.

 - Aqui no Python, os conjuntos sao chamados de Sets.

 Dito isto, da mesma forma que na matematica:

 - Sets (conjuntos) nao possuem valores duplicados;
 - Sets (conjuntos) nao possuem valores ordenados;
 - Elementos nao sao acessados via indice, ou seja, conjuntos nao sao indexados;

 Conjuntos sao bons para se utilizar quando precisamos armazenar elemntos
 mas nao nos importamos como a ordenaçao deles. Quando nao precisamos se preocupar
 com chaves, valores e itens duplicado.

 Os conjuntos (Sets) sao referenciados em Python com chaves {}

A diferença entre Conjuntos (Sets) e Mapas (Dicionarios) em Python:
    - Um dicionario tem Chave/valor;
    - Um conjunto tem apenas valor;

# Definindo um conjunto

# FOrma 1

s = set({1, 2, 3, 4, 5, 6, 7, 2, 3}) # Repare que temos valores repetidos.

print(s)
print(type(s))

# Obs> Ao cria um conjunto, caso seja adicionado um valor ja existente, o mesmo
# sera ignorado sem gerar error e nao fazer parte do conjunto.

# Forma 2 - Mais comum

s = {1, 2, 3, 4, 5, 5}

print(s)
print(type(s))

# Podemos verificar se determinado elemento esta contido no conjunto

if 3 in s:
    print('Tem o 3')
else:
    print('Nao tem o 3')

# Importante lembrar que, alem de nao termos valores duplicad, nao temos ordem

# Lista aceitam valores duplicado.
lista = [99, 2, 34, 24, 12, 1, 44, 5, 2, 34]
print(f'Lsita: {lista}) com {len(lista)} elementos')

# Tupla aceitam valores duplicado.
tupla = (99, 2, 34, 24, 12, 1, 44, 5, 2, 34)
print(f'tupla : {tupla} com {len(tupla)} elementos')

# Conjunto nao aceitam valores duplicado
conjunto = {99, 2, 34, 24, 12, 1, 44, 5, 2, 34}
print(f'conjunto : {conjunto} com {len(conjunto)} elementos')
# Dicionarios nao aceitam chaves duplicadas
dicionario = {}.fromkeys(lista, 'dict')
print(f'Dicionario: {dicionario} com {len(dicionario)} elementos')
# Assim Como todos outo conjunto Python podemos colocar tipos de dados misturados em Sets

s = {1, 'b', True, 34.222, 44}
print(s)
print(type(s))

# podemos iterar em um set normalmente

for valor in s:
    print(valor)


# Usos interessantes com sets

# imagene que fizemos um formulario de cadastro de visitantes em uma feira ou museu e os visitantes
# informam manualmentes a cidade de ondem vieram.


cidades = ['BH', 'Sp', 'CG', 'Cb', 'CG', 'Sp', 'Cb']

print(cidades)
print(len(cidades))


# Agora precisamos saber quantas cidades distinta, ou seja, unicas, temos,

print(len(set(cidades)))

# Copiando um conjunto para outro....

# Forma 1 - Deep copy

s = {1, 2, 3}

print(s)


novo = s.copy()
print(novo)

novo.add(4)
print(novo)
print(s)


"""
