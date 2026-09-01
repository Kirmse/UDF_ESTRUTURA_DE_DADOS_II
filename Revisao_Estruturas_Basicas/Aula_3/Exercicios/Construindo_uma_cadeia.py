# EXERCÍCIO 2 - CONSTRUINDO UMA CADEIA

class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None  # referencia para o proximo nó da cadeia


n1 = Node("A")
n2 = Node("B")
n3 = Node("C")

# Conectando os nós
n1.proximo = n2
n2.proximo = n3

# Percorrendo a cadeia a partir do primeiro nó
atual = n1
while atual is not None:
    print(atual.valor)
    atual = atual.proximo  # avanca para o proximo nó
