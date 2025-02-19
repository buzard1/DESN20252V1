# Cria duas listas vazias para armazenar os números inteiros
lista1 = []
lista2 = []

# Lê 5 números inteiros para a primeira lista
print("Digite 5 números inteiros para a primeira lista:")
for i in range(5):
    numero = int(input(f"Digite o {i + 1}º número: "))  # Lê um número inteiro do usuário
    lista1.append(numero)  # Adiciona o número à lista1

# Lê 5 números inteiros para a segunda lista
print("\nDigite 5 números inteiros para a segunda lista:")
for i in range(5):
    numero = int(input(f"Digite o {i + 1}º número: "))  # Lê um número inteiro do usuário
    lista2.append(numero)  # Adiciona o número à lista2

# Verifica quais elementos da segunda lista também estão na primeira
comuns = []  # Lista para armazenar os números em comum

for elemento in lista2:
    if elemento in lista1:  # Checa se o elemento da lista2 está em lista1
        comuns.append(elemento)  # Adiciona o elemento à lista de comuns

# Exibe o resultado com base nos números encontrados
if comuns:  # Se a lista 'comuns' não estiver vazia
    print("\nElementos em comum:", comuns)
else:
    print("\nNão há elementos em comum entre as listas.")
