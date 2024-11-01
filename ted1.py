VET = [0] * 10 

print("Digite 10 números. No final, vou te mostrar se algum número se repete e onde ele aparece.")

for i in range(10):
    VET[i] = int(input(f"Digite o número {i + 1}: "))

repeticoes = {}

 
for i in range(len(VET)):
    valor = VET[i]   
    if VET.count(valor) > 1:   
        if valor not in repeticoes:
            repeticoes[valor] = [None] * 10  
        if repeticoes[valor][0] is None:
            repeticoes[valor][0] = i   
        else:
            pos = 1
            while repeticoes[valor][pos] is not None:  
                pos += 1
            repeticoes[valor][pos] = i  
if repeticoes:
    print("Esses números se repetem:")
    for numero in repeticoes:
        posicoes = repeticoes[numero]
        
        posicoes_formatadas = ""
        for pos in posicoes:
            if pos is not None:
                posicoes_formatadas += f"{pos + 1}, "
        print(f"O número {numero} aparece nas posições: {posicoes_formatadas[:-2]}")
else:
    print("Boa notícia: Nenhum número se repete na lista!")
