import tkinter as tk

# 1. Criar a janela principal
app = tk.Tk()

# 2. Configuracoes da janela
app.title("my first app in tkinter")
app.geometry("400x300")

# 3. Adicionar widgets
label = tk.Label(app, text="Olá, tkinter!")
label.pak()

# 4. Iniciar o loop da interface 
app.mainloop()