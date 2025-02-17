texto =input("Digite um texto: ")
pontuacao = [".", ",", ":", ";", "!", "?"]

#remove os sinais de pontuacao

for p in pontuacao:
    texto = texto.replace(p," ")

numero_palavras = len(texto)
print("Número de palavras: ",numero_palavras)