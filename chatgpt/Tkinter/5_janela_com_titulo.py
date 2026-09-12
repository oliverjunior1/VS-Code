import tkinter as tk

janela = tk.Tk()

janela.title("Cadastro de Clientes")
janela.geometry("500x300")

titulo = tk.Label(
    janela,
    text="Sistema de Cadastro de Clientes"
)

janela.mainloop()