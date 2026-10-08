import tkinter as tk

janela = tk.Tk()

janela.title("Sistema de estudos")
janela.geometry("600x400")

texto = tk.Label(janela, text="Olá, mundo!")
texto.pack()

janela.mainloop()