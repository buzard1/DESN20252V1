def imprimeCaixa(numero):
    tamanho = len(str(numero))
    for i in range(12+tamanho):
        print('+', end='')
    print()
    print('| Número:', numero,'|')
    for i in range(12+tamanho):
        print('+', end='')
    print()

imprimeCaixa(10)
imprimeCaixa(123456)