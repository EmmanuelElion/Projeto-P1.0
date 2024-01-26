def carteira_estudante(): 
  import sqlite3
  import tkinter as tk
  from tkinter import ttk
  from tkcalendar import DateEntry

  # Conecta ao banco de dados SQLite
  conn = sqlite3.connect('banco_carteirinhas.db')
  cursor = conn.cursor()

  # Cria a tabela se ela não existir
  cursor.execute('''
  CREATE TABLE IF NOT EXISTS carteiras(
      unidade TEXT,
      nome TEXT,
      matricula INT,
      validade DATE,
      curso TEXT,
      acesso INT,
      cpf INT
  )
  ''')
  window = tk.Tk()
  window.title("Cadastro Carteirinha")
  window.geometry("500x350")

  # Criação do input de nome
  nome_label = tk.Label(window, text="Nome:")
  nome_label.pack()
  # nome_label.place(x=15, y=50)
  nome_entry = tk.Entry(window)
  nome_entry.pack()
  # nome_entry.place(x=15, y=70)

  # Criação do input de CPF
  cpf_label = tk.Label(window, text="CPF:")
  cpf_label.pack()
  # cpf_label.place(x=15, y=90)
  cpf_entry = tk.Entry(window)
  cpf_entry.pack()
  # cpf_entry.place(x=15, y=110)

  # Criação do input de data de vencimento
  data_label = tk.Label(window, text="Data Vencimento:")
  data_label.pack()
  # data_label.place(x=200, y=50)
  data_entry = DateEntry(window)
  data_entry.pack()
  # data_entry.place(x=200, y=70)

  # Criação do input de Matricula
  matricula_label = tk.Label(window, text="Matricula:")
  matricula_label.pack()
  # matricula_label.place(x=15, y=90)
  matricula_entry = tk.Entry(window)
  matricula_entry.pack()
  # matricula_entry.place(x=15, y=110)

  # Criação do input de Unidade
  unidade_label = tk.Label(window, text="Unidade:")
  unidade_label.pack()
  # unidade_label.place(x=15, y=90)
  unidade_entry = tk.Entry(window)
  unidade_entry.pack()
  # unidade_entry.place(x=15, y=110)

  # Criação do input de Acesso
  acesso_label = tk.Label(window, text="Acesso:")
  acesso_label.pack()
  # acesso_label.place(x=15, y=90)
  acesso_entry = tk.Entry(window)
  acesso_entry.pack()
  # acesso_entry.place(x=15, y=110)

  # Criação do input de Curso
  curso_label = tk.Label(window, text="Curso:")
  curso_label.pack()
  #curso_label.place(x=15, y=90)
  curso_entry = tk.Entry(window)
  curso_entry.pack()
  #curso_entry.place(x=15, y=110)


  
  # Botão para salvar os dados no banco de dados
  def salvar_dados():
    cursor.execute('''
        INSERT INTO carteiras VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (nome_entry.get(), cpf_entry.get(), data_entry.get(), matricula_entry.get(), unidade_entry.get(), acesso_entry.get(), curso_entry.get()))
    conn.commit()

  salvar_button = tk.Button(window, text="Salvar", command=salvar_dados)
  salvar_button.pack()
  # salvar_button.place(x=15, y=150)

  # Criando botão para fechar janela 
  def fechar_janela():
    window.destroy()

  fechar_button = tk.Button(window, text="Fechar", command=fechar_janela)
  fechar_button.pack()
  # fechar_button.place(x=85, y=150)


  window.mainloop()

  # Fecha a conexão com o banco de dados
  conn.close()


if __name__ == "__main__":
  # Este código só será executado se cadastrar_valores.py for executado diretament
  carteira_estudante()
