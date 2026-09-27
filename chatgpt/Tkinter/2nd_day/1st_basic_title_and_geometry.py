import tkinter as tk

janela = tk.Tk()

janela.title("Sistema")
janela.geometry("500x500")
titulo = tk.Label(janela, text="Sistema de Cadastro")
titulo.pack()
nome = tk.Entry(janela)
nome.pack()

janela.mainloop()