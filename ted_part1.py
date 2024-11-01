VET = [0] * 10

print("Digite 10 números e, no final, vou te mostrar se algum número se repete e onde ele aparece.")

for i in range(10):
    VET[i] = int(input(f"Por favor, digite o número {i + 1}: "))


repeticoes = {}


for i in range(10):
    numero = VET[i]
    if VET.count(numero) > 1:  
        if numero not in repeticoes:
            repeticoes[numero] = [None] * 10  
        for pos in range(10):
            if repeticoes[numero][pos] is None:
                repeticoes[numero][pos] = i  
                break

if repeticoes:
    print("Números repetidos e suas posições:")
    for numero, posicoes in repeticoes.items():
        posicoes_list = ""
        for pos in posicoes:
            if pos is not None:
                posicoes_list += f"{pos + 1}, "
        print(f"O número {numero} aparece nas posições: {posicoes_list[:-2]}")
else:
    print("Nenhum número se repete na lista!")
