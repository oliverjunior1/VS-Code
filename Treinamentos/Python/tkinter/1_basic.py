import tkinter as tk
from tkinter import ttk

# Função do botão
def saudar():
    nome = entrada_nome.get()
    if nome:
        messagebox.showinfo("Saudação", f"Olá, `{nome}!")
    else:
        messagebox.showarning("Aviso", "Digite seu nome.")

# Janela principal
janela = tk.Tk()
janela.title("Aplicação Tkinter")
janela.geometry("300x200")

# Widgets
label = tk.Label(janela, text="Digite seu nome:")
label.pack(pady=10)

entrada_nome = tk.Entry(janela)
entrada_nome.pack(pady=5)

botao = tk.Button(janela, text="Saudar", command=saudar)
botao.pack(pady=10)

# Loop principal
janela.mainloop()