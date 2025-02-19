# Criação de uma lista vazia para armazenar as notas
notas = []

# Solicita ao usuário o número de notas que serão inseridas
n = int(input("Digite o número de notas: "))

# Laço para ler as notas e adicioná-las à lista
for i in range(n):
    # Solicita uma nota ao usuário e converte para float
    dado = float(input(f"Digite a nota {i + 1}: "))
    # Adiciona a nota digitada à lista 'notas'
    notas.append(dado)
    # Exibe a lista de notas atualizada após cada inserção
    print(notas)

# Inicializa a variável 'soma' para acumular as notas
soma = 0

# Laço para percorrer todas as notas e somá-las
for i in range(len(notas)):
    soma = soma + notas[i]  # Adiciona a nota atual à soma

# Calcula a média dividindo a soma pelo número total de notas
media = soma / len(notas)

# Exibe a média formatada com uma casa decimal
print("A média das notas é: {}".format(format(media, ".1f")))

