import tkinter as tk

janela = tk.Tk()

janela.title("Cadastro")
janela.geometry("400x250")

tk.Label(janela, text="Nome:").grid(row=0, column=0, padx=10, pady=10)

nome = tk.Entry(janela)

nome.grid(row=0, column=1, padx=10, pady=10)

tk.Label(janela, text='Idade:').grid(row=1, column=0, padx=10, pady=10)

idade = tk.Entry(janela)

idade.grid(row=1, column=1, padx=10, pady=10)

janela.mainloop()