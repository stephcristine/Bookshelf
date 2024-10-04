class Controller:
  def __init__(self, View, model):
    self.model = model
    self.view = View
    self.logado = None
    self.idLivro = None

  def cadastrandoUsuario(self, usuario):
   return self.model.cadastrarUsuario(usuario)
   
  def preenchendoDados(self, usuario):
    if self.model.verificarUsuario(usuario) == False:
      self.view.frame3.mensagem2()
      return False
    else:
      return True

  def verificandoUsuario(self, usuario):
    if self.model.usuarioExiste(usuario):
      self.view.frame3.mensagem3()
      return False
    else:
      return True

  def logando(self, dadosLogin):
    usuario = self.model.logar(dadosLogin)
    if usuario:
      self.logado = usuario
      return True
    else:
      return False

  def buscandoUsuario(self):
    return self.model.mostrarUsuario(self.logado["_id"])

  def editandoUsuario(self, novosDados):
    if self.logado:
      return self.model.editarUsuario(self.logado['_id'], novosDados)
    
  def deletandoUsuario(self):
    if self.logado:
      resultado = self.model.deletarUsuario(self.logado['_id'])
      if resultado.deleted_count > 0:
        self.logado = None
        return True
      else:
        return False

  def cadastrandoLivro(self, livro):
    return self.model.cadastrarLivro(livro)

  def procurandoLivro(self, livro):
    return self.model.buscarLivro(livro)
  
  def buscandoIdLivro(self, livro):
    existe = self.model.buscarLivro(livro['nome'])
    if existe:
      self.idLivro = existe
      return True
    else:
      return False
  
  def editandoLivro(self, novosDados):
    return self.model.editarLivro(novosDados, self.idLivro['_id'])

  def editandoLista(self, dados):
    return self.model.editarLista(dados)     

  def buscandoLista(self, lista):
    return self.model.buscarListas(lista)

  def showFrame1(self):
    self.view.frame1.root.tkraise()

  def showFrame2(self):
    self.view.frame2.root.tkraise()

  def showFrame3(self):
    self.view.frame3.root.tkraise()

  def showFrame4(self):
    self.view.frame4.root.tkraise()

  def showFrame5(self):
    self.view.frame5.root.tkraise()

  def showFrame6(self):
    self.view.frame6.root.tkraise()

  def showFrame7(self):
    self.view.frame7.root.tkraise()

  def showFrame8(self):
    self.view.frame8.root.tkraise()
