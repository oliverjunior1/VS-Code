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



""" def check_age(age_text):
    "Return the age as an int from 0 to 150, or None if the input is valid."
    try:
        age = int(age_text)
    except (ValueError, TypeError):
        return None

    if age < 0 or age > 150:
        return None

    return age

print(check_age("25"))
print(check_age('abc'))
print(check_age("-5"))
print(check_age("200")) """



""" def calculate_average(total_price: float, item_count: int) -> float:
    "Return the average price per item"
    if item_count <= 0:
        raise ValueError("Item_count must be greater than zero.")
    return total_price / item_count

try:
    print(calculate_average(100,0))
except ValueError as error:
    print(f"Invalid Input: {error}") """

