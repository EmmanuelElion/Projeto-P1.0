def editar_pdf():
  import sqlite3
  from reportlab.pdfgen import canvas
  from reportlab.lib.units import inch, cm
  from PIL import Image

  def preencher_pdf():
      # Conecta ao banco de dados SQLite
      conn = sqlite3.connect('meu_banco_de_dados.db')
      cursor = conn.cursor()

      # Consulta o primeiro valor da coluna "nome"
      cursor.execute("SELECT nome FROM minha_tabela LIMIT 1")
      nome = cursor.fetchone()[0]

      # Obtém as dimensões da imagem
      imagem = Image.open("pdf_a_editar/teste.png")
      largura, altura = imagem.size

      # Converte as dimensões de pixels para pontos (1 ponto = 1/72 polegadas)
      largura, altura = largura * inch / 72, altura * inch / 72

      # Cria um novo PDF com Reportlab com as dimensões da imagem
      c = canvas.Canvas("pdf_a_editar/teste_edicao.pdf", pagesize=(largura, altura))

      # Adiciona a imagem ao PDF, cobrindo a página inteira
      c.drawImage("pdf_a_editar/teste.png", 0, 0, width=largura, height=altura)

      # Adiciona o texto por cima da imagem
      c.setFont("Helvetica", 26)  # Define a fonte e o tamanho do texto
      c.setFillColorRGB(0, 0, 0)  # Define a cor do texto (vermelho)
      
      # Adicionando o nome
      c.drawString(50, 205, nome)  # Adiciona o texto ao PDF  # Adiciona o texto ao PDF

      # adicionando o 

      # Salva o PDF
      c.save()

      # Fecha a conexão com o banco de dados
      conn.close()

  preencher_pdf()

