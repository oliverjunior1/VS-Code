import tkinter as tk

def sum_number():
    first_number = int(number.get())
    second_number = int(number2.get())

    mensagem.config(text=f"the sum of the numers is {first_number+second_number}")

janela = tk.Tk()

janela.title("Sum calculator")
janela.geometry("500x300")

number = tk.Entry(janela, text="Put the first number: ")
number2 = tk.Entry(janela, text="Put the second number: ")
mensagem = tk.Label(janela, text="")
Resultado = tk.Label(janela, text="Resultado:")
button_message = tk.Button(janela, command=sum_number, text="Calcular")


number.pack()
number2.pack()
button_message.pack()
Resultado.pack()
mensagem.pack()


janela.mainloop()