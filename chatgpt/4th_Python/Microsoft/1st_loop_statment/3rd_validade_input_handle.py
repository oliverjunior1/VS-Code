""" total_price = 100
item_count = 0
average_price = total_price / item_count
print(average_price) """

total_price = 100
item_count = 0

try:
    average_price = total_price / item_count
except ZeroDivisionError:
    print("Error: Can't divide by zero. The cart has no items.")

print("Program continues running")