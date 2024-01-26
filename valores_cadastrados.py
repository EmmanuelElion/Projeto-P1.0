def valores_cadastrados():
  from PyPDF2 import PdfReader
  import sqlite3
  import tkinter as tk
  from tkinter import ttk
  from relatorio_financeiro import relatorio_financeiro
  from editar_pdf import editar_pdf

  # Conecta ao banco de dados SQLite
  conn = sqlite3.connect('banco_dados/meu_banco_de_dados.db')
  cursor = conn.cursor()

  # Criando interface gráfica
  window = tk.Tk()
  window.title("Valores Cadastrados ")
  window.geometry("570x250")
  
  # Adicionando texto "Valores cadastrados"
  text_vl_cadastrados = tk.Label(window, text="Valores cadastrados:", font=("Arial", 12))
  text_vl_cadastrados.pack()
  text_vl_cadastrados.place(x=10, y=5 ) 
  # Cria um frame com uma borda
  frame = tk.Frame(window, borderwidth=2, relief="groove")
  frame.place(x=15, y=30, width=545, height=175)

  # Tabela para exibir os dados
  colunas = ('Tipo', 'Nome', 'Descrição', 'Data', 'Valor')
  tabela = ttk.Treeview(
    frame, columns=colunas,
    show='headings')  # Adiciona a tabela ao frame em vez da janela
  for coluna in colunas:
    tabela.heading(coluna, text=coluna)
    tabela.column('Tipo', width=70)
    tabela.column('Nome', width=150)
    tabela.column('Descrição', width=150)
    tabela.column('Data', width=75)
    tabela.column('Valor', width=75)
  tabela.pack(fill="both",
              expand=True)  # Use pack em vez de place para preencher o frame

  # Botão para carregar os dados do banco de dados
  def carregar_dados():
    cursor.execute("SELECT * FROM minha_tabela")
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

  # Label de status 
  status_label = tk.Label(window, text="", font=("Arial", 10), fg="red")
  status_label.pack()
  status_label.place(x=300, y=5)

 
  # Botão para gerar relatório
  def gerar_relatorio():
    relatorio_financeiro()
    # Avisa que as informações foram salvas com sucesso 
    status_label.config(text="Dados salvos com sucesso!")
    window.after(1000, lambda: status_label.config(text=""))
    window.after(1000, lambda: tabela.delete(*tabela.get_children()))
  
  gerar_relatorio_button = tk.Button(window,
                                     text="Gerar relatório",
                                     command=gerar_relatorio)
  gerar_relatorio_button.pack()
  gerar_relatorio_button.place(x=100, y=220)

  
  def edita_o_pdf():
    editar_pdf()

  editar_pdf_button = tk.Button(window, text="Editar PDF", command=editar_pdf)
  editar_pdf_button.pack()
  editar_pdf_button.place(x=220, y=220)

   
  window.mainloop()

  # Fecha a conexão com o banco de dados
  conn.close()
