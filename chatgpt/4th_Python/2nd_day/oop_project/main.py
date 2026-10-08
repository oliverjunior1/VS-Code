from models.book import Book

# Create two Book objects
book1 = Book("Python for Beginners", "Anna Smith", 100.00)
book2 = Book("Database Fundamentals", "John Brown", 80.00)

book1.display_information()
print()

book2.display_information()

# Apply a discount only to the first book
book1.apply_duscount(10)

print("\nAfter the discount:")
book1.display_information()