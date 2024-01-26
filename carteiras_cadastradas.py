def carteiras_cadastradas(): 
  from PyPDF2 import PdfReader
  import sqlite3
  import tkinter as tk
  from tkinter import ttk
  from relatorio_financeiro import relatorio_financeiro
  from editar_pdf import editar_pdf
  

  # Conecta ao banco de dados SQLite
  conn = sqlite3.connect('banco_carteirinhas.db')
  cursor = conn.cursor()

   # Criando interface gráfica
  window = tk.Tk()
  window.title("Infromações cadastradas")
  window.geometry("570x250")

  # Cria um frame com uma borda
  frame = tk.Frame(window, borderwidth=2, relief="groove")
  frame.place(x=15, y=15, width=520, height=200)

  # Tabela para exibir os dados
  colunas = ('Nome', 'CPF', 'Matricula','Unidade','Data', 'Validade', 'Acesso', 'Curso')
  tabela = ttk.Treeview(
      frame, columns=colunas,
      show='headings')  # Adiciona a tabela ao frame em vez da janela
  for coluna in colunas:
    tabela.heading(coluna, text=coluna)
    tabela.column('Nome')
    tabela.column('CPF')
    tabela.column('Matricula')
    tabela.column('Unidade')
    tabela.column('Data')
    tabela.column('Validade')
    tabela.column('Acesso')
    tabela.column('Curso')
    tabela.pack(fill="both",
                expand=True)  # Use pack em vez de place para preencher o frame

    # Botão para carregar os dados do banco de dados
  def carregar_dados():
    cursor.execute("SELECT * FROM carteiras")
    rows = cursor.fetchall()

    # Limpa a tabela
    for i in tabela.get_children():
      tabela.delete(i)

    for row in rows:
      tabela.insert('', 'end', values=row)

  carregar_button = tk.Button(window, text="Carregar", command=carregar_dados)
  carregar_button.pack()
  carregar_button.place(x=15, y=220)

    # Criando botão para fechar janela
  def fechar_janela():
    window.destroy()

  fechar_button = tk.Button(window, text="Fechar", command=fechar_janela)
  fechar_button.pack()
  fechar_button.place(x=320, y=220)


  window.mainloop()

  # Fecha a conexão com o banco de dados
  conn.close()


