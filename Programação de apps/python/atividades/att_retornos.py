def numero():
    num = int(input("Digite um número inteiro: "))
    if num > 0:
        return("P(positivo)") 
    elif num < 0:
        return("N(negativo)")
    else:
        return("Z(zero)") 

resultado = numero()
print(resultado)
