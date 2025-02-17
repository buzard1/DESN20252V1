string = input("Digite um numero : ")
inversa = ""
string_sem_espacos = string.replace(" ", "")
for x in string_sem_espacos:
    inversa = x + inversa
print(inversa)

    