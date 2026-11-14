""" for count in range(6):
    if count == 3:
        continue
    print(count) """

while True:
    user_input = input("Type 'exit' to stop the loop: ")
    if user_input.lower() == "exit":
        break
    print(f"You entered: {user_input}")

print("Goodbye!")