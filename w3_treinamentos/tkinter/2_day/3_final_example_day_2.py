import tkinter as tk

app = tk.Tk()
app.title('Day 2 - Tkinter')
app.geometry('300x200')

label = tk.Label(app, text="Estrutura básica funcionando!")
label.pack(pady=20)

app.mainloop()