valor_por_hora = float(input("Quanto você ganha por hora?"))
horas_trabalhadas = int(input("Quantas horas você trabalhou neste mês?"))

salario = horas_trabalhadas * valor_por_hora

print("Neste Mês você vai receber R$ {0:.2f}".format(salario))
