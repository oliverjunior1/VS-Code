import os
from pathlib import Path
from os import system

my_path = Path("C:/Users/Olive/OneDrive/Área de Trabalho/Receita")

def count_recipes(path: Path):
    counter = 0
    for txt in path.glob("**/*.txt"):
        counter += 1
    return counter

def start():
    system('cls')
    print('*'*50 + "Welcome to the recipe administrator")
    print('*'*50)
    print(f"The recipes are in {my_path}")
    print(f'Total recipes: {count_recipes(my_path)}')

    menu_choice = 'x'
    while not menu_choice.isnumeric() or int(menu_choice) not in range(1,7):
        print("Choose an option.")
        print('''
        [1] - Read recipe
        [2] - Create new recipe
        [3] - Create new category
        [4] - Eliminate recipe
        [5] - Eliminate category
        [6] - Leave the program''')
        menu_choice = input()

    return menu_choice

menu = int(start())

def show_categories(path):
    print("Categories:")
    categories_path = Path(path)
    categories_list = []
    counter = 1

    for folter in categories_path.iterdir():
        folder_str = str(folder.name)


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