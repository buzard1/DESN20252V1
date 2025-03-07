import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk  

class AcaiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Açaí 🍧")
        self.root.configure(bg="gray")
        self.root.geometry("250x500")  # Tamanho da janela

        main_frame = tk.Frame(root)
        main_frame.pack(fill="both", expand=True)

# Criando o Canvas dentro do Frame principal
        self.canvas = tk.Canvas(main_frame)
        self.canvas.pack(side="left", fill="both", expand=True)

# Criando a Scrollbar e associando ao Canvas
        self.scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")

# Criando um Frame dentro do Canvas (área rolável)
        self.scrollable_frame = tk.Frame(self.canvas)

# Configuração do Canvas para redimensionar corretamente o conteúdo
        self.scrollable_frame.bind(
    "<Configure>", lambda e: self.canvas.configure(
        scrollregion=self.canvas.bbox("all")
    )
)

# Criando uma janela dentro do Canvas que conterá o frame rolável
        self.canvas_window = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

# Associando a Scrollbar ao Canvas
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

# Garantindo que o Frame não se expanda horizontalmente ao adicionar elementos
        self.scrollable_frame.update_idletasks()
        self.canvas.config(width=self.scrollable_frame.winfo_reqwidth())

# Permitir rolagem com a roda do mouse
        def _on_mouse_wheel(event):
            self.canvas.yview_scroll(-1 * (event.delta // 120), "units")

# Associar rolagem do mouse ao Canvas
            self.canvas.bind_all("<MouseWheel>", _on_mouse_wheel)   

        # Lista de pedidos
        self.pedidos = []

        # Variáveis
        self.tamanho_var = tk.StringVar(value="Pequeno")
        self.pagamento_var = tk.StringVar(value="Dinheiro")
        self.pre_pronto_var = tk.StringVar(value="Nenhum")

        # Dicionários de preços
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
            "Leite Condensado": 2.00,
            "Granola": 1.50,
            "Banana": 2.50,
            "Paçoca": 3.00,
            "Morango": 3.50,
            "Nutella": 5.00,
            "Mel": 2.50,
            "Ovomaltine": 3.00,
            "Chantilly": 2.00
        }

        self.acompanhamentos = {item: tk.BooleanVar() for item in self.precos_acompanhamentos.keys()}

        # Interface
        self.criar_interface()

    def criar_interface(self):
        """Cria a interface do sistema de pedidos."""
        tk.Label(self.scrollable_frame, text="Escolha o tamanho do copo:", fg='white', bg='black').pack(pady=5, fill="x")
        self.criar_radio_buttons_tamanhos()

        tk.Label(self.scrollable_frame, text="Escolha um açaí pré-pronto (Opcional):", fg='white', bg='black').pack(pady=5, fill="x")
        self.criar_radio_buttons_acais()

        tk.Label(self.scrollable_frame, text="Escolha os acompanhamentos:", fg='white', bg='black').pack(pady=5, fill="x")
        self.criar_check_buttons_acompanhamentos()

        tk.Label(self.scrollable_frame, text="Forma de pagamento:", fg='white', bg='green').pack(pady=2)
        self.criar_radio_buttons_pagamento()

        self.valor_total_label = tk.Label(self.scrollable_frame, text="Total: R$0.00", fg="green", font=("Arial", 12, "bold"))
        self.valor_total_label.pack()

        tk.Button(self.scrollable_frame, text="Adicionar Açai", command=self.montar_acai).pack()
        tk.Button(self.scrollable_frame, text="Finalizar Pedido", command=self.finalizar_pedido, fg="red").pack()

    def criar_radio_buttons_tamanhos(self):
        """Cria os radio buttons para selecionar o tamanho do açaí."""
        for tamanho, (preco, ml) in self.precos_tamanhos.items():
            tk.Radiobutton(self.scrollable_frame, text=f"{tamanho} - R${preco:.2f} ({ml})", 
                           variable=self.tamanho_var, value=tamanho, command=self.atualizar_total).pack()

    def criar_radio_buttons_acais(self):
        """Cria os radio buttons para selecionar um açaí pré-pronto."""
        for nome, preco in self.precos_pre_prontos.items():
            frame = tk.Frame(self.scrollable_frame)
            frame.pack()
            tk.Radiobutton(frame, text=f"{nome} - R${preco:.2f}", 
                           variable=self.pre_pronto_var, value=nome, command=self.atualizar_total).pack(side=tk.LEFT)
            tk.Button(frame, text="?", command=lambda n=nome: self.mostrar_descricao(n)).pack(side=tk.LEFT)

        tk.Radiobutton(self.scrollable_frame, text="Nenhum", variable=self.pre_pronto_var, value="Nenhum", command=self.atualizar_total).pack()

    def criar_check_buttons_acompanhamentos(self):
        """Cria os check buttons para selecionar os acompanhamentos."""
        for item, var in self.acompanhamentos.items():
            tk.Checkbutton(self.scrollable_frame, text=f"{item} - R${self.precos_acompanhamentos[item]:.2f}", variable=var, command=self.atualizar_total).pack()

    def criar_radio_buttons_pagamento(self):
        """Cria os radio buttons para selecionar a forma de pagamento."""
        for pagamento in ["Dinheiro", "Cartão", "Pix"]:
            tk.Radiobutton(self.scrollable_frame, text=pagamento, variable=self.pagamento_var, value=pagamento).pack()

    def atualizar_total(self):
        """Atualiza o valor total do pedido com base nas escolhas feitas."""
        total = 0
        tamanho = self.tamanho_var.get()
        pre_pronto = self.pre_pronto_var.get()

        if pre_pronto != "Nenhum":
            # Se for um açaí pré-pronto, pega apenas o preço dele e adiciona o extra do tamanho
            total += self.precos_pre_prontos[pre_pronto] + self.adicional_tamanho[tamanho]
        else:
            # Se for um açaí personalizado, pega o preço do tamanho e adiciona acompanhamentos
            total += self.precos_tamanhos[tamanho][0]
        for item, var in self.acompanhamentos.items():
            if var.get():
                total += self.precos_acompanhamentos[item]

        self.valor_total_label.config(text=f"Total: R${total:.2f}")
    
    def montar_acai(self):
        """Montar o açaí e adicioná-lo ao pedido."""
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
        """Exibe a descrição do açaí pré-pronto selecionado."""
        descricao = self.descricao_pre_prontos.get(nome, "Descrição não disponível.")
        messagebox.showinfo(nome, descricao)

    def finalizar_pedido(self):
        """Finaliza o pedido e gera o cupom fiscal com a imagem ao lado e a barra de rolagem."""
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
        nova_janela.geometry("600x400")

        # Criando o Canvas com a barra de rolagem
        canvas = tk.Canvas(nova_janela)
        scrollbar = ttk.Scrollbar(nova_janela, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>", lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Adicionar o texto do cupom no canvas
        label_cupom = tk.Label(scrollable_frame, text=cupom, justify=tk.LEFT, font=("Arial", 10))
        label_cupom.pack(side=tk.LEFT, padx=20)

        # Carregar e exibir a imagem
        try:
            imagem = Image.open(r"C:\DESN2025V1\DESN20252V1\Programação de apps\python\tk\image.webp")
            imagem = imagem.resize((400, 300))  # Redimensionar imagem
            img_tk = ImageTk.PhotoImage(imagem)
            label_imagem = tk.Label(scrollable_frame, image=img_tk)
            label_imagem.image = img_tk  # Necessário para manter uma referência à imagem
            label_imagem.pack(side=tk.RIGHT, padx=20)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar a imagem: {e}")

        nova_janela.mainloop()

root = tk.Tk()
app = AcaiApp(root)
root.mainloop()
