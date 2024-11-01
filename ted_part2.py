import random

A = [[random.randint(1, 100) for _ in range(10)] for _ in range(10)]

soma_total = sum(sum(linha) for linha in A)
print(f"Soma de todos os valores da matriz A: {soma_total}")

B = [[elemento * 3 for elemento in linha] for linha in A]
 
print("Matriz B (Matriz A multiplicada por 3):")
for linha in B:
    print(linha)
