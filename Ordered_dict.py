"""
MOdulo Collections - Ordered dict

https://docs.python.org/3/library/collections.html?highlight=collections#collections.OrderedDict

# Em um dicionario, a ordem de inseraçao dos elementos nao sao garantindos.
dicionario = {'a': 1, 'b': 2, 'c': 3}

for cheve, valor in dicionario.items():
    print(f'chave={cheve}: valor={valor}')

# fazendo o import

from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3})

for chave, valor in dicionario.items():
    print(f'chave={chave}: valor={valor} ')


"""
# Entendendo a diferena entre Dict e Ordered Dict

# Dicionarios comuns
from collections import OrderedDict

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2) # True -> ja que a ordem dos elementos nao importa para o dicionario

# Ordered Dict

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})

print(odict1 == odict2)

