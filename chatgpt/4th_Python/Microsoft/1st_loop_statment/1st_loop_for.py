""" for count in range(6):
    if count == 3:
        continue
    print(count) """

""" while True:
    user_input = input("Type 'exit' to stop the loop: ")
    if user_input.lower() == "exit":
        break
    print(f"You entered: {user_input}")

print("Goodbye!") """

""" current_slot = 0

while current_slot < 5:
    current_slot += 1

    if current_slot == 3:
        print(f"Skipping item slot {current_slot} ")
        continue # aborts the rest of this lap and jumps back to the top

    # This processing code is skipped when current_slot is 3
    print(f"Successfully processed item in slot {current_slot}.")

print("Inventory scan complete!") """

color = "blue"

for i in range(3):
    user_input = input("Guess my favorite color: ")
    if user_input.lower() == color:
        print("You guessed it")
        break
else:
    print(f"Sorry, the correct answer is {color}.")
