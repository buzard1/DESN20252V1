n = int(input("Digite uma quantidade de números para ser analisada: "))
print("Informe o número: ")
anterior = int(input())

i = 1 #leu o numero
ordenado = True # variavel indicadora

while (i < n) and (ordenado):
    print("informe o número: ")
    atual = int(input())
    i = i + 1 #leu mais um número
    if(atual < anterior):
        ordenado = False
    anterior = atual

if(ordenado):
    print("Sequência ordenada.")
else:
    print("Sequência não ordenada.")