n= int(input("Digite um número inteiro positivo: "))

numero = 2
primo = True #variável indicadora

while (numero <= n-1):
    if (n % numero == 0): #verifica  se é divisível pelo número
        primo = False
        break
    numero = numero + 1

if (primo):
    print("É primo.")
else:
    print("Não é primo.")