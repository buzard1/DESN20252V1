string = input("Digite um texto : ")
inversa = ""
string_sem_espacos = string.replace(" ", "")
for x in string_sem_espacos:
    inversa = x + inversa
print(inversa)
if string_sem_espacos == inversa:
    print("É um Palíndromo")
else:
    print("Não é um Palíndromo")
    