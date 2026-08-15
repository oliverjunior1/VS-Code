# Importa a biblioteca Tkinter, usada para criar janelas e interfaces gráficas
import tkinter as tk

# Cria a janela principal do programa
janela = tk.Tk()

# Define o título que aparece na barra superior da janela
janela.title("Meu Primeiro App Tkinter, sou Joaquim")

# Define o tamanho da janela: largura x altura
janela.geometry("500x300")

# Define a cor de fundo da janela
janela.configure(bg="#37648e")


# Esta função será executada quando o botão for clicado
def iniciar_jornada():
    # Altera o texto do Label depois do clique
    mensagem.config(text="Você iniciou sua jornada Tkinter, Joaquim!")

    # Altera a cor do texto depois do clique
    mensagem.config(fg="#0b6b3a")


# Cria um texto principal dentro da janela
titulo = tk.Label(
    janela,                         # Diz que o texto pertence à janela principal
    text="Treino de Tkinter",        # Texto que será exibido
    font=("Arial", 18, "bold"),      # Fonte, tamanho e estilo
    bg="#e8f4ff",                    # Cor de fundo igual à janela
    fg="#1f2937"                     # Cor do texto
)

# Coloca o título na tela com espaço vertical
titulo.pack(pady=20)


# Cria uma mensagem inicial
mensagem = tk.Label(
    janela,                         # O Label pertence à janela
    text="Clique no botão para começar",  # Texto inicial
    font=("Arial", 12),             # Fonte e tamanho
    bg="#e8f4ff",                   # Cor de fundo
    fg="#374151"                    # Cor do texto
)

# Coloca a mensagem na tela
mensagem.pack(pady=10)


# Cria um botão
botao = tk.Button(
    janela,                         # O botão pertence à janela
    text="Vai lá",                 # Texto que aparece no botão
    font=("Arial", 12, "bold"),     # Fonte do botão
    bg="#2563eb",                   # Cor de fundo do botão
    fg="white",                     # Cor do texto do botão
    activebackground="#1d4ed8",     # Cor do botão enquanto está sendo clicado
    activeforeground="white",       # Cor do texto enquanto está sendo clicado
    command=iniciar_jornada         # Função chamada ao clicar no botão
)

# Coloca o botão na tela
botao.pack(pady=20)


# Mantém a janela aberta esperando ações do usuário
janela.mainloop()