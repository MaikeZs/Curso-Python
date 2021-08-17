"""
#Criaçao de Dicionarios
#Forma 01 (mais Comum)

paises = {'bra': 'Brasil', 'eua': 'Estaudos Unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))


#Forma 02 (Menos Comum)

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguay')

print(paises)
print(type(paises))

#print(type({}))

# Acessando elementos
# Forma 1 - Acessando via chave,  da mesma forma que lista/tupla

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguay')

print(paises['br'])

#print(paises['ru'])

# obs> Caso tentamos fazer um cesso utilizando uma chave que nao existe, teremos o erro KeyError

# Forma 2 - Acessando via get - Recomendado

print(paises.get('br'))
print(paises.get('ru'))

# caso o get nao encontre o objeto com a chave informada sera retornado o
valor None e nao sera gerado KeyErro

if pais:
    print(f'Encontrei o Pais {pais}')
else:
    print('Nao encrontei o pais')

# Podemos definir um vlaor padrao para caso nao encontremos o objeto com a chave informada
pais = paises.get('ru', 'Nao encontrado')

print(f'Encontrei o pais {pais}')

# Podemos utilizer qualquer tipo de dado (int, float, string, boolean), inclusice lista, tupla  dicionario, como chaves
# de dicionario.

# Tuplas por exemplo sao bastante interessante de serem utilizads como chave de dicionario,
# pois as mesmas sao imutaveis
localidade = {
    (52.333, 55.4480): 'casa 01',
    (66.454, 75.1741): 'casa 02',
    (75.123, 85.7411): 'casa 03',
}

print(localidade)
print(type(localidade))

# Adicionar elemntos em um dicionario

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)
print(type(receita))

# Forma 1 - Mais comum

receita['abr'] = 350

print(receita)

# Forma 2 - Menos comum

novo_dado = {'mai': 500}

receita.update(novo_dado)

print(receita)

# Att dados em um dicionario

# Forma 1

receita['mai'] = 550

print(receita)

# Forma 2

receita['mai']= 600

print(receita)

# Conclusao 01: A forma de adicionar novos elementos oi atualizar dados em um dicionario e a mesma
# Conclusao 02: Em dicionarios, nao podemos ter chaves repetidas.

# Remover dados de um dicionario

receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)

# Forma 1

ret = receita.pop('mar')
print(ret)
print(receita)

# Obs 1 : aqui precisamos sempre informa a chave, e caso nao encontre o elementom, um KeyError e retornado.
# Obs 2 : Ao removermos um objeto, o valor deste objetoe sempre retornado.

# Forma 2

del receita['fev']

print(receita)
# Se a chave nao existir sera gerado um KeyError
# Obs: neste caso o valor removido nao e retornado.

# imagine que voce tem um comercio eletronico, onde tmoes um carrinho de compras na qual adcionamos produtos.

Carrinho de Compras:
    Produto 1:
        - nome;
        - quantidade;
        - preço;
    Produto 2:
        - nome;
        - quantidade;
        - preço;


# 1 Poderimos utilizar em lista para isso ? sim

carrinho = []

prod1 = ['laps', 1, 1.50]
prod2 = ['caneta', 1, 2.00]

carrinho.append(prod1)
carrinho.append(prod2)

print(carrinho)

# Terimos que saber qual e o indice de cade informçao no produto

# 2 Podemos utilizar um dicionario para isso ? sim

prod1 = ('laps', 1, 1.50)
prod2 = ('caneta', 1, 2.00)

carrinho = (prod1, prod2)

print(carrinho)

# 3 poderiamos utilizar um dicionario para isso ? sim

carrinho = []

prod1 ={'nome': 'laps', 'quantidade': 1, 'preço': 1.50}
prod2 ={'nome': 'caneta', 'quantidade': 1, 'preço': 2.00}

carrinho.append(prod1)
carrinho.append(prod2)

print(carrinho)

# Desta forma, facilmente adicionamos ou removemos produtos no carrinho em em cada produto
# Podemos ter a certeza sobre cade produto.

# Metados de dicionarios

d = dict(a=1, b=2, c=3)

print(d)
print(type(d))

# Limpar o dicionario (Zerar dados)

d.clear()

print(d)

# copiando um dicionario para outro

# Forma 1

novo = d.copy()

print(novo)

novo['d'] = 4

print(d)
print(novo)

"""



