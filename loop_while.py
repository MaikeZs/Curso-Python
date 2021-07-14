"""
Loop while

Rorma geral

while expressao_boolean:
    //execucao do loop


O bloco do while sera repetido enquanto a expressao booleana for verdadeira.

Expressao booleana e toda expresao onde o resiltado e verdadeiro ou falso.

exemplo:

num = 5

num < 5

# 01
num = 1

while num < 10:
    print(num)
    num = num + 1

# OBs : Em um loop while, é importante que cuidemos do criterios de parada para nao causar um loop infinito.

"""


resposta = ''

while resposta != 'sim':
    resposta = input('Ja acabou jessica?')
