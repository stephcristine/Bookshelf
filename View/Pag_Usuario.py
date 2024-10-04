import tkinter as tk

class Pag_Usuario():
  def __init__(self, container, controller):
    self.root = tk.Frame(container)
    self.controller = controller

    self.fundoCabecalho = tk.Frame(self.root, bg="#453827")
    self.fundoCabecalho.pack(side="top", fill="x")

    self.botaoMeusDados = tk.Button(self.fundoCabecalho, text="Meus dados", bg ="#725139", fg= "white",
                                 padx=20, pady=10, cursor="hand2", relief="flat", font=("Arial", 10), command=self.controller.showFrame7)
    self.botaoMeusDados.pack(side="right", pady= 30, padx=20)

    self.botaoInicio = tk.Button(self.fundoCabecalho, text="Início", bg ="#725139", fg= "white",
                                 padx=20, pady=10, cursor="hand2", relief="flat", font=("Arial", 10), command=self.controller.showFrame4)
    self.botaoInicio.pack(side="right")

    self.retanguloContainer = tk.Frame(self.root)
    self.retanguloContainer.pack(pady=30, padx=20)

    self.retangulo1 = tk.Frame(self.retanguloContainer, bg="#685f5a")
    self.retangulo1.pack(side="left", padx=13)

    self.texto = tk.Label(self.retangulo1, text="Livros não lidos", bg="#685f5a", font=("Arial", 15))
    self.texto.pack(pady=30, padx=40)

    self.botaoNaoLidos = tk.Button(self.retangulo1, text="Listar", bg ="#725139", fg= "white",
                                    padx=20, pady=10, cursor="hand2", relief="flat", font=("Arial", 10), command=self.listaNaoLidos)
    self.botaoNaoLidos.pack(pady=10)

    self.retangulo2 = tk.Frame(self.retanguloContainer, bg="#685f5a")
    self.retangulo2.pack(side="left", padx=13)

    self.texto = tk.Label(self.retangulo2, text="Livros em andamento", bg="#685f5a", font=("Arial", 15))
    self.texto.pack(pady=30, padx=30)

    self.botaoAndamento = tk.Button(self.retangulo2, text="Listar", bg ="#725139", fg= "white",
                                   padx=20, pady=10, cursor="hand2", relief="flat", font=("Arial", 10), command=self.listaAndamento)
    self.botaoAndamento.pack(pady=10)

    self.retangulo3 = tk.Frame(self.retanguloContainer, bg="#685f5a")
    self.retangulo3.pack(side="left", padx= 13)
  
    self.texto = tk.Label(self.retangulo3, text="Livros lidos", bg="#685f5a", font=("Arial", 15))
    self.texto.pack(pady=30, padx=50)
  
    self.botaoLidos = tk.Button(self.retangulo3, text="Listar", bg ="#725139", fg= "white",
                                    padx=20, pady=10, cursor="hand2", relief="flat", font=("Arial", 10), command=self.listaLidos)
    self.botaoLidos.pack(pady=10)

    self.quadradoLista = None
    self.quadradoListaDados = None


  def listaNaoLidos(self):
    lista = "nao-lidos"
    self.livros = self.controller.buscandoLista("nao-lidos")
    self.exibirLivros(lista)

  def listaAndamento(self):
    lista = "andamento"
    self.livros = self.controller.buscandoLista("andamento")
    self.exibirLivros(lista)

  def listaLidos(self):
    self.livros = self.controller.buscandoLista("lidos")
    lista = "lidos"
    self.exibirLivros(lista)

  def exibirLivros(self, lista):
    if self.quadradoLista:
      self.quadradoLista.pack_forget()
    if self.quadradoListaDados:
      self.quadradoListaDados.pack_forget()
    
    self.quadradoLista = tk.Frame(self.root, bg="#453827", padx=60)
    self.quadradoLista.pack(pady=10)

    self.labelTitulo = tk.Label(self.quadradoLista, text='Título', bg="#453827", fg="white", font=("Arial", 12))
    self.labelTitulo.grid(row=0, column=0, padx=20)

    self.labelAutor = tk.Label(self.quadradoLista, text='Autor', bg="#453827", fg="white", font=("Arial", 12))
    self.labelAutor.grid(row=0, column=1, padx=20)

    self.labelEditora = tk.Label(self.quadradoLista, text='Editora', bg="#453827", fg="white", font=("Arial", 12))
    self.labelEditora.grid(row=0, column=2, padx=20)

    if lista == "andamento" or lista == "lidos":
      self.labelInicio = tk.Label(self.quadradoLista, text='Iniciado', bg="#453827", fg="white", font=("Arial", 12))
      self.labelInicio.grid(row=0, column=3, padx=20)

    if lista == "lidos":
      self.labelFinal = tk.Label(self.quadradoLista, text='Finalizado', bg="#453827", fg="white", font=("Arial", 12))
      self.labelFinal.grid(row=0, column=4, padx=20)

    self.labelEditar = tk.Label(self.quadradoLista, text='Ação', bg="#453827", fg="white", font=("Arial", 12))
    if lista == "nao-lidos":
      self.labelEditar.grid(row=0, column=3, padx=20)
    elif lista == "andamento":
      self.labelEditar.grid(row=0, column=4, padx=20)
    else:
      self.labelEditar.grid(row=0, column=5, padx=20)

    self.quadradoListaDados = tk.Frame(self.root, bg="#453827", padx=60)
    self.quadradoListaDados.pack(pady=10)

    for i, livro in enumerate(self.livros):
      labelTituloLivro = tk.Label(self.quadradoListaDados, text=livro['nome'], bg="#453827", fg="white", font=("Arial", 10))
      labelTituloLivro.grid(row=i, column=0, padx=20)

      labelAutorLivro = tk.Label(self.quadradoListaDados, text=livro['autor'], bg="#453827", fg="white", font=("Arial", 10))
      labelAutorLivro.grid(row=i, column=1, padx=20)

      labelEditoraLivro = tk.Label(self.quadradoListaDados, text=livro['editora'], bg="#453827", fg="white", font=("Arial", 10))
      labelEditoraLivro.grid(row=i, column=2, padx=20)

      if lista == "andamento" or lista == "lidos":
        labelInicioLivro = tk.Label(self.quadradoListaDados, text=livro['inicio'], bg="#453827", fg="white", font=("Arial", 10))
        labelInicioLivro.grid(row=0, column=3, padx=20)

      if lista == "lidos":
        labelFinalLivro = tk.Label(self.quadradoListaDados, text=livro['final'], bg="#453827", fg="white", font=("Arial", 10))
        labelFinalLivro.grid(row=0, column=4, padx=20)

      botaoEditar = tk.Button(self.quadradoListaDados, text="Editar", bg="#725139", fg="white",
                              cursor="hand2", relief="flat", font=("Arial", 10),
                              command=lambda livro=livro: self.editar(livro))
      if lista == "nao-lidos":
        botaoEditar.grid(row=0, column=3, padx=20)
      elif lista == "andamento":
        botaoEditar.grid(row=0, column=4, padx=20)
      else:
        botaoEditar.grid(row=0, column=5, padx=20)

  def editar(self, livro):
    self.controller.buscandoIdLivro(livro)
    self.controller.showFrame8()
