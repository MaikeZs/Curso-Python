maior = 0

n = int(input("informe um numero? "))

while n != 0:
    if n > maior:
        maior = n
    n = int(input("iforme um numero: "))
print("o maior numero e {0}".format(maior))
