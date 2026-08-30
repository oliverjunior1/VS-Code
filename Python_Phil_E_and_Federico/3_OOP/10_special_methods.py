'''Given the Book class, implement the special method __len__ so that each time the len() 
function is executed on it, it returns the number of pages as an integer.'''

class Book:
    def __init__(self, author, title, pages):
        self.author = author
        self.title = title
        self.pages = pages

    def __len__(self):
        return self.pages

    


Acts = Book("Paul", "Acts",35)

print(len(Acts))
