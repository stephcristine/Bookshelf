import tkinter as tk
from tkinter import messagebox

class Pag_Cadastro_Usuario:
  def __init__(self, container, controller):
    self.root = tk.Frame(container)
    self.controller = controller

    self.retangulo = tk.Frame(self.root, bg="#545454")
    self.retangulo.pack(expand=True)

    self.labelCadastro = tk.Label(self.retangulo, width=20, text='Cadastro', bg = "#545454", font=("Arial", 25))
    self.labelCadastro.pack(pady=40, padx=100)

    self.labelNome = tk.Label(self.retangulo, width=20, text='Nome:', bg = "#545454", font=("Arial", 15))
    self.labelNome.pack()

    self.entryNome = tk.Entry(self.retangulo, width=60)
    self.entryNome.pack(pady=10, padx=10)

    self.labelEmail = tk.Label(self.retangulo, width=20, text='E-mail:', bg = "#545454", font=("Arial", 15))
    self.labelEmail.pack(pady=10, padx=10)

    self.entryEmail = tk.Entry(self.retangulo, width=60)
    self.entryEmail.pack(pady=10, padx=10)

    self.labelSenha = tk.Label(self.retangulo, width=20, text='Senha:', bg = "#545454", font=("Arial", 15))
    self.labelSenha.pack(pady=10, padx=10)

    self.entrySenha = tk.Entry(self.retangulo, width=60)
    self.entrySenha.pack(pady=10, padx=10)

    self.button_submit = tk.Button(self.retangulo, text="Cadastrar", padx=20, pady=10, bg= "black", fg="white", cursor="hand2", relief="flat", font=("Arial", 13))
    self.button_submit["command"] = self.verificado
    self.button_submit.pack(pady=40, padx=100)

  def verificado(self):
    self.usuario = (self.entryNome.get(), self.entryEmail.get(), self.entrySenha.get())
    self.preechido = self.controller.preenchendoDados(self.usuario)
    self.usuarioExiste = self.controller.verificandoUsuario(self.usuario[0])
    if self.preechido or self.usuarioExiste:
      self.cadastrar()
  
  def cadastrar(self):
    self.resultado = self.controller.cadastrandoUsuario(self.usuario)
    self.mensagem()
  
  def mensagem(self):
    if self.resultado:
      messagebox.showinfo('Informação', "Usuário cadastrado com sucesso")
      self.controller.showFrame2()
    else:
      messagebox.showerror('Erro', 'Falha ao cadastrar usuário.') 
    
  def mensagem2(self):
    messagebox.showerror('Erro', 'Preencha todos os campos') 

  def mensagem3(self):
    messagebox.showerror('Erro', 'Usuário já existe') 