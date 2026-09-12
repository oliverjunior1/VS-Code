import tkinter as tk

janela = tk.Tk()

janela.title("Cadastro")
janela.geometry("500x300")

nome = tk.Entry(janela).pack()

janela.mainloop()