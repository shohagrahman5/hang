import random

# A small list of words for the game
WORDS = ["python", "computer", "hangman", "program", "developer"]


def show_word(word, guessed_letters):
    """Show guessed letters and hide the remaining letters."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def play_game():
    word = random.choice(WORDS)
    guessed_letters = []
    wrong_guesses = 0
    max_wrong_guesses = 6

    print("\n===== WELCOME TO HANGMAN =====")
    print("Guess the word one letter at a time.")
    print("You can make 6 incorrect guesses.")

    while wrong_guesses < max_wrong_guesses:
        print("\nWord:", show_word(word, guessed_letters))
        print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

        guess = input("Enter one letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one alphabet letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct guess!")
        else:
            wrong_guesses += 1
            print("Wrong guess!")

        # Check whether all letters have been guessed
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            break
    else:
        print("\nGame over! The correct word was:", word)

    print("Thanks for playing!")


if __name__ == "__main__":
    play_game()
