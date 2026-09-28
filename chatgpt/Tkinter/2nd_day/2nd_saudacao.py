import tkinter as tk

def saudar():
    nome_digitado = nome.get()

    print("Olá,", nome_digitado)

janela = tk.Tk()

janela.title("Saudação")
janela.geometry('400x250')

titulo = tk.Label(
    janela,
    text="Digite seu nome"
)

titulo.pack()

nome = tk.Entry(janela)

nome.pack()

botao = tk.Button(
    janela,
    text="Saudar",
    command=saudar
)

botao.pack()

janela.mainloop()