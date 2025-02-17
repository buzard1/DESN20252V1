def main():
    n = int(input("Digite o número de notas: "))
    notas = leNota(n)
    print("As notas são:", notas)
    media = calculaMedia(notas)
    print("A média é:", format(media, ".1f"))

def leNota(num):
    notas = []
    for i in range(num):
        dado = float(input("Digite a nota: "))
        notas.append(dado)
    return notas

def calculaMedia(notas):
    soma = 0
    for i in range(len(notas)):
        soma = soma + notas[i]
    return(soma/len(notas))
main()
