import customtkinter as ctk

class BasicApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Basic CustomTkinter App")
        self.geometry("400x300")

        self.label = ctk.CTkLabel(self, text="Hello, CustomTkinter!")
        self.label.pack(pady=20)

        self.button = ctk.CTkButton(self, text="Click Me", command=self.on_button_click)
        self.button.pack(pady=10)

    def on_button_click(self):
        self.label.configure(text="Button Clicked!")
        preco_final = preco * (1 - descontos[cupom])
# Saída
        print(f"{preco_final:.2f}")
        self.label.configure(text=f"Preço final: {preco_final:.2f}")
if __name__ == "__main__":
    app = BasicApp()
    app.mainloop()