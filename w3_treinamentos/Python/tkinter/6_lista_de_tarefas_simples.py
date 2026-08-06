# Importa o Tkinter, biblioteca usada para criar janelas e interfaces gráficas
import tkinter as tk

# Cria a janela principal do programa
janela = tk.Tk()

# Define o título da janela
janela.title("Lista de Tarefas em tkinter")

# Define o tamanho da janela
janela.geometry("450x400")

# Define a cor de fundo da janela
janela.configure(bg="#2045c0")


# Esta função pega o texto digitado e adiciona na lista
def adicionar_tarefa():
    # Pega o texto que o usuário digitou no campo de entrada
    tarefa = campo_tarefa.get()

    # Verifica se o campo está vazio
    if tarefa == "":
        # Mostra uma mensagem de aviso
        mensagem.config(text="Digite uma tarefa antes de adicionar.")
    else:
        # Adiciona a tarefa dentro da Listbox
        lista_tarefas.insert(tk.END, tarefa)

        # Apaga o texto do campo de entrada depois de adicionar
        campo_tarefa.delete(0, tk.END)

        # Mostra uma mensagem de sucesso
        mensagem.config(text="Tarefa adicionada com sucesso!")


# Esta função remove a tarefa que estiver selecionada na lista
def remover_tarefa():
    # Pega o índice da tarefa selecionada
    selecionada = lista_tarefas.curselection()

    # Verifica se nenhuma tarefa foi selecionada
    if not selecionada:
        # Mostra uma mensagem de aviso
        mensagem.config(text="Selecione uma tarefa para remover.")
    else:
        # Remove a tarefa selecionada
        lista_tarefas.delete(selecionada)

        # Mostra uma mensagem de sucesso
        mensagem.config(text="Tarefa removida.")


# Cria o título principal da tela
titulo = tk.Label(
    janela,
    text="Minha Lista de Tarefas",
    font=("Arial", 18, "bold"),
    bg="#eef2ff",
    fg="#3730a3"
)

# Coloca o título na janela
titulo.pack(pady=15)

# Mostra o XP atual da cobrinha
xp_label = tk.Label(
    janela,
    text="XP da cobrinha: 6/100",
    font=("Arial", 10, "bold"),
    bg="#eef2ff",
    fg="#065f46"
)

# Coloca o XP na janela
xp_label.pack()

# Cria o campo onde o usuário digita uma tarefa
campo_tarefa = tk.Entry(
    janela,
    font=("Arial", 12),
    width=35
)

# Coloca o campo na janela
campo_tarefa.pack(pady=10)

# Cria o botão que adiciona tarefas
botao_adicionar = tk.Button(
    janela,
    text="Criar uma tarefa",
    font=("Arial", 11, "bold"),
    bg="#4f46e5",
    fg="white",
    activebackground="#4338ca",
    activeforeground="white",
    command=adicionar_tarefa
)

# Coloca o botão de adicionar na janela
botao_adicionar.pack(pady=5)

# Cria a lista visual onde as tarefas aparecem
lista_tarefas = tk.Listbox(
    janela,
    font=("Arial", 12),
    width=35,
    height=8,
)

# Coloca a lista na janela
lista_tarefas.pack(pady=10)

# Cria o botão que remove tarefas
botao_remover = tk.Button(
    janela,
    text="Excluir Tarefa Selecionada",
    font=("Arial", 11, "bold"),
    bg="#dc2626",
    fg="white",
    activebackground="#b91c1c",
    activeforeground="white",
    command=remover_tarefa
)

# Coloca o botão de remover na janela
botao_remover.pack(pady=5)

# Cria uma mensagem para avisos e confirmações
mensagem = tk.Label(
    janela,
    text="Digite uma tarefa e clique em adicionar.",
    font=("Arial", 10),
    bg="#eef2ff",
    fg="#1f2937"
)

# Coloca a mensagem na janela
mensagem.pack(pady=5)

# Mantém a janela aberta
janela.mainloop()