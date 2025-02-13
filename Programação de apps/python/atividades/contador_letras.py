def n(s):
    s = s.replace(" ","")
    contagem = {}
    for L in s:
        L = L.lower()
        if L in contagem:
            contagem[L] += 1
        else:
            contagem[L] = 1
    L_C = max(contagem, key=contagem.get)
    return L_C

string = input("Digite a frase: ")
resultado = n(string)
print(f'A letra mais comum é: {resultado}')