def potencia(a, b):
    if b == 0:
        return 1 
    if b < 0:
        return 1 / potencia(a, -b)  
    
    resultado = 1
    for _ in range(b):
        resultado *= a 
    
    return resultado


print(potencia(2, 4))  

