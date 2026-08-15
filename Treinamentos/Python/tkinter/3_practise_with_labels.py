import tkinter as tk

# Criando a janela
janela = tk.Tk()
janela.title("Informações Pessoais")
janela.geometry("450x350")
janela.configure(bg='white')

# Título
titulo = tk.Label(
    janela,
    text="INFORMAÇÕES PESSOAIS",
    font=("Arial", 18, 'bold'),
    fg='blue',
    bg='white'
)
titulo.pack(pady=15)

# Informações
dados = [
    ('Nome:', 'Joaquim Junior'),
    ('Idade', '42 anos'),
    ('Cidade', 'Brasília'),
    ('Profissão', "Empregado da Caixa"),
    ("Curso:", "Engenharia da Computação"),
    ("Email", "joaquim@email.com"),
]

# Criando os Labels
for campo, valor in dados:
    frame = tk.Frame(janela, bg="white")
    frame.pack(anchor='w', padx=20, pady=4)

    lbl_campo = tk.Label(
        frame,
        text=campo,
        font=('Arial', 12, 'bold'),
        fg='black',
        bg='white',
        width=12,
        anchor='w'
    )

    lbl_campo.pack(side='left')

    lbl_valor = tk.Label(
        frame,
        text=valor,
        font=('Arial',12),
        fg='gray30',
        bg='white'
    )
    lbl_valor.pack(side='left')

janela.mainloop()