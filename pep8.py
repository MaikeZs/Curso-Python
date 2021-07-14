"""
PEP8 - Python Enhancement Proposal

São Propostas de melhorias para linguagem Python

The Zen Of Python

import this

A ideia de PEP8 e que possamos escrever códigos python de forma pythônica.

[1] - Utilize Camel case para nomes de classes;
class Calculadora:
    pass


[2] - Utilize nomes em minusculo, separados por underline para funções ou variaveis;

def soma():
    pass


def soma_dois():
    pass


numero = 4

numero_impar = 5

[3] - Utilize 4 espaços para identação!(Não use o Tab)


if 'a' in 'banana':
    print('tem')

[4] - Linhas em branco

- Separar funções e definições de classe com  duas linhas em brnaco;
= métados dentro do uma classe devem ser separados com uma unica linha em branco;

[5] - Imports

- Imports devem ser sempre feitos em linhas separadas;
# Import Errado

import sys, os

# Import Certo

import sys
import os

# Não há problemas em utilizar:

from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

from type import (
    StringType,
    ListType,
    SetType,
    OutroType
)

# Imports devem ser colocados no topo do arquivo, logo depois do qualquer comentarios ou docstrings
# e antes de constantes ou variaveis globais.


"""
