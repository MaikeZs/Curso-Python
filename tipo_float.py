"""
Tipo Float

Tipo real, decimal

Casas decimais

obs: o separador de casas decimais na programaçao e o ponto e nao virgula.
"""
# Errado do ponto de vista do Float, mas gera uma tupla
valor = 1,44
print(valor)
print(type(valor))

# Certo do ponto de vista  Float
valor = 1.44
print(valor)
print(type(valor))

# É possivel fazer dupla atribuição
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))
