n = int(input("Digite um número inteiro positivo: "))

# Verificando se o número é 1
if n == 1:
    print("Não é primo. O número 1 não é considerado primo.")
else:
    numero = 2
    divisores = 0  # divisores é a variável contadora

    while(numero <= n-1):
        if (n % numero == 0):
            divisores = divisores + 1
        numero = numero + 1

    if(divisores == 0):
        print("É primo.")
    elif(divisores == 1):
        print("Não é primo. Possui 1 divisor diferente de 1 e ", n)
    else:
        print("Não é primo. Possui", divisores, "Divisores Diferentes de 1 e ", n)
