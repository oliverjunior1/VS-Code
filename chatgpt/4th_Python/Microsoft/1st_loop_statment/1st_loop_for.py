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

""" color = "blue"

for i in range(3):
    user_input = input("Guess my favorite color: ")
    if user_input.lower() == color:
        print("You guessed it")
        break
else:
    print(f"Sorry, the correct answer is {color}.") """


""" 
In this exercise, you build a Guess the Number game. The program picks a random number and uses a while 
loop to keep asking the player to guess until they get it right. """

from random import randint

guess_number = randint(1, 100)
counter = 6

while counter > 0:
    input_number = int(input("Put a number: "))

    if input_number > guess_number:
        counter -= 1
        print("It is less than that.")
        print(f"Careful. You have {counter} lives left.")

    elif input_number < guess_number:
        counter -= 1
        print("It is greater than that.")
        print(f"Careful. You have {counter} lives left.")

    else:
        print(f"You win. The number is {guess_number}")
        break

if counter == 0 and input_number != guess_number:
    print(f"You lose. The guessed number was {guess_number}")
    

    
        

