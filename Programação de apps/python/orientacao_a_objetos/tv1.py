class TV:
    def __init__(self, cor, tamanho):
        self.cor = cor
        self.ligada = False
        self.tamanho = tamanho
        self.canal = "Netflix"
        self.volume = 10

    def mudar_canal(self):
        self.canal = "Disney+"
    def mudar_canal(self,novo_canal):
        self.canal = novo_canal
    
    

#Programa
tv_sala = TV(cor='preta',tamanho=55)
tv_quarto = TV('branca',29)

tv_sala.mudar_canal("globo")
tv_quarto.mudar_canal('Youtube')

print(tv_quarto.canal) # Impreme "Netflix"
print(tv_sala.canal) #Impreme "Netflix"
print(tv_sala.cor)
print(tv_sala.tamanho)
print(tv_sala.volume)