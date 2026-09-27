import tkinter as tk

janela = tk.Tk()

janela.title("Cadastro")
janela.geometry("500x300")

titulo = tk.Label(
    janela,
    text="Cadastro de Clientes",
    font=("Arial",20)
).pack()

janela.mainloop()