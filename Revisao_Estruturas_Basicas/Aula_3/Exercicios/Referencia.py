# EXERCÍCIO 1 - REFERÊNCIA

a = [10, 20, 30]
b = a  # "b" passa a apontar para o mesmo objeto que "a"

print("a: " + str(a)) # visualizando o valor de "a"

b.append(40)  # como "b" esta apontando para "a", ambos modificam o valor

print("a: " + str(a))
print("b: " + str(b))
print("id(a): " + str(id(a)))
print("id(b): " + str(id(b)))
