import os
from pathlib import Path
from os import system


my_path = Path.home("C:\\Users\\Olive\\OneDrive\\Área de Trabalho\\Receita")

def count_recipes(Path):
    counter = 0

    for txt in Path(path).glob("**/*.txt"):
        counter += 1

    return counter


def start():
    system('cls')
    print('*'*50 + "Welcome to the recipe administrator")
    print('*'*50)
    print(f"The recipes are in {my_path}")
    print(f'Total recipes: {count_recipes(my_path)}')

start()


#show start menu

menu = 0

if menu == 1:
    # show categories
    # choose category
    # show recipes
    # choose recipe
    # read recipe
    # go back to menu
    pass

elif menu == 2:
    # shows categorires
    # choose category
    # cerate new recipe
    # go back to menu
    pass

elif menu == 3:
    # create category
    # go back to menu
    pass

elif menu == 4:
    # show categories
    # choose category
    # show recipes
    # choose recipe
    # eliminate recipe
    # go back to menu
    pass

elif menu == 5:
    # show categories
    # choose category
    # eliminate category
    # go back to menu
    pass

elif menu == 6:
    # end program
    pass