import tkinter as tk

def login_page():
    user = user_input.get()
    password = user_password.get()

    if user == "admin" and password == '1234':
        label_message.config(text="Correct password") 
    else:
        label_message.config(text="Incorrect Password or user") 

janela = tk.Tk()
janela.title("Login screen")
janela.geometry("500x300")

user_text = tk.Label(janela, text="Usuário")
user_input = tk.Entry(janela)
password_text = tk.Label(janela, text="Senha")
user_password = tk.Entry(janela)
entering = tk.Button(janela, text="ENTRAR", command=login_page)
label_message = tk.Label(janela, text='')

user_text.pack()
user_input.pack()
password_text.pack()
user_password.pack()
entering.pack()
label_message.pack()

janela.mainloop()