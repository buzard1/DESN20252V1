# Solicita ao usuário o número de mensagens que ele quer digitar
numero_de_mensagens = int(input("Quantas mensagens você deseja digitar? "))

mensagens = []  # Lista para armazenar as mensagens

for numero in range(1, numero_de_mensagens + 1):  # Laço vai de 1 até o número que o usuário escolheu
    entrada = input(f"Digite a {numero}° mensagem: ")  # Solicita a entrada
    mensagens.append(entrada)  # Adiciona a entrada na lista

# Exibe as mensagens após a coleta
for i in range(numero_de_mensagens):  # Exibe as mensagens com base no número inserido
    print(f"{i + 1}° mensagem: {mensagens[i]}")
