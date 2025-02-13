class Pessoa:
    nome = ""
    idade = 0
    peso = 0.0
    altura = 0.0

    def envelhecer(self):
        self.idade += 1
        if self.idade < 21:
            self.altura += 0.5

    def engordar(self, valor):
        self.peso += valor

    def emagrecer(self, valor):
        self.peso -= valor

    def crescer(self, valor):
        self.altura += valor

if __name__ == '__main__':
    pessoa = Pessoa()
    pessoa.nome = "João"
    pessoa.idade = 25
    pessoa.peso = 70
    pessoa.altura = 170

    pessoa.envelhecer()  
    pessoa.engordar(2)  
    pessoa.emagrecer(1)  

    print(pessoa.nome)
    print(pessoa.idade)
    print(pessoa.peso)
    print(pessoa.altura)
