"""
Open and Manipulate Files Practice #1
Open the file my_text.txt and print its content.

Note: assume that the file is saved in the same folder where your code is located"""

# x = open("C:\\Users\\Olive\\VS Code\\Python_Phil_E_and_Federico\\test.txt", 'r')

# print(x.readlines())

with open("Python_Phil_E_and_Federico\\my_text.txt", 'r') as f:
    print(f.readlines())