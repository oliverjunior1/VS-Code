def fun_1(x):
    def fun_2(*args):
        print("###########################")
        x(*args)
        print("###########################")
    return fun_2

@fun_1
def greetings(*args):
    for arg in args:
        print(f"Hello {arg}")

greetings("Joao", "Maria")
