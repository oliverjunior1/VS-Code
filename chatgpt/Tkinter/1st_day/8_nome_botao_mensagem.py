import tkinter as tk


def cumprimentar():
    nome_digitado = nome.get()

    mensagem.config(
        text=f"Olá, {nome_digitado}!"
    )


janela = tk.Tk()

janela.title("Saudação")
janela.geometry("500x300")

titulo = tk.Label(
    janela,
    text="Digite seu nome:"
)

titulo.pack()

nome = tk.Entry(janela)

nome.pack()

botao = tk.Button(
    janela,
    text="Cumprimentar",
    command=cumprimentar
)

botao.pack()

mensagem = tk.Label(
    janela,
    text=""
)

mensagem.pack()

janela.mainloop()