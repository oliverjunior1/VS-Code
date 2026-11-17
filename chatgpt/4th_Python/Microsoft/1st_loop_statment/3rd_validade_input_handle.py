""" total_price = 100
item_count = 0
average_price = total_price / item_count
print(average_price) """
""" 
total_price = 100
item_count = 0

try:
    average_price = total_price / item_count
except ZeroDivisionError:
    print("Error: Can't divide by zero. The cart has no items.")

print("Program continues running") """


""" count_text = "abc"

try:
    item_count = int(count_text)
    average_price = 100 / item_count
    print(average_price)
except ValueError:
    print("The item count must be a whole number.")
except ZeroDivisionError:
    print("The item count can't be zero.") """



