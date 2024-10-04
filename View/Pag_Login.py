import sys
import tkinter as tk
from tkinter import messagebox

class Pag_Login():
  def __init__(self, container, controller):
    self.root = tk.Frame(container)
    self.controller = controller

    self.retangulo = tk.Frame(self.root, bg="#545454")
    self.retangulo.pack(expand=True)

    self.Label = tk.Label(self.retangulo, width=20, text='Login', bg = "#545454", font=("Arial", 25))
    self.Label.pack(pady=40, padx=100)

    self.labelNome = tk.Label(self.retangulo, width=20, text='Nome', bg = "#545454", font=("Arial", 15))
    self.labelNome.pack()

    self.entryNome = tk.Entry(self.retangulo, width=60)
    self.entryNome.pack(pady=10, padx=10)

    self.labelSenha = tk.Label(self.retangulo, width=20, text='Senha ', bg = "#545454", font=("Arial", 15))
    self.labelSenha.pack(pady=10, padx=10)

    self.entrySenha = tk.Entry(self.retangulo, width=60)
    self.entrySenha.pack()

    self.button_submit = tk.Button(self.retangulo, text="Entrar", padx=20, pady=10, bg="black", 
                                   fg="white", cursor="hand2", relief="flat", font=("Arial", 13))
    self.button_submit["command"] = self.buscarLogin
    self.button_submit.pack(pady=50, padx=100)

  def buscarLogin(self):
    dados = (self.entryNome.get(), self.entrySenha.get())
    self.resultado = self.controller.logando(dados)
    self.mensagem()

  def mensagem (self):
    if self.resultado:
      messagebox.showinfo("Sucesso", "Login realizado com sucesso!") 
      self.controller.showFrame4()
    else:
      messagebox.showerror("Erro", "Nome ou senha incorretos.")
