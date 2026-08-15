import tkinter as tk

app = tk.Tk()
app.title("Hello, World!")
app.geometry("300x150")

label = tk.Label(app, text="Hello World!!!", font=("Arial", 20))
label.pack(padx=40)

app.mainloop()