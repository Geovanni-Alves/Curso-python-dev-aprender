# Set
numeros = [2, 2, 5, 8]
frutas = {"maça", "uva", "banana", "maça", "morango"}
print(set(numeros))
print(set(frutas))

numeros1 = [2, 2, 5, 8]
numeros2 = [2, 2, 3, 9]
a = set(numeros1)
b = set(numeros2)
print(a.symmetric_difference(b))
print(a.intersection(b))
print(a.union(b))
