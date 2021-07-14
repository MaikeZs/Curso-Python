import q as q

quantidade_minima = int(input("informe a quantidade mínima:"))
quantidade_maxina = int(input("Informe a quantidade máxima: "))

estoque_medio = (quantidade_minima + quantidade_maxina)/2

print("o estoque médio é {0}".format(estoque_medio))
