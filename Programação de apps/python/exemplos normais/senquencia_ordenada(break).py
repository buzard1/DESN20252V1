n = int(input("Digite uma quantidade de números para ser analisada: "))
print("Informe o número: ")
anterior = int(input())

ordenado = True # variavel indicadora

for i in range(n-1):
    print("informe o número: ")
    atual = int(input())
    i = i + 1 #leu mais um número
    if(atual < anterior):
        ordenado = False
        break
    anterior = atual

if(ordenado):
    print("Sequência ordenada.")
else:
    print("Sequência não ordenada.")