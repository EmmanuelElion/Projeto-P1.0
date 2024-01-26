def relatorio_financeiro():
  import sqlite3
  import tkinter as tk
  from tkinter import ttk
  from reportlab.pdfgen import canvas
  from reportlab.lib.pagesizes import letter

  # Conecta ao banco de dados SQLite
  conn = sqlite3.connect('banco_dados/meu_banco_de_dados.db')
  cursor = conn.cursor()

  
  
  
  # Função para extrair dados do banco de dados
  def extrair_dados():
    cursor.execute("SELECT * FROM minha_tabela")
    return cursor.fetchall()

  # Função fazendo a soma dos valores cadastrados 
  def soma_valores():
    # Executa a consulta SQL para somar todos os valores na coluna "valor"
    cursor.execute("SELECT SUM(valor) FROM minha_tabela")

    # Obtém o resultado
    soma = cursor.fetchone()[0]
    return soma

  # Função de somar os valores "A PAGAR"
  def soma_valores_a_pagar():
    cursor.execute("SELECT SUM(valor) FROM minha_tabela WHERE tipo = 'A pagar'")
    soma_apagar = cursor.fetchone()[0]
    return soma_apagar

  # Função de somar os valores "A RECEBER"
  def soma_valores_a_receber():
    cursor.execute("SELECT SUM(valor) FROM minha_tabela WHERE tipo = 'A receber'")
    soma_areceber = cursor.fetchone()[0]
    return soma_areceber
    
  
  # Função para criar o e incluir informações no PDF 
  def create_pdf(dados):
    c = canvas.Canvas("relatorio/relatorio_financeiro.pdf", pagesize=letter)
    width, height = letter
    c.drawString(250, height - 50, "Bem-vindo ao Relatório Financeiro")
    c.drawString(100, height - 80, "TIPO ")
    c.drawString(160, height - 80, "NOME ")
    c.drawString(220, height - 80, "DESCRIÇÃO ")
    c.drawString(400, height - 80, "DATA ")
    c.drawString(500, height - 80, "VALOR ")
    

    # Adiciona os dados ao PDF
    for i, linha in enumerate(dados):
      tipo, nome, descricao, data, valor = linha
      y = height - 100 - (i * 20)
      c.drawString(100, y,str(tipo)) #  Nome: {nome}, Descricao: {descricao}, Data: {data}, Valor: {valor}")
      c.drawString(160, y,str(nome))
      c.drawString(220, y,str(descricao))
      c.drawString(400, y,str(data))
      c.drawString(500, y,str(valor))

    
    # Adiciona o total 20 unidades abaixo do último dado inserido
    y = y - 30
    c.drawString(400, y, "Total= R$ ")
    c.drawString(455, y, str(soma_valores()))

    # Adicionando o resultado da soma dos valores a pagar
    c.drawString(400, y - 30, "Total a pagar= R$ ")
    c.drawString(500, y - 30, str(soma_valores_a_pagar()))

    # Adicionando o resultado da soma dos valores a receber
    c.drawString(400, y - 60, "Total a receber= R$ ")
    c.drawString(510, y - 60, str(soma_valores_a_receber()))
    
    
    c.save()

  
  
    
  
  # Extrai os dados e cria o PDF
  dados = extrair_dados()
  create_pdf(dados)
