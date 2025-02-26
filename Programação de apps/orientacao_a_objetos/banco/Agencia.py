from random import randint

class Agencia():

    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []
        
    def adicionar_cliente(self,nome,cpf,patrimonio):
        self.clientes.append((nome,cpf,patrimonio))
    def verificar_caixa(self):
        if self.caixa < 1000000:
            print("Caixa abaixo do nivel recomendado. Caixa Atual: {}" .format(self.caixa))
        else:
            print("O valor de Caixa esta ok. Caixa Atual: {}" .format(self.caixa))

    def empresestar_dinheiro(self, valor, cpf, juros):
        if self.caixa>valor:
            self.emprestimos.append((valor, cpf, juros))
            print('Empréstmo efetuado')
        else:
            print('Empréstimo não é possivel. Dinheiro não disponivel em caixa')

    def adicionar_cliente(self,nome,cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))

class AgenciaVirtual(Agencia):

    def __init__(self, site, telefone, cnpj, numero):
        self.site = site
        super().__init__(telefone, cnpj, numero)
        self.caixa = 1000000
        self.caixa_paypal = 0
    
    def depositar_paypal(self,valor):
        self.caixa -= valor
        self.caixa_paypal += valor

    def sacar_paypal(self,valor):
        self.caixa_paypal -= valor
        self.caixa += valor
    def adicionar_cliente(self, nome, cpf, patrimonio):
        if patrimonio >1000000:
            super().adicionar_cliente(nome, cpf, patrimonio)
        else:
            print('Cliente não possui o patrimonio mínimo necessário')


class AgenciaComum(Agencia):



    def __init__(self, telefone, cnpj):
        super().__init__ (telefone, cnpj, randint(1001,9999))
        self.caixa=1000000

    def adicionar_cliente(self, nome, cpf, patrimonio):
        if patrimonio >1000000:
            super().adicionar_cliente(nome, cpf, patrimonio)
        else:
            print('Cliente não possui o patrimonio mínimo necessário')

class AgenciaPremium(Agencia):

    def __init__(self ,telefone, cnpj):
        super().__init__(telefone, cnpj, randint(1001 ,9999))
        self.caixa=10000000

    def adicionar_cliente(self, nome, cpf, patrimonio):
        if patrimonio >1000000:
            super().adicionar_cliente(nome, cpf, patrimonio)
        else:
            print('Cliente não possui o patrimonio mínimo necessário')