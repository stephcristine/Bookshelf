import tkinter as tk
from tkinter import messagebox

class Pag_Inicial():
  def __init__(self, container, controller):
    self.root = tk.Frame(container)
    self.controller = controller

    self.fundoCabecalho = tk.Frame(self.root, bg="#453827")
    self.fundoCabecalho.pack(side="top", fill="x")

    self.botaoUsuario = tk.Button(self.fundoCabecalho, text="Minha biblioteca", bg="#725139", fg="white",
                                  padx=20, pady=10, cursor="hand2", relief="flat", font=("Arial", 10), command=self.controller.showFrame5)
    self.botaoUsuario.pack(side="right", pady=30, padx=30)

    self.cadastrarLivro = tk.Button(self.fundoCabecalho, text="Cadastrar livro", bg="#725139", fg="white",
                                    padx=20, pady=10, cursor="hand2", relief="flat", font=("Arial", 10), command=self.controller.showFrame6)
    self.cadastrarLivro.pack(side="right")

    self.retangulo = tk.Frame(self.root, bg="#685f5a")
    self.retangulo.pack(pady=50)

    self.texto = tk.Label(self.retangulo, text="Comece a adicionar livros a sua\nbiblioteca",
                          bg="#685f5a", font=("Arial", 25))
    self.texto.pack(side="top", pady=50, padx=100)

    self.inputPesquisa = tk.Frame(self.root, bg="#e9e2db")
    self.inputPesquisa.pack(pady=10)

    self.entryPesquisa = tk.Entry(self.inputPesquisa, width=60, font=("Arial", 13))
    self.entryPesquisa.pack(side="left", padx=5)

    self.buttonPesquisar = tk.Button(self.inputPesquisa, text="Pesquisar")
    self.buttonPesquisar["command"] = self.buscarLivro
    self.buttonPesquisar.pack(side="left")

    self.quadradoLivro = None

  def buscarLivro(self):
    self.livro = self.entryPesquisa.get()
    self.resultado = self.controller.procurandoLivro(self.livro)
    self.mensagem()

  def mensagem(self):
    if self.resultado:
      messagebox.showinfo("Sucesso", "Livro encontrado")
      self.dadosLivro()
    else:
      messagebox.showerror("Erro", "Livro não encontrado")
      self.quadradoLivro.pack_forget()

  def dadosLivro(self):
    if self.quadradoLivro:
      self.quadradoLivro.pack_forget()

    self.quadradoLivro = tk.Frame(self.root, bg="#453827", padx=60)
    self.quadradoLivro.pack(pady=10)

    self.labelLivro = tk.Label(self.quadradoLivro, text=f"Livro: {self.resultado['nome']},     Autor: {self.resultado['autor']},     Editora: {self.resultado['editora']}", fg="white", bg="#453827", font=("Arial", 18))
    self.labelLivro.pack(pady=10)

    self.quadradoOpcoes = tk.Frame(self.quadradoLivro, bg="#453827")
    self.quadradoOpcoes.pack(pady=10)

    self.radioValue = tk.StringVar(value=0)

    self.radioUm = tk.Radiobutton(self.quadradoOpcoes, text='Livros não lidos', bg="#453827", font=("Arial", 13), fg="white", selectcolor="black",
                                  variable=self.radioValue, value='nao-lidos')
    self.radioUm.pack(side="left", padx=10)

    self.radioDois = tk.Radiobutton(self.quadradoOpcoes, text='Livros em andamento', bg="#453827", font=("Arial", 13), fg="white", selectcolor="black",
                                    variable=self.radioValue, value='andamento')
    self.radioDois.pack(side="left", padx=10)

    self.radioTres = tk.Radiobutton(self.quadradoOpcoes, text='Livros lidos', bg="#453827", font=("Arial", 13), fg="white", selectcolor="black",
                                    variable=self.radioValue, value='lidos')
    self.radioTres.pack(side="left", padx=10)

    botaoAdicionar = tk.Button(self.quadradoLivro, text="Adicionar à lista", command=self.adicionarLivro)
    botaoAdicionar.pack(pady=10)
      

  def adicionarLivro(self):
    self.dados = (self.resultado['nome'], self.radioValue.get())
    self.adicionado = self.controller.editandoLista(self.dados)
    if self.adicionado:
      messagebox.showinfo("Sucesso", "Livro adicionado à lista!")
      self.quadradoLivro.pack_forget()
    else:
      messagebox.showerror("Erro", "Erro ao adicionar livro à lista")
      self.quadradoLivro.pack_forget()
