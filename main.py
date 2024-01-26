import sqlite3
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry  # Certifique-se de instalar esta biblioteca usando pip
from cadastrar_valores import cadastrar_valores
from valores_cadastrados import valores_cadastrados
from carteira_estudante import carteira_estudante
from carteiras_cadastradas import carteiras_cadastradas

# Conecta ao banco de dados SQLite
conn = sqlite3.connect('banco_dados/meu_banco_de_dados.db')
cursor = conn.cursor()

# Cria a tabela se ela não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS minha_tabela (
    tipo TEXT,
    nome TEXT,
    descricao TEXT,
    data TEXT,
    valor REAL
)
''')

# Conecta ao banco de dados SQLite
conn = sqlite3.connect('banco_dados/banco_carteirinhas.db')
cursor = conn.cursor()

# Cria a tabela se ela não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS carteiras (
    unidade TEXT,
    nome TEXT,
    matricula INT,
    validade DATE,
    curso TEXT,
    acesso INT,
    cpf INT
)
''')


# blackbox ai 


def cadastrar_vr():
  cadastrar_valores()
  
def valores_cd():
  valores_cadastrados()
    
def cadastrar_atividades():
  pass  

def atividades_cadastradas():
  pass

def cart_estudante():
  carteira_estudante()

def cart_cadastradas(): 
  carteiras_cadastradas()


# INTERFACE PRINCIPAL 
root = tk.Tk()
root.title("Menu")
root.geometry("375x190")

botao1 = tk.Button(root, text="Cadastrar valores", command=cadastrar_vr)
botao1.pack()
botao1.place(x=15, y=20, height=30, width=150)

botao2 = tk.Button(root, text="Valores cadastrados", command=valores_cd)
botao2.pack()
botao2.place(x=175, y=20, height=30, width=150)


botao3 = tk.Button(root, text="Cadastrar atividades", command=cadastrar_atividades)
botao3.pack()
botao3.place(x=15, y=60, height=30, width=150)

botao4 = tk.Button(root, text="Atividades cadastradas", command=atividades_cadastradas)
botao4.pack()
botao4.place(x=175, y=60, height=30, width=150)

botao5 = tk.Button(root, text="Carteira estudante", command=cart_estudante)
botao5.pack()
botao5.place(x=15, y=100, height=30, width=150)

botao6 = tk.Button(root, text="Carteiras Cadastradas", command=cart_cadastradas)
botao6.pack()
botao6.place(x=175, y=100, height=30, width=150)

root.mainloop()
