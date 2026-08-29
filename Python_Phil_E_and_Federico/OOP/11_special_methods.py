'''Given the Book class, implement the special method __del__ so that the user is informed with the message 
"Book deleted", showing it on the screen every time a book is deleted.'''

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        
    def __del__(self, instance):
        return self.instance

    

Adminstracao = Book("A Administracao segundo", "Agusto Cury", 212)
print(Adminstracao.__delete__)