import tkinter as tk
from tkinter import ttk

dicionario_cotacoes = {
'Dolar': 5.47,
'Euro': 6.68,
'Bitcoin':20000
}

def buscar_cotacao():
    print(moeda.get())
    moeda_preenchida = moeda.get()
    cotacao_moeda = dicionario_cotacoes.get(moeda_preenchida)
    mensagem_cotacao = tk.Label(text = "Cotação não encontrada")
    mensagem_cotacao.grid(row=3,column=0)
    if cotacao_moeda:
       mensagem_cotacao["text"] = f'Cotação do {moeda_preenchida} é de {cotacao_moeda} reais'





janela = tk.Tk()
janela.title('Cotação de moedas')

mensagem = tk.Label(text='Sistema de busca de cotação de Moedas', fg='white',bg='black', width=35, height=5) 
mensagem.grid(row=0, column=0, columnspan=2, sticky="NSEW")

mensagem2 = tk.Label(text = 'Selecione a moeda desejada')
mensagem2.grid(row=1, column=0)

#moeda = tk.Entry()
#moeda.grid(row=1, column=1)

moedas = list(dicionario_cotacoes.keys())
moeda = ttk.Combobox(janela, values=moedas)
moeda.grid(row=1, column=1)

botao = tk.Button(text="Buscar Cotação",  command=buscar_cotacao)
botao.grid(row=2, column=1)

janela.mainloop()
