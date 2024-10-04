import tkinter as tk

class Pag_Landing:
  def __init__(self, container, controller):
    self.root = tk.Frame(container)
    self.controller = controller
        
    self.cabecalho = tk.Frame(self.root, bg="#453827")
    self.cabecalho.pack(side="top", fill="x")

    self.botaoLogin = tk.Button(self.cabecalho, text="Login", bg ="#725139", fg= "white",
                                padx=20, pady=10, cursor="hand2", relief="flat", font=("Arial", 10), command=self.controller.showFrame2)
    self.botaoLogin.pack(side="right", pady=30, padx=30)

    self.retangulo = tk.Frame(self.root, bg="#685f5a")
    self.retangulo.pack(expand=True)

    self.texto = tk.Label(self.retangulo, text="Bem-vindo ao Bookshelf.\nUm lugar feito pra te ajudar a organizar\nsuas leituras.",
                          bg="#685f5a", font=("Arial", 25))
    self.texto.pack(pady=50, padx=100)

    self.botaoCadastro = tk.Button(self.retangulo, text="Faça seu cadastro", bg ="#725139", fg= "white",
                                   padx=20, pady=10, cursor="hand2", relief="flat", font=("Arial", 15), command=self.controller.showFrame3)
    self.botaoCadastro.pack(pady=30)
