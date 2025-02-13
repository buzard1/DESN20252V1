n = int(input("Uma quantidade de números para ser analisada: "))
print("Informe o número: ")
anterior = int(input())

i = 1 #leu um número
ordenado = 0 # variavel contadora

while (i < n) and (ordenado == 0):
    print("Informe o número: ")
    atual = int(input())
    i = i + 1 #leu mais um numero
    if (atual <= anterior):
        ordenado = ordenado + 1
    anterior = atual

if(ordenado == 0):
    print("Sequência está ordenada.")
else:
    print("Sequência não está ordenada.")