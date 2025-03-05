from banco import ContaCorrente, CartaoCredito
from Agencia import Agencia
from Agencia import AgenciaVirtual
from Agencia import AgenciaComum
from Agencia import AgenciaPremium

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
print("\n cartão de credito: ")
print(cartao_lira.__dict__)

#agencia
Agencia1 = Agencia(22223333,200000000,4568)
Agencia1.caixa=1000000
Agencia1.adicionar_cliente('lira',11122233344,10000)
print("\n Agencia: ")
print(Agencia1.clientes)
print(Agencia1.__dict__)
Agencia1.verificar_caixa()
Agencia1.empresestar_dinheiro(10,11122233344, 0.1)

#agencia virtual
agencia_virtual = AgenciaVirtual('www.agenciavirtual.com.br',22224444,152000000000, 1000)
agencia_virtual.verificar_caixa()
print("\nAgencia virtual:")
print(agencia_virtual.__dict__)





#agencia comum
agencia_comum = AgenciaComum(33334444,222000000000)
agencia_comum.verificar_caixa()
print("\nAgencia Comum:")
print(agencia_comum.__dict__)

#agencia premium

agencia_premium = AgenciaPremium(33333333,3000000000000)
print('\nAgencia Premium: ')
print(agencia_premium.__dict__)

#depositar dinheiro virtual
agencia_virtual.depositar_paypal(20000)
print(agencia_virtual.caixa)
print(agencia_virtual.caixa_paypal)

#adicionando clientes
print("\nAdicionando Clientes: ")




Agencia1.adicionar_cliente("lira", 11111111111, 1000000)
print("cliente agencia1:" , Agencia1.clientes)

agencia_virtual.adicionar_cliente('Lira', 11111111111, 1000000)
print('clientes agencial:',agencia_virtual.clientes)

agencia_comum.adicionar_cliente('Lira', 11111111111, 1000000)
print('clientes agencial:',agencia_comum.clientes)

agencia_premium.adicionar_cliente('Lira',11111111111, 1000000)
print('Clientes agencia_premium: ', agencia_premium.clientes)

#sacando dinheririnho da conta
conta_lira.sacar_dinheiro(1000)

#transferir dinheiro
conta_lira.transferir(1000, conta_maelira)

print("\nSaldo Final: ")
conta_lira.consultar_saldo()

#historico de transaçoes
conta_lira.consultar_historico_transacoes()