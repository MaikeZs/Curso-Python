"""
modulo collections - counter

collections -> High-performance container Datetypes

https://docs.python.org/3/library/collections.html?highlight=collections#collections.Counter

Counter - Recebe um interavel como parametro e cria um objeto do tipo collection counter
que e parecido com um dicionario, contendo como chave o elemnto da lista passada como
parametro e como valor e quantidade de ocorrencias desse elementos.


# Realizando o import

from collections import Counter

#exemplo 1

# Utilizando counter
lista = [1, 1, 1, 2, 2, 2, 3, 3, 3, 2, 5, 5, 6, 66, 66, 66, 66, 77, 77, 4, 7, 0, 12345]

res = Counter(lista)
print(res)

#exemplo 2
print(Counter('Maike Moura Da Silva'))

#Counter({'a': 4, ' ': 3, 'M': 2, 'i': 2, 'k': 1, 'e': 1, 'o': 1, 'u': 1, 'r': 1, 'D': 1, 'S': 1, 'l': 1, 'v': 1}
"""

from collections import Counter

texto = """O Portugal continental atual, juntamente com a maior parte da Espanha moderna, 
fez parte do al-Andalus, entre 726 e 1249, após a conquista da Península Ibérica pelo Califado 
Omíada. O domínio islâmico durou entre algumas décadas, a norte, e cinco séculos, no sul.[30]
Depois de derrotar os visigodos em apenas alguns meses, o Califado Omíada começou a expandir-se 
rapidamente na península. A partir de 726, o território português atual tornou-se parte do vasto
império omíada centrado em Damasco, que se estendia desde rio Indo no subcontinente indiano ao sul da 
França, até seu colapso em 750. Naquele ano, o oeste do império ganhou a sua 
independência sob Abderramão I com o estabelecimento do Emirado de Córdoba. Após quase dois
séculos, o emirado tornou-se o Califado deCórdoba em 929, até à sua dissolução, em 1031, em 23 
pequenos reinos, chamados taifas 30
Os governadores das taifas proclamaram-se emires das suas províncias e estabeleceram relações
diplomáticas com os reinos cristãos do norte. A maior parte de Portugal caiu nas mãos da taifa 
de Badajoz da dinastia Abássida, e após um curto período de uma efémera taifa de Lisboa em 1022,
ficou sob domínio da taifa de Sevilha dos poetas dos abádidas. O período das taifas terminou com a 
conquista almorávida, proveniente de Marrocos, em 1086, e tiveram uma vitória decisiva na Batalha de 
Zalaca. Al-Andaluz foi dividida em diferentes distritos chamados cora. O Algarbe Alandalus, no seu auge, 
era constituído por dez coras,[31] cada um com uma capital e governadores distintos. As principais cidades 
do período situavam-se no sul do país. A população muçulmana da região consistia principalmente de ibéricos 
nativos convertidos ao islão (os chamados muladis) e berberes. Os árabes eram principalmente nobres da Síria 
e Omã; e apesar de em menor número, constituíam a elite da população. Os berberes eram nómadas originários das 
montanhas do Atlas e Rife do norte da África.[30]"""

palavras = texto.split()
#print(palavras)

res = Counter(palavras)

print(res)


# Encontrando as 5 palavras com mais ocorrencias no texto
print(res.most_common(10))