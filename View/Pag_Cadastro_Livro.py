import tkinter as tk
from tkinter import messagebox

class Pag_Cadastro_Livro():
  def __init__(self, container, controller):
    self.root = tk.Frame(container)
    self.controller = controller

    self.retangulo = tk.Frame(self.root, bg="#545454")
    self.retangulo.pack(expand=True)

    self.labelCadastro = tk.Label(self.retangulo, width=20, text='Cadastro de livros', bg = "#545454", font=("Arial", 25))
    self.labelCadastro.pack(pady=20, padx=100)

    self.labelNome = tk.Label(self.retangulo, width=20, text='Nome:', bg = "#545454", font=("Arial", 15))
    self.labelNome.pack()

    self.entryNome = tk.Entry(self.retangulo, width=60)
    self.entryNome.pack(pady=5, padx=10)

    self.labelAutor = tk.Label(self.retangulo, width=20, text='Autor:', bg = "#545454", font=("Arial", 15))
    self.labelAutor.pack(pady=5, padx=10)

    self.entryAutor = tk.Entry(self.retangulo, width=60)
    self.entryAutor.pack(pady=5, padx=10)

    self.labelEditora = tk.Label(self.retangulo, width=20, text='Editora:', bg = "#545454", font=("Arial", 15))
    self.labelEditora.pack(pady=5, padx=10)

    self.entryEditora = tk.Entry(self.retangulo, width=60)
    self.entryEditora.pack(pady=5, padx=10)

    self.labelInicio = tk.Label(self.retangulo, width=20, text='Inicio Leitura', bg = "#545454", font=("Arial", 15))
    self.labelInicio.pack(pady=5, padx=10)

    self.entryInicio = tk.Entry(self.retangulo, width=60)
    self.entryInicio.pack(pady=5, padx=10)

    self.labelFinal = tk.Label(self.retangulo, width=20, text='Final Leitura', bg = "#545454", font=("Arial", 15))
    self.labelFinal.pack(pady=5, padx=10)

    self.entryFinal = tk.Entry(self.retangulo, width=60)
    self.entryFinal.pack(pady=5, padx=10)

    self.radioValue = tk.StringVar(value=0)

    self.radioUm = tk.Radiobutton(self.retangulo, text='Adicionar a lista de livros não lidos', width=40, bg="#545454", font=("Arial", 13),
                                  variable=self.radioValue, value='nao-lidos', anchor=tk.W)
    self.radioUm.pack()

    self.radioDois = tk.Radiobutton(self.retangulo, text='Adicionar a lista de livros em andamento', width=40, bg="#545454", font=("Arial", 13),
                                    variable=self.radioValue, value='andamento', anchor=tk.W)
    self.radioDois.pack()

    self.radioTres = tk.Radiobutton(self.retangulo, text='Adicionar a lista de livros lidos', width=40, bg="#545454", font=("Arial", 13),
                                    variable=self.radioValue, value='lidos', anchor=tk.W)
    self.radioTres.pack()
    
    self.button_submit = tk.Button(self.retangulo, text="Cadastrar", padx=20, pady=10, bg= "black", fg="white", cursor="hand2", relief="flat", font=("Arial", 13))
    self.button_submit["command"] = self.enviar
    self.button_submit.pack(pady=20, padx=100)

  def enviar(self):
    dadosLivro = (self.entryNome.get(), self.entryAutor.get(), self.entryEditora.get(), self.radioValue.get(), self.entryInicio.get(), self.entryFinal.get())
    self.resultado = self.controller.cadastrandoLivro(dadosLivro)
    self.mensagem()

  def mensagem(self):
    if self.resultado:
      messagebox.showinfo('Informação', "Livro cadastrado com sucesso")
      self.controller.showFrame4()
    else:
      messagebox.showerror('Erro', 'Falha ao cadastrar Livro.') 
      print(self.resultado)
