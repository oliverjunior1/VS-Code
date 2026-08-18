"""
Open and Manipulate Files Practice #1
Open the file my_text.txt and print its content.

Note: assume that the file is saved in the same folder where your code is located"""

# x = open("C:\\Users\\Olive\\VS Code\\Python_Phil_E_and_Federico\\test.txt", 'r')

# print(x.readlines())

# with open("Python_Phil_E_and_Federico\\my_text.txt", 'r') as f:
#     print(f.readlines())

# with open("test.txt") as x:
#     print(x.readline())
#################################diretório_direcionado############################################
# import os

# path = os.chdir("C:\\Users\\Olive\\VS Code\\Python_Phil_E_and_Federico")

# file = open('my_text.txt')

# print(file.read())


# from pathlib import Path

# folder = Path('Python_Phil_E_and_Federico')
# file = folder / 'my_text.txt'

# my_file = open(file)
# print(my_file.read())


# from pathlib import Path

# folder = Path('Python_Phil_E_and_Federico') / 'my_text.txt'

# my_file = open(folder)
# print(my_file.read())

#################################Pathlib####################################

# from pathlib import Path

# folder = Path("C:\\Users\\Olive\\VS Code\\Python_Phil_E_and_Federico\\test.txt")

# # print(folder.read_text())
# print(folder.stem)

####################################Path######################################

# from pathlib import Path

# guide = Path('Paris', 'Eiffel_tower.txt')
# print(guide)


# from pathlib import Path

# base = Path.home()
# guide = Path(base, 'Europe', 'France', Path('Paris', 'Eiffel_tower.txt'))
# print(guide.parent.parent.parent)


# from pathlib import Path

# guide = Path(Path.home(), 'Europe')

# for txt in Path(guide).glob('**/*.txt'):
#     print(txt)


# from pathlib import Path

# guide = Path('Europe', 'France', 'Paris', 'Eiffel_tower.txt')

# in_europe = guide.relative_to(Path('Europe'))
# in_france = guide.relative_to(Path('Europe', 'France'))

# print(in_europe)
# print(in_france)


##################################Exercises#####################################
"""Path Practice #1
Store in the base_path variable, a Path object that points to the user's base directory.

Remember to import Path from the pathlib module, and use the home() method"""

# from pathlib import Path

# # cria um objeto Path que aponta para o diretório base do usuário
# base_path = Path.home()

# print(base_path)


'''Path Practice #2
Implement and create a relative path that allows us to reach the file path_practice.py from the following folder structure:
Store that directory in the my_path variable. Don't forget to import Path.'''
# from pathlib import Path

# # Supondo que você esteja dentro da pasta "exercises"
# # e o arquivo path_practice.py esteja em uma subpasta chamada "practice"
# my_path = Path("practice/path_practice.py")

# print(my_path)


################################Clean_console########################################

name = input('Tell me your name: ')
age = input("Tell me your age: ")

print(f"Your name is {name}, and you are {age} years old")


