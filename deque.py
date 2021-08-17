"""
Modulo collection - Deque

https://docs.python.org/3/library/collections.html?highlight=collections#collections.deque

podemos dizer que o deque e uma lista de alta performance.

"""
# imortando

from collections import deque

#criando deque

deq = deque('Maike')

print(deq)

# Adicionando elementos do deque

deq.append('e')

print(deq)

deq.appendleft('k') # adiciona no começo

print(deq)