from pathlib import Path

while True:
    option_country = int(input("Type 1 to brazilian food, 2 to italian food, 3 to spanish food and 4 to exit: "))
    match option_country:
        case 1:
            option_food = int(input("Put 1 to feijoada, 2 to moqueca capixaba and 3 to pão de queijo: "))
            match option_food:
                case 1:
                    x = open("C:\\Users\\Olive\\OneDrive\\Área de Trabalho\\Receita\\Comida Brasileira\\Feijoada.txt")
                    print(x)
                case 2:
                    x = open("C:\\Users\\Olive\\OneDrive\\Área de Trabalho\\Receita\\Comida Brasileira\\Moqueca capixaba.txt")
                    print(x)
                case 3:
                    x = open("C:\\Users\\Olive\\OneDrive\\Área de Trabalho\\Receita\\Comida Brasileira\\Pão de queijo.txt")
                case 4:
                    break

        
        case 2:
            option_food = int(input("Put 1 lasagna, 2 to risotto, 3 to Tiramisu, and 4 to exit: "))
            match option_food:
                case 1:
                    x = open("C:\\Users\\Olive\\OneDrive\\Área de Trabalho\\Receita\\Comida Italiana\\LASAGNA ALLA BOLOGNESE.txt")
                    print(x)
                case 2:
                    x = open("C:\\Users\\Olive\\OneDrive\\Área de Trabalho\\Receita\\Comida Italiana\\RISOTTO ALLA MILANESE.txt")
                    print(x)
                case 3:
                    x = open("C:\\Users\\Olive\\OneDrive\\Área de Trabalho\\Receita\\Comida Italiana\\TIRAMISU.txt")
                case 4:
                    break

        
        case 3:
            option_food = int(input("Put 1 to feijoada, 2 to moqueca capixaba and 3 to pão de queijo: "))
            match option_food:
                case 1:
                    x = open("C:\\Users\\Olive\\OneDrive\\Área de Trabalho\\Receita\\Comida Espanhola\\CHURROS COM CHOCOLATE.txt")
                    print(x)
                case 2:
                    x = open("C:\\Users\\Olive\\OneDrive\\Área de Trabalho\\Receita\\Comida Espanhola\\PAELLA VALENCIANA.txt")
                    print(x)
                case 3:
                    x = open("C:\\Users\\Olive\\OneDrive\\Área de Trabalho\\Receita\Comida Espanhola\\TORTILLA ESPAÑOLA.txt")
                case 4:
                    break

        case 4:
            break

        
