
import random

words = ["father", "singing", "jail", "grandfather"]

def print_underscores(word):
    """Prints underscores for each character in the given word."""
    for _ in word:
        print("_", end=" ")

def check_user_input(word):
    """Checks if the user's input matches the given word."""
    user_input = input("Enter the string to match underscore: ")
    if user_input.strip() == word:
        print("You win!")
       
    else:
        print("You lose.")
        print(f"correct answer is:{word}")

def gamecal():
    """Plays a round of the Word Guessing game."""
    word = random.choice(words)
    print_underscores(word)
    check_user_input(word)

def play_game():
    """Plays the Word Guessing game until the user chooses to quit."""
    gamecal()
    while True:
        response = input("Want to play again? (y/n): ")
        if response.lower() == "y":
            gamecal()
        else:
            print("Bye!")
            break

play_game()
