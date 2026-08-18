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


from pathlib import Path

base = Path.home()
guide = Path(base, 'Europe', 'France', Path('Paris', 'Eiffel_tower.txt'))
print(guide.parent.parent.parent)
