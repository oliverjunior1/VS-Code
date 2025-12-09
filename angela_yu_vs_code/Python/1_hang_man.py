# Hangman Game
import random
def hangman():
    word_list = ['python', 'java', 'kotlin', 'javascript']
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)
    display = ['_'] * word_length
    lives = 6
    end_of_game = False

    print("Welcome to Hangman!")
    
    while not end_of_game:
        guess = input("Guess a letter: ").lower()

        if guess in display:
            print(f"You've already guessed {guess}")

        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        if guess not in chosen_word:
            lives -= 1
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            if lives == 0:
                end_of_game = True
                print("You lose.")

        print(f"{' '.join(display)}")

        if '_' not in display:
            end_of_game = True
            print("You win.")

hangman()