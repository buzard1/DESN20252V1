# Solicita ao usuário que digite um número inteiro
n = int(input("Digite um número: "))

# Laço para percorrer de 1 até n (inclusive)
for i in range(1, n + 1):
    # Laço interno para imprimir os números de 1 até i
    for j in range(1, i + 1):
        print(j, end=" ")  # Imprime o número na mesma linha com um espaço
    print()  # Quebra a linha após imprimir a sequência
