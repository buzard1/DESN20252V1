n = int(input("Digite uma quantidade de números para ser analisada: "))
print("Informe os números:")

numeros = []
for i in range(n):
    numeros.append(input())

adjacente = False
for i in range(n - 1):
    if numeros[i][-1] == numeros[i + 1][0]:
        adjacente = True
        break

if adjacente:
    print("Sim")
else:
    print("Não")
