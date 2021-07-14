"""
Saindo de loops com break

Fuciona da mesma forma que nas linguagens c ou java.

utilizamos o break para sair de loops de maneira projeta.

# 01
for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print('Saindo')

"""

#02

while True:
    comando = input("digite 'sair' para sair")
    if comando == 'sair': 
        break

