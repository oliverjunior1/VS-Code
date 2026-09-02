'''Create a generator that subtracts the lives of a video game character one by one, and returns a 
message each time it is called:
"You have 3 lives left"
"You have 2 lives left"
"You have 1 live left"
"Game Over"
Store the generator in the variable lose_live'''

def character():
    lives = 4
    while lives > 0:
        yield lives
        lives -= 1

# Criar o generator
lose_live = character()

# Consumir os valores com next()
try:
    while True:
        lives_left = next(lose_live)
        print(f"You have {lives_left} lives left")
except StopIteration:
    print("Game Over")


 