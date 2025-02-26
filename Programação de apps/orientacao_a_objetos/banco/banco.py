from datetime import datetime
import pytz
from random import randint


class ContaCorrente():


    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, nome, cpf, agencia, num_conta):
        self._nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None
        self.agencia = agencia
        self._num_conta = num_conta
        self.transacoes = []
        self._cartoes = []

    def consultar_saldo(self):
        print("Seu saldo atual é de R${:,.2f}".format(self.saldo))

    def depositar_dinheiro(self,valor):
        self.saldo += valor
        self.transacoes.append((valor, self.saldo, ContaCorrente._data_hora()))

    def _limite_conta(self):
        self.limite = -1000
        return self.limite

    def sacar_dinheiro(self,valor):
        if self.saldo -valor < self._limite_conta():
            print("Você não tem saldo suficiente para sacar esse valor")
            self.consultar_saldo()
        else:
            self.saldo -= valor
            self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora()))


    def consultar_historico_transacoes(self):
        print("Historico de transações: ")
        for transacao in self.transacoes:
            print(transacao)

    def transferir(self, valor, conta_destino):
        self.saldo -= valor
        self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora()))
        conta_destino.saldo += valor
        conta_destino.transacoes.append((valor, conta_destino.saldo,ContaCorrente._data_hora()))


class CartaoCredito():

    @staticmethod
    def _data_hora():
            fuso_BR = pytz.timezone('Brazil/East')
            horario_BR = datetime.now(fuso_BR)
            return horario_BR
    


    def __init__(self,titular, conta_corrente):
        self.numero = randint (1000000000000000,9999999999999999)
        self.titular = titular
        self.validade =  '{}/{}'.format(CartaoCredito._data_hora().month, CartaoCredito._data_hora().year +4)
        self.cod_segurança =  '{}{}{}'.format(randint(0,9),randint(0,9),randint(0,9))
        self.limite = 1000
        self.conta_corrente = conta_corrente
        conta_corrente._cartoes.append(self)


#programa

conta_lira = ContaCorrente("lira","111.222.333-45","1234","34062")
conta_maelira = ContaCorrente('beth', '222.333.444-55','5555','656565')
conta_lira.consultar_saldo()
conta_lira._saldo = 8000
cartao_lira = CartaoCredito("lira", conta_lira)
cartao_lira.numero=123

#depositar um dinheiro na conta:
conta_lira.depositar_dinheiro(10000)
conta_lira.consultar_saldo()

#cartão de credito
print(cartao_lira.__dict__)



#sacando dinheririnho da conta
conta_lira.sacar_dinheiro(1000)

#transferir dinheiro
conta_lira.transferir(1000, conta_maelira)

print("Saldo Final: ")
conta_lira.consultar_saldo()

#historico de transaçoes
conta_lira.consultar_historico_transacoes()
