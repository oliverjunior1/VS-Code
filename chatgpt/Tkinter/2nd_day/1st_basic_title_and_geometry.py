import tkinter as tk

janela = tk.Tk()

janela.title("Sistema")
janela.geometry("500x500")
titulo = tk.Label(janela, text="Sistema de Cadastro")
titulo.pack()
nome = tk.Entry(janela)
button = tk.Button("Enviar")
nome.pack()
texto = nome.get()
label1 = tk.Label(janela, text=texto)
label1.pack()

janela.mainloop()