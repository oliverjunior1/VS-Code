import tkinter as tk


def cadastrar():

    nome_digitado = nome.get()
    idade_digitada = idade.get()

    if nome_digitado == "":
        resultado.config(
            text="Digite o nome."
        )
        return

    if idade_digitada == "":
        resultado.config(
            text="Digite a idade."
        )
        return

    try:

        idade_numero = int(idade_digitada)

    except ValueError:

        resultado.config(
            text="A idade precisa ser um número."
        )

        return

    resultado.config(
        text=f"Cadastro realizado: {nome_digitado}, "
             f"{idade_numero} anos."
    )


janela = tk.Tk()

janela.title("Sistema de Cadastro")
janela.geometry("450x300")


tk.Label(
    janela,
    text="Nome:"
).grid(
    row=0,
    column=0,
    padx=10,
    pady=10
)


nome = tk.Entry(janela)

nome.grid(
    row=0,
    column=1,
    padx=10,
    pady=10
)


tk.Label(
    janela,
    text="Idade:"
).grid(
    row=1,
    column=0,
    padx=10,
    pady=10
)


idade = tk.Entry(janela)

idade.grid(
    row=1,
    column=1,
    padx=10,
    pady=10
)


botao = tk.Button(
    janela,
    text="Cadastrar",
    command=cadastrar
)

botao.grid(
    row=2,
    column=0,
    columnspan=2,
    pady=20
)


resultado = tk.Label(
    janela,
    text=""
)

resultado.grid(
    row=3,
    column=0,
    columnspan=2
)


janela.mainloop()