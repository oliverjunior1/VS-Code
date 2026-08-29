'''
Special Methods Practice #1
Given the Book class, implement the special method __str__ so that each time the object is printed, 
it returns '"{title}", from {author}' (note: the title must be enclosed in double quotes).'''

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def __str__(self):
        return f"Title:{self.title}, \nAuthor:{self.author}"

Plato = Book("Allegory of the cave", "Plato")

print(Plato)