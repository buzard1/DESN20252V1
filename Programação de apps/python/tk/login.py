import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("300x200")

        tk.Label(root, text="Usuário:").pack()
        self.usuario_entry = tk.Entry(root)
        self.usuario_entry.pack()

        tk.Label(root, text="Senha:").pack()
        self.senha_entry = tk.Entry(root, show="*")
        self.senha_entry.pack()

        tk.Button(root, text="Login", command=self.verificar_login).pack()

    def verificar_login(self):
        usuario = self.usuario_entry.get()
        senha = self.senha_entry.get()

        if usuario == "admin" and senha == "123":
            self.root.destroy()
            abrir_admin()
        elif usuario == "cliente" and senha == "123":
            self.root.destroy()
            abrir_acai_cliente()
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos!")

def abrir_login():
    root = tk.Tk()
    LoginApp(root)
    root.mainloop()

class AdminApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin - Gerenciar Produtos")
        self.root.geometry("300x200")
        
        tk.Label(root, text="Tela de Admin").pack()
        tk.Button(root, text="Sair", command=self.voltar_login).pack()
    
    def voltar_login(self):
        self.root.destroy()
        abrir_login()

def abrir_admin():
    root = tk.Tk()
    AdminApp(root)
    root.mainloop()

class ClienteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Montar Açaí")
        self.root.geometry("300x200")
        
        tk.Label(root, text="Tela do Cliente").pack()
        tk.Button(root, text="Sair", command=self.voltar_login).pack()
    
    def voltar_login(self):
        self.root.destroy()
        abrir_login()

def abrir_acai_cliente():
    root = tk.Tk()
    AcaiApp(root)
    root.mainloop()

class AcaiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Açaí 🍧")
        self.root.configure(bg="gray")
        self.root.geometry("230x480")

        main_frame = tk.Frame(root, bg="gray")
        main_frame.pack(fill="both", expand=True)

        self.canvas = tk.Canvas(main_frame, bg="gray")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.scrollable_frame = tk.Frame(self.canvas, bg="gray")

        self.scrollable_frame.bind(
            "<Configure>", lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas_window = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.canvas.bind_all("<MouseWheel>", lambda e: self.canvas.yview_scroll(-1 * (e.delta // 120), "units"))

        self.pedidos = []
        self.tamanho_var = tk.StringVar(value="Pequeno")
        self.pagamento_var = tk.StringVar(value="Dinheiro")
        self.pre_pronto_var = tk.StringVar(value="Nenhum")

        self.precos_tamanhos = {
            "Pequeno": (10.00, "300ml"),
            "Médio": (15.00, "500ml"),
            "Grande": (20.00, "700ml")
        }

        self.adicional_tamanho = {
            "Pequeno": 0,
            "Médio": 5.00,
            "Grande": 10.00
        }

        self.precos_pre_prontos = {
            "Energia Total": 18.00,
            "Choco Love": 22.00,
            "Morango Supreme": 20.00,
            "Nutella Mix": 25.00,
            "Power Whey": 23.00
        }

        self.descricao_pre_prontos = {
            "Energia Total": "Açaí com banana, granola e mel.",
            "Choco Love": "Açaí com Nutella, Ovomaltine e chantilly.",
            "Morango Supreme": "Açaí com morangos, leite condensado e paçoca.",
            "Nutella Mix": "Açaí com Nutella, morango e chantilly.",
            "Power Whey": "Açaí com whey protein, banana e aveia."
        }

        self.precos_acompanhamentos = {
            "Leite Condensado": 5.00,
            "Granola": 4.50,
            "Banana": 3.50,
            "Paçoca": 3.00,
            "Morango": 4.00,
            "Nutella": 8.00,
            "Mel": 2.50,
            "Ovomaltine": 5.00,
            "Chantilly": 3.00
        }

        self.acompanhamentos = {item: tk.BooleanVar() for item in self.precos_acompanhamentos.keys()}

        self.criar_interface()

    def criar_interface(self):

        try:
            imagem = Image.open(r"C:\DESN2025V1\DESN20252V1\Programação de apps\python\tk\acai.png")  # Caminho absoluto
            imagem = imagem.resize((210, 65))  # Ajuste conforme necessário
            self.img_tk = ImageTk.PhotoImage(imagem)

    # Criar um rótulo para exibir a imagem no topo
            self.label_imagem = tk.Label(self.scrollable_frame, image=self.img_tk, bg='gray')
            self.label_imagem.pack(pady=5, anchor="n", fill="x")  # Fixando a imagem no topo e preenchendo a largura
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar a imagem: {e}")



        tk.Label(self.scrollable_frame, text="Escolha o tamanho do copo:", fg='white', bg='purple').pack(pady=5, fill="x")
        self.criar_radio_buttons_tamanhos()

        tk.Label(self.scrollable_frame, text="Escolha um açaí pré-pronto (Opcional):", fg='white', bg='purple').pack(pady=5, fill="x")
        self.criar_radio_buttons_acais()

        tk.Label(self.scrollable_frame, text="Escolha os acompanhamentos:", fg='white', bg='purple').pack(pady=5, fill="x")
        self.criar_check_buttons_acompanhamentos()

        tk.Label(self.scrollable_frame, text="Forma de pagamento:", fg='white', bg='green').pack(pady=2)
        self.criar_radio_buttons_pagamento()

        self.valor_total_label = tk.Label(self.scrollable_frame, text="Total: R$0.00", fg="green", bg='grey', font=("Arial", 12, "bold"))
        self.valor_total_label.pack()

        tk.Button(self.scrollable_frame, text="Adicionar Açai", command=self.montar_acai).pack()
        tk.Button(self.scrollable_frame, text="Finalizar Pedido", command=self.finalizar_pedido, fg="red").pack()

    def criar_radio_buttons_tamanhos(self):
        for tamanho, (preco, ml) in self.precos_tamanhos.items():
            tk.Radiobutton(self.scrollable_frame, text=f"{tamanho} - R${preco:.2f} ({ml})", 
                           variable=self.tamanho_var, value=tamanho, command=self.atualizar_total, bg="gray").pack()

    def criar_radio_buttons_acais(self):
        for nome, preco in self.precos_pre_prontos.items():
            frame = tk.Frame(self.scrollable_frame, bg="gray")
            frame.pack()
            tk.Radiobutton(frame, text=f"{nome} - R${preco:.2f}", 
                           variable=self.pre_pronto_var, value=nome, command=self.atualizar_total, bg="gray").pack(side=tk.LEFT)
            tk.Button(frame, text="?", command=lambda n=nome: self.mostrar_descricao(n), bg="gray").pack(side=tk.LEFT)

        tk.Radiobutton(self.scrollable_frame, text="Nenhum", variable=self.pre_pronto_var, value="Nenhum", command=self.atualizar_total, bg="gray").pack()

    def criar_check_buttons_acompanhamentos(self):
        for item, var in self.acompanhamentos.items():
            tk.Checkbutton(self.scrollable_frame, text=f"{item} - R${self.precos_acompanhamentos[item]:.2f}", variable=var, command=self.atualizar_total, bg="gray").pack()

    def criar_radio_buttons_pagamento(self):
        for pagamento in ["Dinheiro", "Cartão", "Pix(5% de desconto)"]:
            tk.Radiobutton(self.scrollable_frame, text=pagamento, variable=self.pagamento_var, value=pagamento, bg="gray").pack()

    def atualizar_total(self):
        total = 0
        tamanho = self.tamanho_var.get()
        pre_pronto = self.pre_pronto_var.get()

        if pre_pronto != "Nenhum":
            total += self.precos_pre_prontos[pre_pronto] + self.adicional_tamanho[tamanho]
        else:
            total += self.precos_tamanhos[tamanho][0]
        
        for item, var in self.acompanhamentos.items():
            if var.get():
                total += self.precos_acompanhamentos[item]

        self.valor_total_label.config(text=f"Total: R${total:.2f}")
    
    def montar_acai(self):
        pedido = {
            "Tamanho": self.tamanho_var.get(),
            "Açaí Pré-Pronto": self.pre_pronto_var.get(),
            "Acompanhamentos": ", ".join([item for item, var in self.acompanhamentos.items() if var.get()]),
            "Forma de Pagamento": self.pagamento_var.get(),
            "Preço": float(self.valor_total_label.cget("text").split("R$")[-1])
        }
        self.pedidos.append(pedido)
        messagebox.showinfo("Pedido Adicionado", "Açaí adicionado ao pedido!")

    def mostrar_descricao(self, nome):
        descricao = self.descricao_pre_prontos.get(nome, "Descrição não disponível.")
        messagebox.showinfo(nome, descricao)

    def finalizar_pedido(self):
        if not self.pedidos:
            messagebox.showwarning("Aviso", "Nenhum pedido foi feito!")
            return

        total_geral = sum(p["Preço"] for p in self.pedidos)
        cupom = "CUPOM FISCAL\n" + "-"*20 + "\n"
        for i, pedido in enumerate(self.pedidos, 1):
            cupom += f"Pedido {i}:\n"
            for chave, valor in pedido.items():
                cupom += f"{chave}: {valor}\n"
            cupom += "-"*20 + "\n"
        cupom += f"Total: R${total_geral:.2f}\nObrigado pela preferência!"

        # Criar uma nova janela para o cupom e a imagem
        nova_janela = tk.Toplevel(self.root)
        nova_janela.title("Cupom Fiscal")
        nova_janela.geometry("600x300")

        # Criando o Canvas com a barra de rolagem
        canvas = tk.Canvas(nova_janela, bg="white")
        scrollbar = ttk.Scrollbar(nova_janela, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="white")

        scrollable_frame.bind(
            "<Configure>", lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Adicionando o cupom na tela
        cupom_label = tk.Label(scrollable_frame, text=cupom, font=("Courier", 12), bg="white", justify="left")
        cupom_label.pack(pady=10)

        # Adicionando a imagem (caso você tenha uma imagem do cupom ou um logotipo, você pode usá-la aqui)
        try:
            imagem = Image.open(r"C:\DESN2025V1\DESN20252V1\Programação de apps\python\tk\image.webp")
            imagem = imagem.resize((200, 100))  # Redimensionar imagem
            img_tk = ImageTk.PhotoImage(imagem)
            label_imagem = tk.Label(scrollable_frame, image=img_tk, bg="white")
            label_imagem.image = img_tk  # Necessário para manter uma referência à imagem
            label_imagem.pack(side=tk.LEFT, padx=20)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar a imagem: {e}")

        # Fechando o pedido e retornando ao login
        tk.Button(scrollable_frame, text="Fechar", command=self.voltar_login).pack(pady=10)

    def voltar_login(self):
        self.root.destroy()
        abrir_login()

# Função de inicialização do sistema
def main():
    abrir_login()

if __name__ == "__main__":
    main()
