import tkinter as tk

janela = tk.Tk()

tk.Label(janela, text="Nome:").grid(row=0, column=0)

nome = tk.Entry(janela)

nome.grid(row=0, column=1)

janela.mainloop()