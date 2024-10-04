import sys
import tkinter as tk
from Controller import Controller
from Model import Model

from View.Pag_Landing import *
from View.Pag_Cadastro_Livro import *
from View.Pag_Cadastro_Usuario import *
from View.Pag_Inicial import *
from View.Pag_Login import *
from View.Pag_Usuario import *
from View.Pag_Editar_Usuario import *
from View.Pag_Editar_Livro import *

class View():
  def __init__(self):
    self.root = tk.Tk()
    self.root.title("BookShelf")
    self.root.geometry("800x600")
    self.root.configure(bg="#e9e2db")

    self.model = Model()
    self.controller = Controller(self, self.model)

    self.container = tk.Frame(self.root)
    self.container.pack(fill="both", expand=True)

    self.frame1 = Pag_Landing(self.container, self.controller)
    self.frame2 = Pag_Login(self.container, self.controller)
    self.frame3 = Pag_Cadastro_Usuario(self.container, self.controller)
    self.frame4 = Pag_Inicial(self.container, self.controller)
    self.frame5 = Pag_Usuario(self.container, self.controller)
    self.frame6 = Pag_Cadastro_Livro(self.container, self.controller)
    self.frame7 = Pag_Editar_Usuario(self.container, self.controller)
    self.frame8 = Pag_Editar_Livro(self.container, self.controller)

    self.frame1.root.grid(row=0, column=0, sticky='nsew')
    self.frame2.root.grid(row=0, column=0, sticky='nsew')
    self.frame3.root.grid(row=0, column=0, sticky='nsew')
    self.frame4.root.grid(row=0, column=0, sticky='nsew')
    self.frame5.root.grid(row=0, column=0, sticky='nsew')
    self.frame6.root.grid(row=0, column=0, sticky='nsew')
    self.frame7.root.grid(row=0, column=0, sticky='nsew')
    self.frame8.root.grid(row=0, column=0, sticky='nsew')
    
    self.frame1.root.tkraise()

    self.root.bind('<Escape>', self.close)

    self.root.mainloop()

  def close(self, evento=None):
    sys.exit()

View()
