# Importa a biblioteca Tkinter, usada para criar janelas e interfaces gráficas
import tkinter as tk

# Cria a janela principal do programa
janela = tk.Tk()

# Define o título que aparece na barra superior da janela
janela.title("inicio jornada")

# Define o tamanho da janela: largura x altura
janela.geometry('400x250')

# Define a cor de fundo da janela
janela.configure(bg='#e8f4ff')

# Esta função será executada quando o botão for clicado
def iniciar_jornada():
    # Altera o texto do Label depois do clique
    mensagem.config(text='Você iniciou sua jornada Tkinter!')

    # Altera a cor do texto depois do clique
    mensagem.config(fg='#0b6b3a')

# Cria um texto principal dentro da janela
titulo = tk.Label(
    janela,
    text="Treino de tkinter",
    font=("Arial", 18, "Bold"),
    bg="#e8f4ff",
    fg="#1f2937"
)

# Coloca o título na tela com espaço vertical
titulo.pack(pady=20)

# Cria uma mensagem inicial
mensagem = tk.Label(
    janela,
    text="Clique no botão para começar",
    font=("Arial",12),
    bg='#e5f1ff',
    fg='#374151'
)

# Coloca a mensagem na tela
mensagem.pack(pady=10)

# Cria um botão
botao = tk.Button(
    janela,
    text='Começar',
    font=("Arial", 12, "bold"),
    bg="#2563eb",
    fg='white',
    activebackground='white',
    command=iniciar_jornada
)

# Coloca o botão na tela
botao.pack(pady=20)

# Mantém a janela aberta esperando ações do usuário
janela.mainloop()