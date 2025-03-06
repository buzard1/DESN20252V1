import tkinter as tk
from tkinter import messagebox

class AcaiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Açaí 🍧")

        # Variáveis
        self.tamanho_var = tk.StringVar(value="Pequeno")
        self.pagamento_var = tk.StringVar(value="Dinheiro")
        self.acompanhamentos = {
            "Leite Condensado": tk.BooleanVar(),
            "Granola": tk.BooleanVar(),
            "Banana": tk.BooleanVar(),
            "Paçoca": tk.BooleanVar(),
            "Morango": tk.BooleanVar()
        }

        # Criando a interface
        tk.Label(root, text="Escolha o tamanho do copo:").pack()
        tamanhos = ["Pequeno", "Médio", "Grande"]
        for tamanho in tamanhos:
            tk.Radiobutton(root, text=tamanho, variable=self.tamanho_var, value=tamanho).pack()

        tk.Label(root, text="Escolha os acompanhamentos:").pack()
        for item, var in self.acompanhamentos.items():
            tk.Checkbutton(root, text=item, variable=var).pack()

        tk.Label(root, text="Forma de pagamento:").pack()
        pagamentos = ["Dinheiro", "Cartão", "Pix"]
        for pag in pagamentos:
            tk.Radiobutton(root, text=pag, variable=self.pagamento_var, value=pag).pack()

        self.resultado_label = tk.Label(root, text="", fg="blue")
        self.resultado_label.pack()

        tk.Button(root, text="Finalizar Pedido", command=self.finalizar_pedido, fg="red").pack()
        tk.Button(root, text="Montar Novo Açaí", command=self.montar_acai).pack()

    def montar_acai(self):
        tamanho = self.tamanho_var.get()
        pagamento = self.pagamento_var.get()
        acompanhamentos_selecionados = [item for item, var in self.acompanhamentos.items() if var.get()]

        if not acompanhamentos_selecionados:
            acompanhamentos_texto = "Nenhum"
        else:
            acompanhamentos_texto = ", ".join(acompanhamentos_selecionados)

        resumo = f"Tamanho: {tamanho}\nAcompanhamentos: {acompanhamentos_texto}\nPagamento: {pagamento}"
        self.resultado_label["text"] = resumo
        messagebox.showinfo("Açaí Montado!", resumo)

    def finalizar_pedido(self):
        if messagebox.askyesno("Finalizar", "Tem certeza que deseja encerrar?"):
            self.root.quit()

# Criando a interface
root = tk.Tk()
app = AcaiApp(root)
root.mainloop()
