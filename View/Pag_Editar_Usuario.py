import tkinter as tk
from tkinter import messagebox

class Pag_Editar_Usuario:
  def __init__(self, container, controller):
    self.root = tk.Frame(container)
    self.controller = controller

    self.retangulo = tk.Frame(self.root, bg="#545454")
    self.retangulo.pack(expand=True)

    self.labelEditarCadastro = tk.Label(self.retangulo, width=20, text='Editar', bg = "#545454", font=("Arial", 25))
    self.labelEditarCadastro.pack(pady=40, padx=100)

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

    self.button_submit = tk.Button(self.retangulo, text="Editar", padx=20, pady=10, bg= "black", fg="white", cursor="hand2",
                                    relief="flat", font=("Arial", 13), command= self.enviar)
    self.button_submit.pack(side="left",pady=40, padx=130)

    self.button_deletar = tk.Button(self.retangulo, text="Deletar", padx=20, pady=10, bg= "black", fg="white", cursor="hand2",
                                     relief="flat", font=("Arial", 13), command= self.deletar)
    self.button_deletar.pack(side="left",pady=40)

  def enviar(self):
    usuario = (self.entryNome.get(), self.entryEmail.get(), self.entrySenha.get())
    self.resultado = self.controller.editandoUsuario(usuario)
    self.mensagem()

  def deletar(self):
    self.deletado = self.controller.deletandoUsuario()
    self.mensagemDeletar()
  
  def mensagem(self):
    if self.resultado:
      messagebox.showinfo('Informação', "Usuário editado com sucesso.")
      self.controller.showFrame5()
    else:
      messagebox.showerror('Erro', 'Falha ao editar usuário.')    
  
  def mensagemDeletar(self):
    if self.deletado:
      messagebox.showinfo('Informação', "Usuário deletado com sucesso.")
      self.controller.showFrame1()
    else:
      messagebox.showerror('Erro', 'Falha ao deletar usuário.')

