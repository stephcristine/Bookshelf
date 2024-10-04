from pymongo import MongoClient
from bson.objectid import ObjectId

class Model:
  def __init__(self):
    connection_string = "mongodb://localhost:27017/"
    client = MongoClient(connection_string)
    self.db_connection = client["BookShelf"]

    self.collection_usuarios = self.db_connection.get_collection("Usuario")
    self.collection_livros = self.db_connection.get_collection("Livro")

  def cadastrarUsuario(self, usuario):
    usuario = {
      "nome": usuario[0],
      "email": usuario[1],
      "senha": usuario[2]
    }
    return self.collection_usuarios.insert_one(usuario)

  def mostrarUsuario(self, id):
    dadosUsuario = self.collection_usuarios.find_one({"_id": ObjectId(id)})
    return dadosUsuario

  def editarUsuario(self, id, novosDados):
    atualizar = {}

    if novosDados[0] != '':
        atualizar['nome'] = novosDados[0]
    if novosDados[1] != '':
        atualizar['email'] = novosDados[1]
    if novosDados[2] != '':
        atualizar['senha'] = novosDados[2]

    if atualizar:
      resultado = self.collection_usuarios.update_one({"_id": id}, {"$set": atualizar})

      if resultado.modified_count > 0:
        return True
      else:
        return False
    else:
        return False

  def deletarUsuario(self, id):
    return self.collection_usuarios.delete_one({"_id": id})

  def logar(self, dadosLogin):
    dadosLogin = {
      "nome": dadosLogin[0],
      "senha": dadosLogin[1]
    }
    return self.collection_usuarios.find_one(dadosLogin)
    
  def cadastrarLivro(self, livro):
    livro = {
      "nome": livro[0],
      "autor": livro[1],
      "editora": livro[2],
      "lista": livro[3],
      "inicio": livro[4],
      "final": livro[5]
    }
    return self.collection_livros.insert_one(livro)

  def editarLivro(self, novosDados, id):
    atualizar = {}

    if novosDados[0] != '':
      atualizar['nome'] = novosDados[0]
    if novosDados[1] != '':
      atualizar['autor'] = novosDados[1]
    if novosDados[2] != '':
      atualizar['editora'] = novosDados[2]
    if novosDados[3] == 'nao-lidos' or novosDados[3] == 'andamento' or novosDados[3] == 'lidos':
      atualizar['lista'] = novosDados[3]
    if novosDados[4] != '':
      atualizar['inicio'] = novosDados[4]
    if novosDados[5] != '':
      atualizar['final'] = novosDados[5]

    if atualizar:
      resultado = self.collection_livros.update_one({"_id": id}, {"$set": atualizar})

      if resultado.modified_count > 0:
        return True
      else:
        return False
    else:
        return False

  def buscarLivro(self, livro):
    return self.collection_livros.find_one({"nome": livro})

  def editarLista(self, dados):
    if dados[1] == 'nao-lidos' or dados[1] == 'andamento' or dados[1] == 'lidos':
      return self.collection_livros.update_one({"nome": dados[0]}, {"$set": {"lista": dados[1]}})
  
  def buscarListas(self, lista):
    resultado = self.collection_livros.find({"lista": lista})
    livros = []
    for livro in resultado:
      livros.append(livro)
    return livros

  def verificarUsuario(self, usuario):
    if usuario[0] == '' or usuario[1] == '' or usuario[2] == '':
      return False
    else:
      return True

  def usuarioExiste(self, usuario):
    return self.collection_usuarios.find_one({"nome": usuario})
