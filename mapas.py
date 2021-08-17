"""
Mapas -> Conhcidos em Python como dicionarios

Dicionarios em Python sao representados por chaves {}

# Interar sobre dicionarios

for chave in receitas:
    print(chave)

for chave in receitas:
    print(receitas[chave])

for chave in receitas:
    print(f'{chave} : recebi R$ {receitas[chave]}')

# Acessando as chaves
print(receitas.keys())

for chave in receitas.keys():
    print(receitas[chave])

# Acessando os valores

print(receitas.values())

for valor in receitas.values():
    print(valor)

# Desempacotador de dicionarios

for chave, valor in receitas.items():
    print(f'chave={chave} e valor={valor}')


"""
receitas = {'jan': 100, 'fev': 250, 'mar': 400}

print(receitas)


# Soma+, valor maximo*, valor minimo*, tamanho
# * se os valores forem todos inteiros ou reais

print(sum(receitas.values()))
print(max(receitas.values()))
print(min(receitas.values()))
print(len(receitas))
