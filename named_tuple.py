"""
Modulo collections - Named Tuple

https://docs.python.org/3/library/collections.html?highlight=collections#collections.namedtuple

Named Tuple -> Sao tupla, diferenciadasm ondem especificamos um nome para a mesma
e tambem parametros.

"""

# Importando

from collections import namedtuple

# precisamos definir o nome e paramentros;

# Forma 1 - declaraçao Named tuple

cao = namedtuple('cao', 'idade raca nome')

# Forma 2

cao = namedtuple('cao', 'idade, raca, nome')

# Forma 3

cao = namedtuple('cao', ['idade', 'raca', 'nome'])

# usando


ray = cao(idade=2, raca='ninguem sabe', nome='zed')

print(ray)

#Forma 1
print(ray[0]) # idade

print(ray[1]) # raca

print(ray[2]) # nome


#Forma 2
print(ray.idade)
print(ray.raca)
print(ray.nome)
