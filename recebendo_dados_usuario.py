"""
Recebendo Dados do usuario.

"""
#  Entrada de Dados
#  print("Qual e seu nome?")
#  nome = input()  # input -> Entrada

nome = input("Qual e seu Nome?")

#  Exmplo de print 'antigo' 2.x
#  print('Seja Bem-Vindo(a) %s' % nome)

#  Exmplo de print 'mordeno' 3.x
#  print('Seja Bem-Vindo(a) {0}'.format(nome))

#  Exemplo de print 'mais atual' 3.7
print(f'Seja Bem-Vindo(a) {nome}')

#  print("Qual e sua idade?")
   #idade = input()

idade = input("Qual e sua idade?")

#  Processamento

#  Saida de dados

#  Exmplo de print 'mordeno' 3.x
#  print('A {0} tem {1} Anos '.format(nome, idade))

#  Exemplo de print 'mais atual' 3.7
print(f'A {nome} tem {idade} Anos')

"""
int(idade) => cast

Cast é a 'conversão' de um tipo de dado para outro.
"""

print(f'A {nome} nasceu em {2021 - int(idade)}')
