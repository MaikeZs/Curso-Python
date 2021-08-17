"""
Modulo Collections - Default dict

https://docs.python.org/3/library/collections.html?highlight=collections#collections.defaultdict

Default dict -> ao criar um dicionario utilizando-o, nós informando um valor default,
podendo utilizar um lambda para isso. Este valor sera utilizado sempre que nao houver
um valor definido. Caso tentamos acessr uma chave que nao existem essa chave sera criada
e o valor default sera atribuido.


"""

# Fazendo Import

from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curos'] = 'Programaçao de Python: do 0'

print(dicionario)

print(dicionario['outro'])

print(dicionario)