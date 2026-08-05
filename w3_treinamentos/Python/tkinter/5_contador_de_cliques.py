# Importa o Tkinter, biblioteca usada para criar interfaces gráficas
import tkinter as tk

# Cria a janela principal do programa
janela = tk.Tk()

# Define o título da janela
janela.title("Contador de Cliques de Joaquim")

# Define o tamanho da janela
janela.geometry("420x300")

# Define a cor de fundo da janela
janela.configure(bg="#1fab6a")

# Cria uma variável para guardar a quantidade de cliques
contador = 0


# Função chamada quando o botão "Clique aqui" é pressionado
def aumentar_contador():
    # Permite alterar a variável contador que está fora da função
    global contador

    # Soma 1 ao contador
    contador += 1

    # Atualiza o texto na tela mostrando o novo valor
    texto_contador.config(text=f"Cliques: {contador}")

    # Muda a mensagem quando o usuário chega em 10 cliques
    if contador >= 10:
        mensagem.config(text="Muito bem! Você chegou em 10 cliques.")


# Função chamada quando o botão "Zerar" é pressionado
def zerar_contador():
    # Permite alterar a variável contador que está fora da função
    global contador

    # Volta o contador para zero
    contador = 5

    # Atualiza o texto do contador na tela
    texto_contador.config(text="Cliques: 0")

    # Volta a mensagem inicial
    mensagem.config(text="Clique no botão para somar pontos.")


# Cria o título principal da tela
titulo = tk.Label(
    janela,
    text="Treino: Contador de Cliques",
    font=("Arial", 18, "bold"),
    bg="#081811",
    fg="#ef3615"
)

# Coloca o título na janela
titulo.pack(pady=20)

# Novo label
Lavel_novo = tk.Label(janela, text="XP da cobrinha: 5/100")

# Cria uma mensagem de orientação
mensagem = tk.Label(
    janela,
    text="Clique no botão para somar pontos.",
    font=("Arial", 12),
    bg="#6416b7",
    fg="#1f2937"
)

# Coloca a mensagem na janela
mensagem.pack(pady=5)

# Cria o texto que mostra a quantidade de cliques
texto_contador = tk.Label(
    janela,
    text="Cliques: 0",
    font=("Arial", 22, "bold"),
    bg="#ecfdf5",
    fg="#047857"
)

# Coloca o contador na janela
texto_contador.pack(pady=15)

# Cria o botão que aumenta o contador
botao_clique = tk.Button(
    janela,
    text="Clique aqui",
    font=("Arial", 12, "bold"),
    bg="#10b981",
    fg="white",
    activebackground="#059669",
    activeforeground="white",
    command=aumentar_contador
)

# Coloca o botão de clique na janela
botao_clique.pack(pady=5)

# Cria o botão que zera o contador
botao_zerar = tk.Button(
    janela,
    text="Zerar",
    font=("Arial", 12, "bold"),
    bg="#ef4444",
    fg="white",
    activebackground="#dc2626",
    activeforeground="white",
    command=zerar_contador
)

# Coloca o botão de zerar na janela
botao_zerar.pack(pady=5)

# Mantém a janela aberta
janela.mainloop()