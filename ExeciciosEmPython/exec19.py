numero = int(input("informe um numero entre 1 e 10: "))

while numero < 1 or numero > 10:
    numero = int(input("informe um numero entre 1 e 10: "))
print("tabuada de {0}".format(numero))
for n in range(1, 11):
    print("{0} x {1} = {2}".format(numero, n, numero * n))
