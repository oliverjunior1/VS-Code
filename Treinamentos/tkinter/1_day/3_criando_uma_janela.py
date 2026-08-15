# import tkinter as tk
# app = tk.Tk()
# label = tk.Label(app, text="Jesus is the light!").pack()
# app.geometry("400x400")
# app.mainloop()

import tkinter as tk

# Criar a janela principal
app = tk.Tk()

# Personalizações
app.title("Janela personalizada")
app.geometry("500x350")
app.configure(bg="#1e1e1e") # fundo escuro
app.resizable(False, False) # Impede redimensionamento

# Texto dentro da janela
label = tk.Label(
    app,
    text="Bem vindo ao tkinter!",
    font=("Arial", 18),
    fg="white",
    bg="#1e1e1e"
)


label.pack(pady=20)

app.mainloop()