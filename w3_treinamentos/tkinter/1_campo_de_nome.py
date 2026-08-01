# Importa a biblioteca Tkinter para criar janelas e componentes visuais
import tkinter as tk

# Cria a janela principal do aplicativo
app = tk.Tk()

# Define o título da janela
app.title("Campo de Nome")

# Define o tamanho da janela
app.geometry('450x300')

# Define a cor de fundo da janela
app.configure(bg='#dbeafe')

# Esta função será chamada quando o botão for clicado
def mostrar_saudacao():
    # Pega o texto digitado dentro do campo de entrada
    nome = campo_nome.get()

    # Verifica se o usuário digitou alguma coisa
    if nome == "":
        # Mostra uma mensagem caso o campo esteja vazio
        resultado.config(text='Digite seu nome primeiro.')
    else:
        # Mostra uma saudação personalizada usando o nome digitado
        resultado.config(text=f"Olá, {nome}! Bem-vindo ao Tkinter.")


# Cria o título principal da tela
titulo = tk.Label(
    app,
    text="Treino com Entry",
    font=("Arial", 20, 'bold'),
    bg='#dbeafe',
    fg='#1e368a'
)

# Exibe o título na janela
titulo.pack(pady=20)

# Cria um texto explicando o que o usuário deve fazer
instrucao = tk.Label(
    app,
    text="Digite seu nome: ",
    font=("Arial", 12),
    bg='#dbeafe',
    fg='#1f2937'
)

# Exibe a instrução na janela
instrucao.pack()

# Cria um campo de entrada para o usuário digitar
campo_nome = tk.Entry(
    app,
    font=('Arial', 12),
    width=30
)

# Exibe o campo de entrada na janela
campo_nome.pack(pady=10)

# Cria um botão que chama a função mostrar_saudacao
botao = tk.Button(
    app,
    text='Mostrar Saudação',
    font=('Arial', 12, 'bold'),
    bg='#2563eb',
    fg='white',
    activebackground='white',
    command=mostrar_saudacao
)

# Exibe o botão na janela
resultado = tk.Label(
    app,
    text='',
    font=('Arial', 12, 'bold'),
    bg='#dbeafe',
    fg='#0f766e'
)

# Exibe o resultado na janela
resultado.pack(pady=15)

# Mantém a janela aberta
app.mainloop()