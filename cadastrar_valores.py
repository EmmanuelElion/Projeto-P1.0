# Arquvio que muda o "CADASTRAR VALORES"
def cadastrar_valores():
  import sqlite3
  import tkinter as tk
  from tkinter import ttk
  from tkcalendar import DateEntry
  from datetime import datetime


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

  # Criando a interface gráfica 
  window = tk.Tk()
  window.title("Cadastro valores")
  window.geometry("350x200")

  # Criação do botão do tipo rádio
  tipo = tk.StringVar()
  tipo.set("A receber")

  rb1 = tk.Radiobutton(window, text="A pagar", variable=tipo, value="A pagar")
  rb1.pack()
  rb1.place(x=15, y=15)

  rb2 = tk.Radiobutton(window, text="A receber", variable=tipo, value="A receber")
  rb2.pack()
  rb2.place(x=90, y=15)


  # Criação do input de nome
  nome_label = tk.Label(window, text="Nome:")
  nome_label.pack()
  nome_label.place(x=15, y=40)
  nome_entry = tk.Entry(window)
  nome_entry.pack()
  nome_entry.place(x=15, y=60)

  # Criação do input de descrição
  descricao_label = tk.Label(window, text="Descrição:")
  descricao_label.pack()
  descricao_label.place(x=15, y=90)
  descricao_entry = tk.Entry(window)
  descricao_entry.pack()
  descricao_entry.place(x=15, y=110)

  # Criação do input de data de vencimento
  data_label = tk.Label(window, text="Data:")
  data_label.pack()
  data_label.place(x=200, y=40)
  
  # Definição das datas mínima e máxima
  mindate = datetime(2024, 1, 1)
  maxdate = datetime(2035, 12, 31)
  data_entry = DateEntry(window, mindate=mindate, maxdate=maxdate)
  data_entry.pack()
  data_entry.place(x=200, y=60)

  # Criação do input de valor
  valor_label = tk.Label(window, text="Valor:")
  valor_label.pack()
  valor_label.place(x= 200,y= 90 )
  valor_entry = tk.Entry(window)
  valor_entry.pack()
  valor_entry.place(x= 200, y= 110, width=115, height=20)

  # Criando botão para fechar janela 
  def fechar_janela():
      window.destroy()
  # Criação do botão de fechar janela
  fechar_button = tk.Button(window, text="Fechar", command=fechar_janela)
  fechar_button.pack()
  fechar_button.place(x=250, y=160)
  
  # Criação do label de status
  status_label = tk.Label(window, text="", fg="red")
  status_label.pack()
  status_label.place(x= 85 , y= 130)
  
  # Criando a função para salvar dados 
  def salvar_dados():
    # Configurando para caso o nome estiver em branco ou o valor ai ele avisar e não aceitar
    nome = nome_entry.get()
    valor = valor_entry.get()
    if len(valor) <= 0:
      status_label.config(text="O valor não foi inserido")
      return
    if len(nome) <= 0:
      status_label.config(text="O Titulo não foi inserido")
      return
    
    cursor.execute('''
      INSERT INTO minha_tabela VALUES (?, ?, ?, ?, ?)
      ''', (tipo.get(), nome_entry.get(), descricao_entry.get(), data_entry.get(), float(valor_entry.get())))
    conn.commit()

    # Avisa que as informações foram salvas com sucesso 
    status_label.config(text="Dados salvos com sucesso!")
    
    
    # Limpa todos os campos de entrada
    nome_entry.delete(0, 'end')
    data_entry.delete(0, 'end')
    descricao_entry.delete(0, 'end')
    valor_entry.delete(0, 'end')

  
  # Criação do botão de Salvar dados   
  salvar_button = tk.Button(window, text="Salvar", command=salvar_dados)
  salvar_button.pack()
  salvar_button.place(x=15, y=160)

 
 
  window.mainloop()

  # Fecha a conexão com o banco de dados
  conn.close()
  

if __name__ == "__main__":
  # Este código só será executado se cadastrar_valores.py for executado diretament
  cadastrar_valores()
